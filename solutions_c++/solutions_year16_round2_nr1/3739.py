#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define ll long long
vector <string >v;
vector <int> v1;
int main()
{
	int t;
//	ios_base::sync_with_stdio(false);
//	freopen("A-small-attempt (2).in","r",stdin);//redirects standard input
//    freopen("output120.out","w",stdout);
	
	cin>>t;
	v.pb("ZERO");
	v.pb("ONE");
	v.pb("TWO");
	v.pb("THREE");
	v.pb("FOUR");
	v.pb("FIVE");
	v.pb("SIX");
	v.pb("SEVEN");
	v.pb("EIGHT");
	v.pb("NINE");

	int p=1;
	while(t--)
	{
		string s;
		cin>>s;
		int j=0;
		int arr[26],ans[15];
		for(int i=0;i<26;i++)arr[i]=0;
		while(s[j]!='\0')
		{
			arr[s[j]-'A']++;
			j++;
		}
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		int x=ans[0]=arr['Z'-'A'];
		for(int i=0;i<v[0].size();i++)
		arr[v[0][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		int y=ans[2]=arr['W'-'A'];
		for(int i=0;i<v[2].size();i++)
		arr[v[2][i]-'A']-=y;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[4]=arr['U'-'A'];
		for(int i=0;i<v[4].size();i++)
		arr[v[4][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[8]=arr['G'-'A'];
		for(int i=0;i<v[8].size();i++)
		arr[v[8][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[6]=arr['X'-'A'];
		for(int i=0;i<v[6].size();i++)
		arr[v[6][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[5]=arr['F'-'A'];
		for(int i=0;i<v[5].size();i++)
		arr[v[5][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[7]=arr['V'-'A'];
		for(int i=0;i<v[7].size();i++)
		arr[v[7][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[9]=arr['I'-'A'];
		for(int i=0;i<v[9].size();i++)
		arr[v[9][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[1]=arr['O'-'A'];
		for(int i=0;i<v[1].size();i++)
		arr[v[1][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
		x=ans[3]=arr['T'-'A'];
		for(int i=0;i<v[3].size();i++)
		arr[v[3][i]-'A']-=x;
//		for(int i=0;i<26;i++)cout<<arr[i]<<" ";
//		cout<<"\n";
//		
//		cout<<"@";
	cout<<"Case #"<<p<<": ";
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<ans[i];j++)
			{
				cout<<i;
			}
		}
		cout<<"\n";
		p++;
		
	}
}
