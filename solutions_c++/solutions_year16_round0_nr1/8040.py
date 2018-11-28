#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.rtf","w",stdout);
	int n;
	cin>>n;
	unsigned long long x;
	for(int i=0;i<n;i++)
	{
		cin>>x;
		vector<int> v(10);
		unsigned long long r=x;
		for(int j=1;j<=10000000;j++)
		{
			r=x*j;
			//cout<<r<<" ";
			unsigned long long h=r;
			while(h)
			{
				v[h%10]=1;
				h/=10;
			}
			bool f=0;
			for(int k=0;k<10;k++)
				if(v[k]==0) f=1;
				
			if(f==0) {
			cout<<"Case #"<<i+1<<": "<<r;
			if(i+1!=n)
			cout<<'\n';
			break;}
			
			if(f==1 && j==10000000){
			cout<<"Case #"<<i+1<<": INSOMNIA";
			if(i+1!=n)
			cout<<'\n';}
		}
	}
	return 0;
}
