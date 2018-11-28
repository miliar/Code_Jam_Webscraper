#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
#include<iostream>
using namespace std;
#define rep(i,n) for(int i=0;i<((int)(n));i++)
#define reg(i,a,b) for(int i=((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i=((int)(n))-1;i>=0;i--)
#define ireg(i,a,b) for(int i=((int)(b));i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int,int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define pque(type) priority_queue<type,vector<type>,greater<type> >
#define memst(a,b) memset(a,b,sizeof(a))


char s[150005];
int main(void){
	int qn;
	scanf("%d",&qn);
	reg(qqq,1,qn){
		scanf("%s",s);
		int a=0,b=0,c=0;
		int ls=strlen(s);
		rep(i,ls){
			if(s[i]!='C')continue;
			if(i%2)a++;
			else b++;
			c++;
		}
		a = min(a,b);
		b = c-a*2;
		int ans = a*10+b*5+(ls/2-a-b)*10;
		printf("Case #%d: %d\n",qqq,ans);
	}
	return 0;
}




