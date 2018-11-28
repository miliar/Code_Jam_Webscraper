#include <iostream>
using namespace std;

int main() {
	
		int i,t,smax,k,j=1;
		long count=0,sum=0;
		string s;
		cin>>t;
		while(t--)
		{
		    j=1;
			sum=0;
			count=0;
			cin>>smax;
			cin>>s;
			for(i=0;i<=smax;i++)
			{
				k=s[i]-'0';
				if(sum<i&&k!=0)
				{
					count+=(i-sum);
					sum+=(i-sum);
				}
			
					sum+=k;
			
			} 
			cout<<"case #"<<j<<": "<<count<<"\n";
			j++;
		}
}