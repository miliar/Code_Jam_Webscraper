#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int mapn[5][5]={0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
int GetVal(char x){
	if(x=='i')return 2;
	if(x=='j')return 3;
	if(x=='k')return 4;
}
int GetRes(int a,long long b,char* arr){
	//printf("a b %d %lld %s\n",a,b,arr);
	long long x=(b%2);long long y=(b%4);x=int(x);y=int(y);
	int now=GetVal(arr[0]);
	int flag=1;
	for(int i=1;i<a;i++){
		int t=GetVal(arr[i]);
		int xnow=mapn[now][t];
		if(xnow<0){
			xnow=-xnow;
			flag*=-1;
		}
		now=xnow;
	}
	//cout << now << endl;
	if(now==1&&flag==-1&&x==1){return 1;}
	if(now==-1&&flag==1&&x==1){return 1;}
	if(now>1 && x==0 && y!=0){return 1;}
	if(now<-1 && x==0 && y!=0){return 1;}
	return 0;
}
int main(int argc,char **argv)
{
    freopen("A.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int cnt,n;long long x;
	cin >> cnt;
	for(int i=1;i<=cnt;i++){
		char str[12000];
		printf("Case #%d: ", i);
		scanf("%d %lld",&n,&x);scanf("%s",str);
		int ans_res=GetRes(n,x,str);
		if(ans_res==1)
			printf("YES\n");
		else
			printf("NO\n");
	}
} 
