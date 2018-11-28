//This code was writen by Alexander Dryapko (sdryapko)
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

using namespace std;
bool used[211][211];
int a[211][211],tt,n,m;

int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout); 
        cin>>tt;
        for (int t=1;t<=tt;t++) {
        	printf("Case #%d: ",t);
       		cin>>n>>m;
       		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) cin>>a[i][j];
       		memset(used,0,sizeof(used));
                bool ok=true;
		while (true) {
       			int q1,q2,_min=maxi;
       			for (int i=1;i<=n;i++) for (int j=1;j<=m;j++) if (used[i][j]==false&&a[i][j]<_min) {
       				_min=a[i][j];
       				q1=i;
       				q2=j;
       			}
       			if (_min==maxi) break;
       			bool vert=true,hor=true;
       			for (int i=1;i<=n;i++) if (used[i][q2]==false&&a[i][q2]!=a[q1][q2]) {
       				vert=false;
       				break;
       			}	
       			for (int i=1;i<=m;i++) if (used[q1][i]==false&&a[q1][i]!=a[q1][q2]) {
       				hor=false;
       				break;
       			}
       			if (vert+hor==0) {
       				ok=false;
       				break;
       			}
       			if (vert) for (int i=1;i<=n;i++) used[i][q2]=1;
       			if (hor) for (int j=1;j<=m;j++) used[q1][j]=1;
       	     }
       	     if (ok) puts("YES"); else puts("NO");
       }
       return 0;
}
