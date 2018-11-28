#include <iostream>
#include <cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
using namespace std;

long long 
gcdr ( long long  a, long long  b )
{
  if ( a==0 ) return b;
  return gcdr ( b%a, a );
}
int main()
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	cin>>tests;
	//long long pow[42];
	//pow[0]=1;
	//for (int i=1; i<42; i++)
	//	pow[i]=pow[i-1]*2;
	for (int t=0; t<tests; t++){
		long long p,q;
		char c;
	    cin>>p>>c>>q;
		long long g=gcdr(p,q);
		p/=g;
		q/=g;

		cout<<"Case #"<<t+1<<": ";
		long double ans=log(q*1.0)/log(2.0);
		if ((long long)ans!=ans) {
			cout<<"impossible"<<endl;
			continue;
		}
		int k=0;

		while (p*2<q) { q/=2; k++; };
		if (k+1<=40) 
		cout<<k+1<<endl;
		else cout<<"impossible"<<endl;
		//long double ans=log((q/p)*1.0)/log(2.0);
		//if ((long long)ans==ans &&  (long long)ans<=40)
		//cout<<max((long long)1,(long long)ans)<<endl;
	}
}