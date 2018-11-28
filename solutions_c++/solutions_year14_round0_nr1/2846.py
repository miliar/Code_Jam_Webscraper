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
int tt,q1,q2,a[111][111],b[111][111];
vector<int> v;
int main(){                 
        freopen("input.txt","r",stdin);                              
        freopen("output.txt","w",stdout); 
        scanf("%d\n",&tt);
        for (int t=1;t<=tt;t++) {
        	scanf("%d\n",&q1);
        	for (int i=1;i<=4;i++) {
        		for (int j=1;j<=4;j++) scanf("%d",&a[i][j]);
        		scanf("\n");
        	}
        	scanf("%d\n",&q2);
        	for (int i=1;i<=4;i++) {
        		for (int j=1;j<=4;j++) scanf("%d",&b[i][j]);
        		scanf("\n");
        	}
                v.clear();
        	for (int i=1;i<=4;i++) for (int j=1;j<=4;j++) if (a[q1][i]==b[q2][j]) v.push_back(a[q1][i]);
        	printf("Case #%d: ",t);
        	if (v.size()==0) puts("Volunteer cheated!"); 
        	else if (v.size()==1) cout<<v[0]<<endl;
        	else puts("Bad magician!");
        }
       	return 0;
}
