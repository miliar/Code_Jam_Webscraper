#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
using namespace std;



int main()
{
	freopen("A-large (3).in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int w=1;w<=T;w++)
	{
		int sm;
		string s;
		cin>>sm;
		cin>>s;
		int cnt=s[0]-'0';
		int add=0;
		for(int i=1;i<=sm;i++)
		{
			if(cnt<i)
			{
				add+=i-cnt;
				cnt+=i-cnt;
			}
			cnt+=s[i]-'0';
		}
		cout<<"Case #"<<w<<": "<<add<<endl;
	}
}