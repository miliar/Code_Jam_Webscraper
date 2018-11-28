#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int splitFirst(vector<int> p);
int eatOne(vector<int> p);
int recurse(vector<int> p);
int splitDiv3(vector<int> p);

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		int d;
		cin >> d;
		vector<int> p;
		int temp;
		for(int j = 0; j < d; j++){
			cin >> temp;
			p.push_back(temp);
		}
		sort(p.begin(), p.end(), greater<int>());
		cout << "Case #" << i << ": ";
		cout << recurse(p) << endl;
	}
	return 0;
}

int splitFirst(vector<int> p){
	if(p[0] < 4)
		return 100000;
	//cout << "here" << endl;
	int rem = p[0] % 2;
	p.push_back(p[0]/2);
	p[0] = p[0]/2 + rem;
	sort(p.begin(), p.end(), greater<int>());
	return 1 + recurse(p);
}

int splitDiv3(vector<int> p){
	if(p[0] < 4)
		return 100000;
	//cout << "here" << endl;
	int rem = p[0] % 3;
	p.push_back(p[0]/3);
	p[0] = p[0]/3 + p[0]/3 + rem;
	sort(p.begin(), p.end(), greater<int>());
	return 1 + recurse(p);
}

int eatOne(vector<int> p){
	int i;
	for(i = p.size()-1; i >= 0; i--){
		if(p[i] <= 1)
			p.erase(p.begin()+i);
		else
			break;
	}
	for(i = 0; i < p.size(); i++)
		p[i]--;
	return 1 + recurse(p);
}

int recurse(vector<int> p){
	if(p.empty())
		return 0;
	//for(int i = 0; i < p.size(); i++)
	//	cout << p[i] << " ";
	//cout << endl;
	if(p[0] >= 4)
		return min(splitFirst(p), min(splitDiv3(p), eatOne(p)));
	return eatOne(p);
}