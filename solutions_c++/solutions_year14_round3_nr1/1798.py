#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;

int f(int p, int q, int x);
int g(int q, int x);

int main()
{
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,count;

	cin>>T;
	count = 1;
	while(T--){
	
		int P,Q;
		char slash;
		cin>>P>>slash>>Q;

		cout<<"Case #"<<count<<": ";

		int x = f(P,Q,40);
		if(x<0) cout<<"impossible"<<endl;
		else cout<<x<<endl;
		
		count++;
	}

	return 0;
}

int f(int p, int q, int x)
{
	if(x<0) return -100;

	if (!g(q,x)) return -100;

	double y = 2*(double)(p) /q;
	if( 0 <= (y - 1) && (y-1) <= 1) return 1;

	else return 1 + f(2*p,q,x-1);
}

int g(int q,int x)
{
	for(int i=0; i<=x; i++)
		if( (double) q == pow(2.0,i) ) return true;

	return false;

}