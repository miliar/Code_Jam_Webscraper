#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main()
{
	int test;
	cin >> test;
	for (int ii = 0; ii < test; ii++){
		int s;
		cin >> s;
		int ans = 0,cur;
		char st[1001];
		cin >> st;
		cur = st[0] - '0';
		for (int i = 1; i <= s; i++){
			int si = st[i]-'0';
			if (i > cur && si!=0){
				ans += i-cur;
				cur = i + si;
			}
			else cur += si;
		}
		printf("Case #%d: %d\n",ii+1, ans);
	}
return 0;
}
