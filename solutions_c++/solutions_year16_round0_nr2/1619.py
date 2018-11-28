#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Output2-2.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		string S;
		cin>>S;
		int L=S.length();
		int Step = 0, k = 0;
		for(;;)
		{
			k=0;
			while(S[k]==S[0] && k<L) k++;
			if(S[0]=='+' && k==L)  break;
			reverse(&S[0],&S[k-1]);
			for(int j=0; j<k; j++) S[j]='+'+'-'-S[j];
			Step++;
		}
		cout<<"Case #"<<i<<": "<<Step<<endl;
	}
	return 0;
}
