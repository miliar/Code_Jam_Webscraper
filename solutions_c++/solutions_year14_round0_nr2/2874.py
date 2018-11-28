//This code was writen by Aliaksandr Driapko (sdryapko)
#include<sstream>
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>                             	
#include<set>               
#include<string>
#include<string.h>  
#include<deque>
#include<ctime>
#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define pw2(x) (1ll<<(x))
#define F first
#define S second
const int maxi=2000000000;              
const int maxq=1000000000;
const double eps=1e-10;       
const double pi=3.1415926535897932;
const double inf=1e+18;
const int mo=1000000007;
const int maxn=100000;
using namespace std;
int tt;
double c,f,x;
double f1(int n) {
	double tim=0;
        double kol=2.0;
        for (int j=1;j<=n;j++) {
        	double tmp=c/kol; 
        	tim+=tmp;
        	kol+=f;
        }                         
       return tim+x/kol;
}
        
int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout); 
        cin>>tt;
        for (int t=1;t<=tt;t++) {
        	cin>>c>>f>>x;
        	double ans=inf;
                int l=0;
                int r=(int) x+1;
                while (r-l>100) {
                	int l1=l+(r-l)/3;
                	int l2=r-(r-l)/3;
                	if (f1(l1)<f1(l2)) r=l2; else l=l1;
                }
                for (int i=l;i<=r;i++) ans=min(ans,f1(i));
        	printf("Case #%d: %.8lf\n",t,ans);

        }
       	return 0;
}
