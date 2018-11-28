#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

#define rep(i,j,n) for(int i=j;i<n;i++)
typedef long long LL;
typedef pair<LL,LL> PLL;
typedef pair<int,int> PII;

LL t,a,b,c,cn;
string tmp;
int main(){
	cin>>t;
	while(t--){
		a=b=0;
		cin>>c>>tmp;
		rep(i,0,c+1){
			if(i>b && tmp[i]!='0'){
				a+=i-b;
				b=i;
			}
			b+=tmp[i]-'0';
		}
		cn++;
		cout<<"Case #"<<cn<<": "<<a<<(t?"\n":"");
	}
	return 0;
}