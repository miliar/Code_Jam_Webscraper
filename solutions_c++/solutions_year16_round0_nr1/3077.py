#include<bits/stdc++.h>
using namespace std;
#define ll long long int
char n[1000010];
bool mark[10];
string ans,temp;
int main()
{	
	ll t,i,j,l,l1,r,d,c,k;
	cin>>t;
	while(t--)
	{
		cin>>n;
		memset(mark,0,sizeof(mark));
		l=strlen(n);
		for(i=0;i<l;++i)
			mark[n[i]-48]=1;
		for(i=2;;++i)
		{
			c=0;
			temp="";
			//cout<<temp<<" "<<n<<endl;
			//cout<<"ola\n";
			for(j=0,k=l-1;k>=0;--k,++j)
			{
				d=i*(n[k]-48)+c;
				r=d%10;
				c=d/10;
				char t1=r+48;
				temp=temp+t1;
				//cout<<temp[j]<<endl;
			}
			if(c>0)
			{
				char t2=c+48;
				temp=temp+t2;
			}
			l1=temp.length();
			for(j=0,k=l1-1;j<=k;++j,--k)
				swap(temp[j],temp[k]);
			cout<<temp<<endl;
			for(j=0;j<l1;++j)
				mark[((char)(temp.at(j)))-48]=1;
			//cout<<endl;
			bool f=0;
			for(j=0;j<10;++j)
			{
				//cout<<mark[j]<<" ";
				if(mark[j]==0)
				{
					f=1;
					break;
				}
			}
			//cout<<endl;
			if(!f)
				break;
		}
		cout<<temp<<endl;
	}
	return 0;
}