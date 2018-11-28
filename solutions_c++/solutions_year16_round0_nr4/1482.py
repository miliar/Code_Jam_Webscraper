#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;

#define ll long long

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	ll list[100];
	for(int tnum=1; tnum<=T; ++tnum)
	{
		int k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << tnum <<": ";
		if(k==1)
			cout << "1\n";
		else if (c==1){
			if(s==k)
				for(int i=1; i<=k; ++i)
					cout << i << " ";
			else
				cout << "IMPOSSIBLE";
			cout << endl;
		}else{
			/*ll x=1;
			for(int i=0; i<c; ++i)
				x*=k;
			ll x1=x/k;
			int cnt=0, i=0;
			ll pos=2;
			for(; i<k/2; i+=2, pos+=x1)
				list[cnt++]=pos;
			pos=x-1;
			for(int j=k-1; j>=i; j-=2, pos-=x1)
				list[cnt++]=pos;
			if(cnt>s)
				cout << "IMPOSSIBLE";
			else
				for(int i=0; i<cnt; ++i)
					cout << list[i] << " ";
			cout << endl;*/
			for(int i=1; i<=k; ++i)
				cout << i << " ";
			cout << endl; 
		}
	}
}