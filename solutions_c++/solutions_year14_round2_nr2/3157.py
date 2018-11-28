#include <iostream>
#include <cstdio>
#include <string>

using namespace std;


#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))

int main() {


//	freopen("A.in","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int t,tt;
	cin>>t;
	tt=t;
	while(t--)
	{
		cout<<"Case #"<<tt-t<<": ";
		unsigned int a,b; long long int c,k;
		cin>>a>>b>>k;
		c=0;
		for(int q=0;q<a;q++)
		for(int qq=0;qq<b;qq++)
		if((q&qq)<k)c++;
		cout<<c<<endl;
	}
	return 0;
};