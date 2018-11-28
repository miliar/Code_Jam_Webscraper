#include<iostream>
#include<string.h>
#include<stdio.h>
#include<vector>
#include<cmath>
#include<stack>
#include<ctime>
#include<set>
#include<map>
#include<queue>

#pragma comment(linker, "/STACK:268435456")

#define _min(a,b) ((a<b)?(a):(b))
#define _max(a,b) ((a<b)?(b):(a))
#define sqr(x) ((x)*(x))
#define _abs(a) ((a<0)?(-a):(a))
#define eps 1.0E-6
#define PI acos(-1.0)

typedef unsigned long long ull;
typedef long long ll;

using namespace std;

ll _gcd(ll a,ll b)
{
    if(b==0)return a;
    _gcd(b,a%b);
}
//*******************************************************************************************************


int main()
{
 
freopen("A-small-attempt0.in.","r",stdin);
freopen("output.txt","w",stdout);



int t,a[4][4],b[4][4],c[17],l,r;

cin>>t;


for(int k=0;k<t;++k)
{

for(int i=0;i<17;++i)
c[i]=0;

cin>>l;
for(int i=0;i<4;++i)
for(int j=0;j<4;++j)
cin>>a[i][j];
	
	
cin>>r;
for(int i=0;i<4;++i)
for(int j=0;j<4;++j)
cin>>b[i][j];
	
l--;
r--;

for(int i=0;i<4;++i)
c[a[l][i]]++;

for(int i=0;i<4;++i)
c[b[r][i]]++;


int u=0,res;
for(int i=1;i<17;++i)
if(c[i]==2)u++,res=i;

if(u==1)
{
	cout<<"Case #"<<k+1<<": "<<res<<endl;
}

if(u>1)
{
	cout<<"Case #"<<k+1<<": Bad magician!"<<endl;
}

if(u==0)
{
	cout<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
}


}



}
