#include <iostream>
#include <fstream>
using namespace std;

int solve(int shyindex, string str)
{
	int a[shyindex+1],i;
	
	for(i=0;i<shyindex+1;i++)
		a[i]=str[i]-'0';
		
	
	int stdpersons=0,res,extra;
	res=a[0];

	for(i=0;i<shyindex+1;i++)
	{
		extra = i-stdpersons;
		if(extra>0)
		{
			a[0]+=extra;
			stdpersons+=extra;
		}
		stdpersons+=a[i];	
	}
	int ans=a[0]-res;
	return ans;
	
}

int main () 
{
	ios::sync_with_stdio(false);
	int testcases,shyindex;
	cin>>testcases;
	string str;
	int i=0;
	while(testcases--)
	{
		i++;
		cin>>shyindex>>str;
		cout<<"Case #"<<i<<": "<<solve(shyindex,str)<<endl;
	}
	return 0;
	
}
