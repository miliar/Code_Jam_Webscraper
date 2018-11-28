#include <cstdio>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases = 0;
	scanf("%d",&cases);
	for(int casenum = 1; casenum <= cases; casenum++) {
		int ans1, ans2, a1[17]={0}, a2[17]={0}, t;
		char s[100];
		scanf("%d",&ans1);
		gets(s);
		for(int i=0;i<ans1-1;i++)gets(s);
		for(int i=0;i<4;i++) {
			scanf("%d",&t);
			a1[t]=1;
		}
		gets(s);
		for(int i=ans1;i<4;i++)gets(s);
		scanf("%d",&ans2);
		gets(s);
		for(int i=0;i<ans2-1;i++)gets(s);
		for(int i=0;i<4;i++) {
			scanf("%d",&t);
			a2[t]=1;
		}
		gets(s);
		for(int i=ans2;i<4;i++)gets(s);
		printf("Case #%d: ", casenum);
		int b=0, bi=-1;
		for(int i=1;i<=16;i++){
			if(a1[i]==1 && a2[i]==1){
				b++;
				bi=i;
			}
		}
		if(b==0){
			puts("Volunteer cheated!");
		}else if (b==1){
			printf("%d\n",bi);
		}else puts("Bad magician!");
	}
	return 0;
}