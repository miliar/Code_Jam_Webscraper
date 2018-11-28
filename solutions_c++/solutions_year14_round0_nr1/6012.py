/****************************************
* File Name: a.cpp
* Author: sky0917
* Created Time: 2014Äê04ÔÂ12ÈÕ  9:51:06
****************************************/
#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 20;
int a[maxn];
int b[maxn];
int main(){
  //  freopen("A-small-attempt0.in","r",stdin);
  //  freopen("A-small-attempt0.out","w",stdout);
	int T;
    int ca = 1;
    scanf("%d",&T);
    while (T--){
		int f, s, p;
	    scanf("%d",&f);
	    for (int i=1; i<=4; i++){
			for (int j=0; j<4; j++){
				scanf("%d",&p);
				a[p] = i;
			}
		}
		scanf("%d",&s);
		for (int i=1; i<=4; i++){
			for (int j=0; j<4; j++){
				scanf("%d",&p);
				b[p] = i;
			}
		}
		int cnt = 0;
		int res;
		for (int i=1; i<=16; i++){
			if (a[i] == f && b[i] == s){
				res = i;
				cnt++;
			}
		}
		printf("Case #%d: ",ca++);
		if (cnt == 1)printf("%d\n",res);
		else if (cnt == 0)
			printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
