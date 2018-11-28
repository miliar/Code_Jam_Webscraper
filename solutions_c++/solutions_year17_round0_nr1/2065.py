#include<bits/stdc++.h>
using namespace std;
//nksheokand
int arr[1001];
int main()
{
	fstream in,out;
	in.open("A-large.in");
	out.open("Output.txt");
	int t,k,s,done,r;
	bool flag;
	string S;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>S>>k;
		s=S.size();
		for(int i=0;i<s;i++)
		arr[i]=0;
		done=r=0;
		for(int i=0;i<=s-k;i++)
		{
			done-=arr[i];
			if(done%2 && S[i]=='+')
			{
				done++;
				r++;
				arr[i+k]++;
			}
			else if(done%2==0 && S[i]=='-')
			{
				done++;
				r++;
				arr[i+k]++;
			}
		}
		flag=true;
		for(int i=s-k+1;i<s;i++)
		{
			done-=arr[i];
			if(done%2 && S[i]=='+')
			{
				flag=false;
				break;
			}
			else if(done%2==0 && S[i]=='-')
			{
				flag=false;
				break;
			}
		}
		if(!flag)
		out<<"Case #"<<l<<": IMPOSSIBLE"<<endl;
		else
		out<<"Case #"<<l<<": "<<r<<endl;
	}
	in.close();
	out.close();
	return 0;
}
