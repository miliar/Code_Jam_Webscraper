#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

struct pancake{
	string side;
	int step;
	pancake(string a, int b){
		side = a;
		step = b;
	}
};

char opposite(char c){
	if (c == '+') return '-';
	if (c == '-') return '+';
}

bool allsmile(string s){
	for (int i = 0; i < s.length();i++)
		if (s[i] == '-') return false;
	return true;
}

bool notinqueue(string s, vector<pancake> q){
	for (int i = 0; i < q.size();i++)
		if (s == q[i].side) return false;
	return true;
}

int bfs(string s){
	if (allsmile(s)) return 0;
	vector<pancake> q;
	q.clear();
	pancake p(s,0);
	q.push_back(p);
	int current = 0,tail = 0,l = s.length();
	string s1,s2;
	while (current <= tail){
		s1 = q[current].side;
		//cout << current << ' ' << tail << ' ' << s1 << endl;
		for (int i = 1; i <= l; i++ ){
			s2 = "";
			for (int j = i-1; j >= 0; j--)
				s2 = s2 + opposite(s1[j]);
			for (int j = i; j < l; j++) 
				s2 = s2 + s1[j];
			if (allsmile(s2)) return (q[current].step +1);
			else if (notinqueue(s2,q)){
				pancake p(s2,q[current].step+1);
				q.push_back(p);
				tail++;
			}
		}
		current ++;
	}
}


int main(){
	ifstream in("B-small-attempt1.in");
	ofstream out("pancake.out");
	int t;
	string s;
	in >> t;
	for (int x = 0; x < t;x++){
		in >> s;
		out << "Case #" << x+1 << ": " << bfs(s) << endl;
		cout << "Case #" << x << ": " << bfs(s) << endl;
	}
}
