#include <iostream>
#include <set>
#include <queue>
using namespace std;

void convert(string s, bool *flag){
	int l = s.size();
	for(int i = 0; i < l; i ++){
		if(s[i] == '+')
			flag[i] = 1;
		else
			flag[i] = 0;
	}
}

bool check(bool *flag, int sSize){
	for(int i = 0; i < sSize; i ++){
		if(flag[i] == 0)
			return false;
	}
	return true;
}

bool checkNF(bool *flag, int j){
	for(int i = 1; i <= j; i ++)
		if(flag[i] != flag[i - 1])
			return false;
	return true;
}

int main(){
	int t;
	string s;
	cin >> t;

	for(int i = 1; i <= t; i ++){
		cout << "Case #" << i << ": ";
		cin >> s;
		int sSize = s.size();
		queue <pair<bool*, pair<int, int> > > q;//array, steps, pos
		bool *flag = new bool[sSize];
		convert(s, flag);
		q.push(make_pair(flag, make_pair(0, -1)));
		while(q.size() > 0){
			pair <bool *, pair<int, int> > e = q.front();
			bool *eF = e.first;
			int steps = e.second.first;
			int pos = e.second.second;
			if(check(eF, sSize)){
				cout << steps << endl;
				break;
			}
			for(int j = pos + 1; j < sSize; j ++){
				bool *nF = new bool[sSize];
				memcpy(nF, eF, sSize);
				for(int k = j; k >= 0; k --){
					nF[j - k] = 1 - eF[k];
				}
				if(!checkNF(nF, j)){
					delete[] nF;
					continue;
				}
				q.push(make_pair(nF, make_pair(steps + 1, j)));
			}
			delete[] eF;
			q.pop();
		}
		while(q.size() > 0){
			pair <bool *, pair<int, int> > e = q.front();
			bool *eF = e.first;
			delete[] eF;
			q.pop();
		}
	}
	return 0;
}

