#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int c=1,t,n;
	string temp1,temp2,str;
	cin>>t;
	while(t--)
	{
		cin>>str;
		n=str.size();
		temp1="";temp2="";

		temp1+=str[0];
		for (int i = 1; i < n; ++i)
		{
			if(str[i]<temp1[0])
				temp1+=str[i];
			else
			{
				temp2="";
				temp2+=str[i];
				temp2+=temp1;
				temp1=temp2;
			}			
		}
		cout<<"Case #"<<c++<<": "<<temp1<<endl;
	}
	return 0;
}