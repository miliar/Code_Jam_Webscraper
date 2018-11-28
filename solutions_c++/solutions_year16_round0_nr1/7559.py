//By SCJ
#include<iostream>
using namespace std;
int main()
{
ios::sync_with_stdio(0);
cin.tie(0);
	int T,n;cin>>T;
	for(int ca=1;ca<=T;++ca)
	{
		cin>>n;
		if(n==0){
			cout<<"Case #"<<ca<<": INSOMNIA\n";
			continue;
		}
		bool used[10];
		for(int i=0;i<10;++i) used[i]=0;
		for(int t=0;;++t)
		{
			int x=n*t;
			while(x)
			{
				used[x%10]=1;
				x/=10;
			}
			bool f=1;
			for(int i=0;i<10;++i)
			{
				if(used[i]==0){
					f=0;break;
				}
			}
			if(f)
			{
				//if(t>50) cout<<"n="<<n<<"ttttttttttttttt="<<t<<endl;
				//if(n%10000!=0) break;
				cout<<"Case #"<<ca<<": "<<n*t<<'\n';
				break;
			}
		}
	}

}
