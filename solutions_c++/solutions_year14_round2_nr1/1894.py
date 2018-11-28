#include<iostream>
using namespace std;
//---------------------------------

int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("code1.txt","w",stdout);
	//cout<<"kit";
	int t;
	cin>>t;
	//cout<<t<<endl;
	for(int test=1;test<=t;test++)
	{
		int n;
		cin>>n;
		//cout<<n
		string str[n+1];
		
		for(int i=0;i<n;i++)
			cin>>str[i];
			
		int count=0;
		int i=0;
		int j=0;
		int l=str[0].size();
		int m=str[1].size();
		while(i<l || j<m)
		{
			if(str[0][i]==str[1][j])
			{
				i++;
				j++;
			}
			else if(i-1>=0 && str[0][i]==str[0][i-1])
			{
				count++;
				i++;
			}
			else if(j-1>=0 && str[1][j]==str[1][j-1])
			{
				count++;
				j++;
			}
			else
			{
				count=-1;
				break;
			}
		}
		cout<<"Case #"<<test<<": ";
		if(count==-1)
			cout<<"Fegla Won\n";
		else
			cout<<count<<endl;
	}
}
