#include<iostream>
#include<fstream>
#include<stdio.h>
#include<cstdio>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<ctype.h>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<iomanip>
#include<vector>
#include<map>
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define ff first
#define ss second
#define ll long long
#define pii pair< int, int >
#define MEM(p, v) memset(p, v, sizeof(p))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define S system("pause")
#define R return(0)
#define INF int(1e9)
#define MAX_5 int(1e5+5)
#define MAX_6 int(1e6+6)
#define ll long long
#define tree int h,int l1,int r1
#define left 2*h,l1,(l1+r1)/2
#define right 2*h+1,(l1+r1)/2+1,r1
using namespace std;
ll n,k,ans,d,a[1005],b[1005],x,r,c;
string s;
main()
{
	READ("a.in");
	WRITE("go.out");
int t;
cin>>t;
for(int o=1;o<=t;o++)
{
	cin>>x>>r>>c;
	if((x>r && x>c) || (r*c)%x!=0 || x>r*c)
	    {s="RICHARD",cout<<"Case #"<<o<<": "<<s<<endl;continue;}
	    
	if(x==1 || x==2){s="GABRIEL",cout<<"Case #"<<o<<": "<<s<<endl;continue;}
	if(x>=min(r,c)*2 || (min(r,c)>=3 && x>=7))
	    {s="RICHARD",cout<<"Case #"<<o<<": "<<s<<endl;continue;}
	s="GABRIEL",cout<<"Case #"<<o<<": "<<s<<endl;
	
	
	
	
}
}












