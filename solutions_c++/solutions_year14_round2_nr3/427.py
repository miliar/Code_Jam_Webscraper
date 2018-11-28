#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<stack>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
string arr[60];
int brr[60][60];
int seq[60];
int main()
{
	long long r,T,t,i,j,k,cnt,l,m,a,g,b,n,x,f,vis;
	//fstream cin;
	map<string,int>mp;
	string str,str1;
	stack<int>st;
	vector<string>val;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1B\\C\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1B\\C\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		cin>>n>>m;
		mp.clear();
		val.clear();
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			mp[arr[i]]=i+1;
			val.push_back(arr[i]);
		}
		sort(val.begin(),val.end());
		for(i=0;i<=n;i++)
		for(j=0;j<=n;j++)brr[i][j]=0;
		for(i=0;i<m;i++)
		{
			cin>>j>>l;
			brr[j][l]=1;
			brr[l][j]=1;
		}
		str="";
		do
		{
			str1="";
			for(i=0;i<n;i++)
			{
				seq[i]=mp[val[i]];
				str1+=val[i];
			}
			if(str=="")
			{
				vis=1;
				while(st.empty()!=true)st.pop();
				st.push(seq[0]);
				while(vis<n)
				{
					while(st.empty()!=true&&brr[st.top()][seq[vis]]==0)st.pop();
					if(st.empty()==true)break;
					st.push(seq[vis]);
					vis++;
				}
				
				if(vis>=n)
				{
					if(str=="")str=str1;
					else if(str1<str)str=str1;
				}
			}
			else if(str1<str){
				vis=1;
				while(st.empty()!=true)st.pop();
				st.push(seq[0]);
				while(vis<n)
				{
					while(st.empty()!=true&&brr[st.top()][seq[vis]]==0)st.pop();
					if(st.empty()==true)break;
					st.push(seq[vis]);
					vis++;
				}
				
				if(vis>=n)
				{
					if(str=="")str=str1;
					else if(str1<str)str=str1;
				}
			}
		}
		while(next_permutation(val.begin(),val.end()));
		cout<<str<<endl;
	}
	return 0;
}