#include<iostream>
#include<deque>
#include<algorithm>
using namespace std;
int main(){
	int n;
	cin >> n;
	for(int i = 1; i <= n; i++){
		string ch;
		deque<char> qc;
		cin >> ch;
		int j = 0;
		char front_char;
		while(j < ch.length()){
			if(j == 0){
				qc.push_back(ch[j]);
				front_char = qc.front();
				j++;
				continue;
			}
			front_char = qc.front();
			if(front_char > ch[j]){
				//cout << "pb " << ch[j] << endl;
				qc.push_back(ch[j]);
			}else{
				//cout << "pf "<< ch[j] << endl;
				qc.push_front(ch[j]);
			}
			j++;
		}
		cout << "Case #" << i << ": ";
		while(!qc.empty()){
			cout << qc.front();
			qc.pop_front();
		}
		qc.clear();
		cout << endl;
	}
}
