#include<iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t,i,k,j;
	cin>>t;int count[t];
	for(k=0;k<t;k++)
	{	count[k]=0;
	char a[100]; int extra[100];
	cin>>a;
	for( i=0;a[i]!='\0';i++)
	{
		if(a[i]=='-')
		extra[i]=0;
		else
		extra[i]=1;
	}j=i;
	for(i=0;i<j-1;i++)
	{
		if(extra[i]!=extra[i+1])
		{
			count[k]++;
		}
	}
	if(extra[j-1]==0)
	count[k]++;
}	for(k=0;k<t;k++)
	{
		cout<<"Case #"<<k+1<<": "<<count[k]<<"\n";
	}

}
