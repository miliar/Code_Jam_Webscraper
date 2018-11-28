#include<bits/stdc++.h>
using namespace std;
#define LL long long
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int count = 1;
	while(T--)
	{
		cout<<"Case #"<<count++<<": ";
		LL N;
		cin>>N;
		if(N == 0)
			cout<<"INSOMNIA\n";
		else
		{
			LL val = N,a;
			LL iter = 1;
			vector<bool> V(10,false);
			while(true)
			{
				a = val;
				while(a)
				{
					V[a%10] = true;
					a /= 10;
				}
				bool flag = true;
				for(int i=0;i<10 && flag;i++)
					if(!V[i])
						flag = false;
				if(flag)
					break;
				else
				{
					iter++;
					val = N * iter;
				}
			}
			cout<<val<<endl;
		}
	}
	
	return 0;
}
