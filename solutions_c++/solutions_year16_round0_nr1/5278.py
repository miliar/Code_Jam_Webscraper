#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int c = 1;
	while(c<=t)
	{
	
		long n;
		cin>>n;
		
		vector<bool> v(10,false); 
		long long i = 1;
		long long res = 0;
		long loopcnt = 0;
		bool  flag = false;
		while((loopcnt < 100) && flag == false)
		{
				
				long long t = n * i;
				while(t)
				{
						int d = t%10;
						t /= 10;
						v[d] = true;
				}
				bool f = true;
				for(int j=0;j<10;j++)
						f = (f && v[j]);
				if(f)
				{
					res = (n*i);
					flag = true;
					break;
				}
				else
					i++;
			loopcnt++;
		}
		
		if(flag)
			cout<<"Case #"<<c<<": "<<res<<endl;
		else
			cout<<"Case #"<<c<<": INSOMNIA"<<endl;
		c++;
	}
}
