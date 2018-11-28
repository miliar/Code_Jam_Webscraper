#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<iostream>
#include<vector>
using namespace std;
char a[5000];
string s;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	int cas = 1;
	while (t--){
		printf("Case #%d: ",cas++);
		cin >> s;
		int len = s.length();
		int p = 2500;
		int l = p;
		int r = p;
		char pre = s[0];
		a[p] = pre;
		for (int i = 1; i < len; i++){
			if (s[i] >= pre){
				a[l - 1] = s[i];
				pre = s[i];
				l--;
			}
			else{
				a[r + 1] = s[i];
				r++;
			}
		}
		for (int i = l; i <= r; i++){
			printf("%c",a[i]);
		}
		printf("\n");
	}
	return 0;
}