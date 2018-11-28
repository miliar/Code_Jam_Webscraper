#include<iostream>
#include<string.h>
#include<fstream>
#include<map>
using namespace std;
int main()
{
	int t,iter=1;
	ifstream read("input.txt");
	ofstream output("output.txt");
	read>>t;
	//cin>>t;
	while(t--)
	{
		int arr[10]={0};
		long long int n;
		//cin>>n;
		read>>n;
		long long int m=n,l;
		int c=0;
		int x=1;
		long long int k=1;
		while(x)
		{
			l=m;
			while(m>0)
			{
				int d=m%10;
				if(arr[d]==0)
				{
					c++;
					arr[d]=1;
				}
				m=m/10;
			}
		
			if(c==10)
			{
				output<<"Case #"<<iter<<": "<<l<<"\n";
				//cout<<"Case #"<<iter<<": "<<l<<"\n";
				break;
			}
			k++;
			m=k*n;
			if(l==m)
			{
				output<<"Case #"<<iter<<": INSOMNIA\n";
				//cout<<"Case #"<<iter<<": INSOMNIA\n";
				break;
			}
		}
		iter++;
		
	}
	
	return 0;
}
