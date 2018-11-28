#include<bits/stdc++.h>

using namespace std;


const int Maxn=1e3+10;

int num[Maxn];
string s;

ofstream fout("out.txt");
ifstream fin("A-large.in");
int main()
{
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		fin>>n>>s;
		n++;
		int cnt=0,q=0;
		memset(num,0,sizeof num);
		for(int j=0;j<n;j++)
			num[j]=s[j]-'0';
		q=num[0];
		for(int j=1;j<n;j++)
			if(q<j&&num[j])
			{
				cnt+=j-q;
				q=j+num[j];
			}
			else 
				q+=num[j];
	
		fout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}


}
