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
 

freopen("B-small-attempt0.in.","r",stdin);
//freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);



int g;
cin>>g;


for(int j=0;j<g;++j)
{

double C,F,X,p=2.0,k=0.0;
cin>>C>>F>>X;
double res=(X)/2.0;
for(int i=0;i<10000;++i)
{
	double r=(C)/p;
	double l=r;
	k+=r;
	p+=F;
	
	r+=(X)/p+k-l;
	
	if(r<res)res=r;
}
printf("Case #%d: %0.7f\n",j+1,res);

}


}
