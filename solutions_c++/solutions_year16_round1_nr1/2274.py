/******************************************************
 * File Name:   a.cpp
 * Author:      kojimai
 * Create Time: Fri 15 Apr 2016 06:04:46 PM PDT
******************************************************/

#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
char s[1005];
int next[1005];
int main() {
	int T;
	freopen("out.out","w",stdout);
	scanf("%d",&T);
	for(int Cas = 1;Cas <= T;Cas++) {
		scanf("%s",s);
		printf("Case #%d: ",Cas);
		memset(next,-1,sizeof(next));
		int first = 0,last = 0;
		for(int j = 1;s[j] != '\0';j++) {
			if(s[j] >= s[first]) {
				next[j] = first;
				first = j;
			}
			else {
				next[last] = j;
				last = j;
			}
		}
		while(first != -1) {
			printf("%c",s[first]);
			first = next[first];
		}
		cout << endl;
	}
	return 0;
}
