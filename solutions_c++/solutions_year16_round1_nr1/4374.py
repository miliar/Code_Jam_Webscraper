#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;char in[10000];string out="";
	scanf("%d",&t);
	int tt=t;
	t=0;
	while(t!=tt)
	{
	    t++;
		scanf("%s",in);
		out=out+in[0];
		char comp=in[0];
		for(int i=1;i<strlen(in);i++)
		{
			if(in[i]>=comp)
			{
				out=in[i]+out;
			//	cout<<"yes";
			}
			else
			{
				out=out+in[i];
			//	cout<<"no";
			}
			comp=out[0];
		}
		cout<<"Case #"<<t<<":"<<" "<<out<<endl;
		out="";
		
	}
	return 0;
}