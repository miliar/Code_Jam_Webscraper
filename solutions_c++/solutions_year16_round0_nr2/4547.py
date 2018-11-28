#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
int main()
{
	ifstream cin("Q2L.in");
	ofstream cout("Q2LA.txt");
	string str;
	int i,j,k,l,t,ind=1;
	LL a,b,c,d,m,n;
	cin>>t;
	while(t--)
	{
		cin>>str;
		l=str.length();
		n=0;
		for(i=l-2;i>=0;i--)
		{
			if(str[i]!=str[i+1])
			n++;
			
		}
		n=n+(str[l-1]=='-');
		cout<<"Case #"<<ind++<<": "<<n<<endl;
	}
	
}
