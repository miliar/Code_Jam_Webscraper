/*	ashish1610	*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tcase=1;tcase<=t;++tcase)
	{
		int n;
		cin>>n;
		string str[n],temp[n];
		for(int i=0;i<n;++i)
		{
			cin>>str[i];
			temp[i]+=str[i];
		}
		bool flag=true;
		string z;
		for(int j=0;j<temp[0].length();++j)
			if(temp[0][j]!=temp[0][j+1])
				z+=temp[0][j];
		for(int i=1;i<n;++i)
		{
			string x;
			for(int j=0;j<temp[i].length();++j)
				if(temp[i][j]!=temp[i][j+1])
					x+=temp[i][j];
			if(x.length()!=z.length())
			{
				flag=false;
				break;
			}
			else
			{
				for(int j=0;j<z.length();++j)
				{
					if(z[j]!=x[j])
					{
						flag=false;
						break;
					}
				}
				if(!flag)
					break;
			}
		}
		if(!flag)
			cout<<"Case #"<<tcase<<": Fegla Won\n";
		else
		{
			int ans=0,final_ans=INT_MAX;
			int cnt[n][105];
			for(int i=0;i<n;++i)
				for(int j=0;j<105;++j)
					cnt[i][j]=0;
			for(int i=0;i<n;++i)
			{
				int k=0;
				string temp_str=str[i];
				for(int j=0;j<temp_str.length();++j)
				{
					if(str[i][j]==str[i][j+1])
						cnt[i][k]++;
					else
						cnt[i][k++]++;
				}
			}
			for(int i=0;i<n;++i)
			{
				ans=0;
				for(int j=0;j<n;++j)
				{
					for(int k=0;k<str[i].length();++k)
					{
						ans+=abs(cnt[i][k]-cnt[j][k]);
					}
				}
				final_ans=min(ans,final_ans);
			}
			int temp2=0;
			for(int i=0;i<str[0].length()-1;++i)
			{
				if(str[0][i]!=str[0][i+1])
					temp2++;
			}
			temp2++;
			ans=0;
			for(int i=0;i<n;++i)
				ans+=abs(str[i].length()-temp2);
			final_ans=min(ans,final_ans);
			cout<<"Case #"<<tcase<<": "<<final_ans<<endl;
		}
	}
	return 0;
}
