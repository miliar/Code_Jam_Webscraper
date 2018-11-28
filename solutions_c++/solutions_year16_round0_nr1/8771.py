#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int n;
	cin>>n;
	for(int t=1;t<=n;t++){
		long long x,y,i;
		cin>>y;
		if(y==0){
			cout<<"Case #"<<t<<": INSOMNIA\n";
			continue;
		}
		int ch = 0;
		for(i=1;ch != (1<<10)-1;i++){
			x = i*y;
			for(;x!=0;x/=10)
				ch|=1<<(x%10);
		}
		cout<<"Case #"<<t<<": "<<(i-1)*y<<"\n";
	}
}
