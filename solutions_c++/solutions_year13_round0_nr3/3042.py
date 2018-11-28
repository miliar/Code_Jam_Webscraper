#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<string>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#define lim 1000
#define lli long long int
using namespace std;

bool check (int n) {
	int num=n,val=0;

	while(n!=0) {
		val=val*10+n%10;
		n/=10;
		}
	if(num==val)
		return true;
	return false;
	}

int main() {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small.out");
	int A[100],cnt=0;
	for(int i=1;i<40;i++) {
		if(check(i) && check(i*i)) {
			A[cnt++]=i*i;
			//cout<<i<<" "<<i*i<<endl;
			}
		}
	int t,a,b,ans;
	fin>>t;
	for(int k=1;k<=t;k++) {
		fin>>a;
		fin>>b;
		if(b>=484)
			ans=5;
		else if(b>=121)
			ans=4;
		else if(b>=9)
			ans=3;
		else if(b>=4)
			ans=2;
		else
			ans=1;
		a--;

		if(a>=484)
			ans-=5;
		else if(a>=121)
			ans-=4;
		else if(a>=9)
			ans-=3;
		else if(a>=4)
			ans-=2;
		else if(a>=1)
			ans-=1;
		else
			;
		fout<<"Case #"<<k<<": "<<ans<<endl;
		}

	return 0;
	}
