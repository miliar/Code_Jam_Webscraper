#include<fstream>
#include<string>
#include<cmath>
#include<cstring>
using namespace std;
ifstream cin("xx.in");
ofstream cout("xx.out");
int T,counter=0,L,ans;
string S;
int main()
{
	cin>>T;int i,temp;
	while(T--)
	{
		counter++;ans=0;temp=0;
		cin>>L;cin>>S;
		cout<<"Case #"<<counter<<": ";
		for(i=0;i<=L;i++)
		{
			if(temp>=i)
			{
				temp+=int(S[i]-48);
				continue;
			}
			else
			{
				ans+=(i-temp);
				temp+=(i-temp);
				temp+=int(S[i]-48);
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
