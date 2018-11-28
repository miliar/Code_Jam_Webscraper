#include<iostream>
#include<vector>
using namespace std;
int min(int a ,int b)
{
	return a>b?b:a;
}
int main()
{
	int T;
	cin>>T;
	for(int j=1;j<=T;j++)
	{
		string s;
		cin>>s;
		int minNop[s.size()];
		int minNos[s.size()];
		int minNo[s.size()];
		
		if(s[0]=='+'){minNop[0]=0;minNos[0]=1;}
						
		else {minNop[0]=1;minNos[0]=0;}
		
		for(int i=1;i<s.size();i++)
		{
			if(s[i]=='+'){
			
			minNop[i]=minNop[i-1];
			minNos[i]=min(minNos[i-1]+2,minNop[i-1]+1);
			}
			else {
			minNos[i]=minNos[i-1];
			 minNop[i]=min(minNop[i-1]+2,minNos[i-1]+1);
			}
		}
		cout<<"Case #"<<j<<": "<<minNop[s.size()-1]<<endl;
	}
}
		
		
