#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;




int main()
{
	

	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		vector<int> cnt(26);
		string s;
		cin>>s;
		for(int j=0;j<s.size();j++)
		{
			cnt[s[j]-'A']++;
		}
		vector<int> v(10,0);
		v[0]+=cnt[25];
		cnt[4]-=v[0];
		cnt[17]-=v[0];
		cnt[14]-=v[0];
		v[2]+=cnt[22];
		cnt[19]-=v[2];
		cnt[14]-=v[2];
		v[8]+=cnt[6];
		cnt[4]-=v[8];
		cnt[8]-=v[8];
		cnt[7]-=v[8];
		cnt[19]-=v[8];	
		v[6]+=cnt[23];
		cnt[18]-=v[6];
		cnt[8]-=v[6];
		v[3]=cnt[7];
		cnt[17]-=v[3];
		v[7]=cnt[18];
		cnt[13]-=v[7];
		v[4]=cnt[17];
		cnt[5]-=v[4];
		cnt[14]-=v[4];
		v[5]=cnt[5];
		v[1]=cnt[14];
		cnt[13]-=v[1];
		v[9]=cnt[13]/2;
		
		cout<<"Case #"<<i+1<<": ";	
		for(int j=0;j<v.size();j++)
		{
			for(int k=0;k<v[j];k++)
			{
				cout<<j;
			}

		}
		cout<<endl;
	}
	return 0;
}
