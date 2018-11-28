#include<bits/stdc++.h>
using namespace std;
long long int t,n,i,count[10],k=1;
void cal(long long int a, long long int count[])
{long long int b;
	while(a!=0)
	{
		b=a%10;
		count[b]++;
		a=a/10;
		
	}
}
bool check(long long int count[])
{int d;
	for(d=0;d<=9;d++)
	{
	if(count[d]<1)
	{
	return false;	
	}
	}
	return true;
}
int main()
{ios_base::sync_with_stdio(false); 
cin.tie(0);
	long long int t,n,i,count[10],k=1,ans,j;
	ifstream infile;
	ofstream outfile;
	infile.open("input.txt",ios::in);
	outfile.open("output.txt",ios::out);
	infile>>t;
	for(i=1;i<=t;i++)
	{ k=1;ans=1;
		infile>>n;
		if(n==0)
		{
			outfile<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
	for(j=0;j<=9;j++)
	{
		count[j]=0;
	}
	while(true)
		{
		ans=(k++)*n;
		cal(ans,count);
		if(check(count))
		{
			break;
		}
		}
	outfile<<"Case #"<<i<<": "<<ans<<endl;
	}
	infile.close();
   outfile.close();
return 0;
}
