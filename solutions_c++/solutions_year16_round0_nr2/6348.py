#include<stdio.h>
#include<iostream>
#include<string>
#include<deque>
#include<algorithm>
using namespace std;
int T, N, i;
string str;
#define MAXN 99999999
typedef pair<string, int> psi;
int main() {
	scanf("%d", &T);
	for (i = 1; i <=T; i++){
		printf("Case #%d: ", i);
		cin >> str;
		int depth = 0;
		deque<pair<string,int>> deq;
		deq.push_front(psi(str,0));
		if (count(str.begin(), str.end(), '-') == 0){
			cout << deq.front().second << endl;
			goto L;
		}
		while (true){
			for (int i = 0; i < deq.front().first.size(); i++){
				if (deq.front().first[i] == '-'){
					string tmp = deq.front().first;
					for_each(tmp.begin(), tmp.begin() + i + 1, [](char& c)->void{if (c == '-')c = '+'; else c = '-'; });
					if (count(tmp.begin(), tmp.end(), '-') == 0){
						cout << deq.front().second + 1 << endl;
						goto L;
					}
					else{
						//reverse(tmp.begin(), tmp.end());
						if (tmp != str){
							deq.push_back(psi(tmp, deq.front().second + 1));
						}
					}
				}
			}
			deq.pop_front();
		}
L:{}
	}
	return 0;
}