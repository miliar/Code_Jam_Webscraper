#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <limits.h>
#include<string.h>
using namespace std;
typedef long long l;
#define mod 1000000007
char s1[105],s2[105];
int ab(int x,int y){
	if((x-y)<0)return y-x;
	return x-y;
}
int main(){
	int t,co=1;
	scanf("%d",&t);
//	printf("t is %d\n",t);
	while(t--){
	//	printf("dsfa %d\n",t);
		int n,ans=0;
		bool f=true;
		scanf("%d ",&n);
		scanf("%s %s",s1,s2);
			printf("Case #%d: ",co);
		int len1=strlen(s1),len2=strlen(s2);
			int i=0,j=0;char curr1,curr2;
			int t1=1,t2=1;
			if(s1[0]!=s2[0]){
				printf("Fegla Won\n");
				co++;
				continue;
			}
			while(i<len1 || j<len2){
											
					curr1=s1[i];		
				while(i<len1 && s1[i]==s1[i+1]){
					i++;
					t1++;
				}
				
					curr2=s2[j];
				while(j<len2 && s2[j]==s2[j+1]){
					j++;
					t2++;
				}
			//	printf("curr1,curr2,i,j,t1,t2 are %c %c %d %d %d %d\n",curr1,curr2,i,j,t1,t2);
				if(curr1==curr2){
					ans+=ab(t1,t2);
				}else{
					f=false;
					printf("Fegla Won\n");
					break;
				}
				t1=1;
				t2=1;
				i++;j++;
			}
			if(f==true){
				printf("%d\n",ans);
			}
		co++;
	}
	return 0;
}

