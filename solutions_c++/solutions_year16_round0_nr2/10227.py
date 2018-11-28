#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;
int ret[1 << 10];
void init(){
	for(int i = 0; i < (1 << 10); i++)
		ret[i] = -1;
	//- => 1
	//+ => 0
	ret[0] = 0;
	queue<int> q;
	q.push(0);
	while(!q.empty()){
		int t = q.front();
		q.pop();
		for(int i = 0; i < 10; i++){
			int tt = t ^ (((1 << (i + 1)) - 1) << (9 - i));
			if (ret[tt] == -1){
				ret[tt] = ret[t] + 1;
				q.push(tt);
			}
		}
	}
}

int calc(string &s){
	int ret = 0;
	for(int i = 0; i < s.length(); i++){
		ret <<= 1;
		if (s[i] == '-')
			ret ++;
	}
	return ret << (10 - s.length());
}
int main(){
	init();
	int ntest;
	cin >> ntest;
	string s;
	for(int i = 1; i <= ntest;i ++){
		cin >> s;
		cout << "Case #" << i << ": " << ret[calc(s)] << endl;
	}
	return 0;
}
