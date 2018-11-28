#include <iostream>
using namespace std;

int main() {
	int test,cas;
	cin>>test;
	for(cas=1;cas<=test;cas++)
	{
		long long required=0,i;
		int max;
		cin>>max;
		string s;
		cin>>s;
		long long tot_required=0;
		long long a[max+1];
		long long j=1;
		for(i=0;i<=max;i++)
		{
			a[i]=s[i]-48;
		//	cout<<"a["<<i<<"]"<<" "<<a[i]<<endl;
		}
		long long uptil_now=0;
		
		if(max>0)
		{
			for(i=0;i<max;i++)
			{
				if(((a[i]+uptil_now)>=(i+1))&&(a[i+1]!=0))
				{
					uptil_now+=a[i];
				//	cout<<"uptil_ now "<<i<<" u "<<tot_required<<endl;
				}
				else if(a[i+1]!=0)
				{
					required=i+1-uptil_now;
					tot_required+=required;
					uptil_now=uptil_now+required;
				//	cout<<"uptil_ now r "<<i<<" u "<<tot_required<<endl;
				}
				else
				{
					uptil_now+=a[i];
				}
			}
			cout<<"Case #"<<cas<<": "<<tot_required<<endl;
		}
		else
		{
			cout<<"Case #"<<cas<<" 0"<<endl;
		}
		//j+=1;
		
	}
	return 0;
}