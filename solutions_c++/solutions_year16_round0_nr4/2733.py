/*************************************************************************
	> File Name: pD.cpp
	> Author: fuyu0425/a0919610611
	> School: National Chiao Tung University
	> Team: NCTU_Ragnorok
	> Mail: a0919610611@gmail.com
	> Created Time: 西元2016年04月10日 (週日) 02時24分48秒
 ************************************************************************/
#include <bits/stdc++.h>
using namespace std;

int main()
{

	int T;
	cin>>T;
	int kase=0;
	while(T--)
	{	
		if(kase++) cout<<endl;
		cout<<"Case #"<<kase<<": ";
		long long k,c,s;
		cin>>k>>c>>s;
		vector<long long >ans;
		long long i,j;
		for(i=1;i<=k;i++)
		{
			long long  now=i;
			for(j=2;j<=c;j++)
			{
				now=k*(now-1)+i;
			}
			ans.push_back(now);

		}
		int space=0;
		for(i=0;i<ans.size();i++)
		{
			if(space++)cout<<" ";
			cout<<ans[i];
		}
	}
    return 0;
}
