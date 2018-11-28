/*************************************************************************
	> File Name: pB.cpp
	> Author: fuyu0425/a0919610611
	> School: National Chiao Tung University
	> Team: NCTU_Ragnorok
	> Mail: a0919610611@gmail.com
	> Created Time: 西元2016年04月09日 (週六) 14時19分23秒
 ************************************************************************/
#include <bits/stdc++.h>
using namespace std;

int main()
{

	int T;
	int kase=0;
	cin>>T;
	while(T--)
	{
		if(kase++) cout<<endl;
		cout<<"Case #"<<kase<<": ";
		string in;
		cin>>in;
		int ln=in.size();
		int ans=0;
		if(in[ln-1]=='+') ans=0;
		else ans=1;
		int now=(ans)? -1:1;
		int i;
		for(i=ln-2;i>=0;i--)
		{
			if(in[i]=='+' && now==-1) 
			{
				ans++;
				now=1;
			}else if(in[i]=='-' && now==1)
			{
				ans++;
				now=-1;
			}
		}
		cout<<ans;
	}
     return 0;
}
