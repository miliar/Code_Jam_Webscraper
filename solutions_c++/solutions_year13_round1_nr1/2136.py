#include <iostream>
#include <string>
#include <sstream>

#define _for(i,n) for(int i = 0; i<n; i++)
#define _fora(i,n) for(int i = 1; i<=n; i++)
#define _forlor(i,n) for(int i=n-1; i>=0; i--)
#define max(a,b) a<b?b:a

using namespace std;

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);

	int T;
	cin>>T;
	_fora(t,T){
		long long r,
			tot,
			x=0;
		cin>>r>>tot;
		do 
		{
			tot -= (++x)*4 + r*2 -3;
		} while (tot>=0);
		cout<<"Case #"<<t<<": "<<(x-1)<<endl;
	}

	return 0;
}