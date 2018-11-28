#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<set>
#include<cstdio>
using namespace std;
//pandey
int main()
{
	//ios_base::sync_with_stdio(false);
	freopen("A-large.txt","r",stdin);
	freopen("A-large-out.txt","w",stdout);
	
	int t;
	cin>>t;
	
	for(int i=1;i<=t;i++)
	{
		int len;
		cin>>len;
		string s;
		cin>>s;

		int a[len+1];
		for(int j=0;j<=len;j++)
		{
			a[j]=(int)(s[j]-'0');
		}

		int totalyet=0,addfriend=0;
		for(int j=0;j<=len;j++)
		{
			if(j>totalyet)
			{
				//cout<<totalyet<<"  "<<j<<endl;
				addfriend++;
				totalyet++;
			}
			totalyet=totalyet+a[j];
		}
		cout<<"Case #"<<i<<": "<<addfriend<<endl;

	}

	
	
	

}


