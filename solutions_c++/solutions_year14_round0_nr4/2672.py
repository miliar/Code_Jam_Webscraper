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
int tt,n,used1[maxn],used2[maxn],t;
double a[maxn],b[maxn];
int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout); 
        cin>>t;
        for (int tt=1;tt<=t;tt++) {
        	scanf("%d\n",&n);
        	for (int i=1;i<=n;i++) cin>>a[i];
        	sort(a+1,a+n+1);
        	for (int i=1;i<=n;i++) cin>>b[i];
        	sort(b+1,b+n+1);
        	memset(used1,0,sizeof(used1));
        	memset(used2,0,sizeof(used2));
        	int ans1=0,ans2=0;
        	for (int i=1;i<=n;i++) {
        		bool flag=false;
        		for (int j=1;j<=n;j++) if (b[j]>a[i]&&used1[j]==false) {
        			flag=true;
        			used1[j]=1;
        			break;
        	        }
        	        if (!flag) ans1++;
               }
               for (int i=1;i<=n;i++) for (int j=1;j<=n;j++) if (a[i]>b[j]&&used2[j]==false) {
               		used2[j]=1;
               		ans2++;
               		break;
               }
               printf("Case #%d: %d %d\n",tt,ans2,ans1);
        }
       	return 0;
}
