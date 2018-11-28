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

string mins[20][3];

void init(){
	mins[0][0]=string("P");
	mins[0][1]=string("R");
	mins[0][2]=string("S");
	
	reg(i,1,15){
		rep(j,3){
			int p=(j+1)%3,q=(j+2)%3;
			string &s1 = mins[i-1][p];
			string &s2 = mins[i-1][q];
			if(s1<s2)mins[i][j]=(s1+s2);
			else mins[i][j]=(s2+s1);
		}
	}
}

int main(void){
	init();
	int qn;
	scanf("%d",&qn);
	reg(i,1,qn){
		int n,r,p,s;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		string ans("IMPOSSIBLE");
		if(r==s){
			if(abs(p-r)==1){
				ans = mins[n][0];
			}
		}
		else if(s==p){
			if(abs(p-r)==1){
				ans = mins[n][1];
			}
		}
		else if(p==r){
			if(abs(p-s)==1){
				ans = mins[n][2];
			}
		}
		printf("Case #%d: %s\n",i,ans.c_str());
	}
	return 0;
}




