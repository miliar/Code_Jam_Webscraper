#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#include<string.h>
#include<cmath>
#include<iostream>
#include<vector>
#include<sstream>
#include <map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000000007

#define pn printf("\n")
#define pw printf(" ")
#define N 1000005
#define inf 1e7
typedef long long int ll;
using namespace std;
string s[105];int mark[105][105],flag=0,n,m;

int check(int i,int j){
if(i>=n||j>=m||i<0||j<0){return 0;}
return 1;}

int rec(int i,int j,int d){if(check(i,j)==0){return 0;}if(mark[i][j]==1){return 0;}
mark[i][j]=1;
if(flag==1){return 0;}

if(i==0&&d==1&&s[i][j]=='.'){flag=1;return 0;}
if(i==n-1&&d==2&&s[i][j]=='.'){flag=1;return 0;}
if(j==0&&d==3&&s[i][j]=='.'){flag=1;return 0;}
if(i==m-1&&d==4&&s[i][j]=='.'){flag=1;return 0;}




if(s[i][j]=='<'){rec(i,j-1,3);}
if(s[i][j]=='>'){rec(i,j+1,4);}
if(s[i][j]=='^'){rec(i-1,j,1);}
if(s[i][j]=='v'){rec(i+1,j,2);}
return 0;}


int main(){
int t,kase=0;
cin>>t;
while(t--){kase++;

int i,j,k,ans=0;
printf("Case #%d: ",kase);
cin>>n>>m;

rep(i,n){cin>>s[i];}
flag=0;


rep(i,n){rep(j,m){
memset(mark,0,sizeof(mark));
rec(i,j,-1);}}

if(flag==1){cout<<"IMPOSSIBLE";}
else{

rep(i,m){if(i==0||i==m-1){continue;}
if(s[0][i]=='^'){ans++;}}

rep(i,m){if(i==0||i==m-1){continue;}
if(s[n-1][i]=='v'){ans++;}}

if(s[0][0]=='^'||s[0][0]=='<'){ans++;}
if(m-1!=0&&s[0][m-1]=='^'||s[0][m-1]=='>'){ans++;}


if(s[n-1][0]=='v'||s[n-1][0]=='<'){ans++;}
if(m-1!=0&&s[n-1][m-1]=='v'||s[n-1][m-1]=='>'){ans++;}
cout<<ans;}

pn;}
return 0;}

