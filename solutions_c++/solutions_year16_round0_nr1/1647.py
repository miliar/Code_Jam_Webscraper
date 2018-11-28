#include <iostream>
using namespace std;

typedef long long ll;

int main() {
	// your code goes here
	ll N, T, i, j, ans, m;
	cin>>T;
	for(int k=1; k<=T; ++k) {
	cin>>N;
	cout<<"Case #"<<k<<": ";
	if(N==0)
	{
		cout<<"INSOMNIA"<<endl;
		continue;
	}
	ll m, b[10]={};
	i=1;
	while(1)
	{
		m=i*N;
		while(m) {
			ll z=m%10;
			b[z]++;
			m/=10;
		}
		bool flag=true;
		for(j=0; j<10; ++j)
			if(b[j]==0)
			{
				flag=false;
				break;
			}
		if(flag)
			break;
		i++;
	}
	cout<<i*N<<endl;
	}
	return 0;
}