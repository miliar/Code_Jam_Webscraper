#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
	long long r,T,t,i,j,k,cnt,l,m,a,g,b,n;
	unsigned long long x,y;
	//fstream cin;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1A\\A\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1A\\A\\Small Output.txt","w",stdout);
	cin>>t;
		vector<int>st;
	for(k=1;k<=t;k++)
	{
		cin>>n>>l;
		m=l+1;
		vector<string>arr(n);
		vector<string>brr(n);
		vector<string>crr(n);
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
		}
		for(i=0;i<n;i++)cin>>brr[i];
		sort(brr.begin(),brr.end());
		for(i=0;i<n;i++)
		{
			st.clear();
			for(j=0;j<l;j++)
			{
				if(arr[i][j]!=brr[0][j])st.push_back(j);
				
			}
			crr=arr;
			for(j=0;j<n;j++)
			{
				for(a=0,b=0;a<l&&b<st.size();a++)
				{
					if(st[b]==a)
					{
						if(crr[j][a]=='1')crr[j][a]='0';
						else crr[j][a]='1';
						
						
						
						
						b++;
					}
				}
			}
			sort(crr.begin(),crr.end());
			if(crr==brr)
			{
				if(m>st.size())m=st.size();
			}
			
		}
		cout<<"Case #"<<k<<": ";
		if(m==l+1)cout<<"NOT POSSIBLE"<<endl;
		else cout<<m<<endl;
	}
	return 0;
}