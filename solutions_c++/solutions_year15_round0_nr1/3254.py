#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include <set>
#include <stack>
#include <queue>
#include <map>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define GCD(a,b)  { return (b==0)?a:GCD(b,a%b); }
#define LCM(a,b)  { return a*b/GCD(a,b);  }
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR_X(i,n,x) for(i=x;i<n;i++)
#define FORN(i,n) for(i=n;i>=0;i--)
#define FORN_X(i,n,x) for(i=n;i>=x;i--)
 
typedef long long int lld;
using namespace std;


int main(){
	
	int t;
	cin>>t;
	
	for(int k=1;k<=t;k++){
		int n,i;
		string s;
		cin>>n;
		cin>>s;
		
		int len = s.length();
		int frnds = 0;
		int now = 0;
		
		for(i=0;i<len;i++){
			
			if(i<=now){
				now = now + (s[i] - '0');
			}
			
			else {
				frnds = frnds + i-now;
				now = now + (s[i]-'0') +  i - now;
			}
		}
		
		printf("Case #%d: %d\n",k,frnds);
	}
	
	return 0;
	
}
			

