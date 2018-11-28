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
long long st[1111111];
int l,r,stn,tt;
bool pali(long long x) {
	stringstream q;
	string s="";
	q<<x;
	q>>s;
	string s1=s;
	reverse(s1.begin(),s1.end());
	if (s==s1) return true; else return false;
}
int f(int r) {
	int ans=0;
	for (int i=1;i<=stn;i++) if (pali(1ll*st[i]*st[i])&&1ll*st[i]*st[i]<=r) ans++; 
	return ans;
}
int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout); 
        cin>>tt;
        for (int i=1;i<=10000000;i++) if (pali(i)) {
        	stn++;
        	st[stn]=i;
        }
        for (int t=1;t<=tt;t++) {
        	printf("Case #%d: ",t);
       	        cin>>l>>r;
       	        cout<<f(r)-f(l-1)<<endl;
        }
       	return 0;
}
