#include <iostream>
#include <algorithm>
using namespace std;

void fact(int x){
    int sum=1;
    while(x--){
        int sum=sum*x;
    }
}
int main()
{
	int t=1;
	int N;cin>>N;
	string hashing[10]={"ZERO","EIGHT","THREE","TWO","SIX","SEVEN","FOUR","FIVE","NINE","ONE",};
	for(;t<=N;t++)
	{
		string x;
		cin>>x;
		int cnt[26]={0};
		for(int i=0;i<x.length();i++)
			cnt[x[i]-'A']++;
		int ans[10]={0};
		int c[26]={0};
		for(int i=0;i<10;)
		{
			for(int k=0;k<26;k++)
				c[k]=cnt[k];
			string w=hashing[i];
			int j;
			for(j=0;j<w.length();j++)
			{
				if(c[w[j]-'A']==0)break;
				else
					c[w[j]-'A']--;
			}
			if(j!=w.length())
			{
				i++;

			}
			else
			{
				for(j=0;j<w.length();j++)
				{
					cnt[w[j]-'A']--;
				}
				if(hashing[i]=="ZERO")
					ans[0]++;
				else if(hashing[i]=="ONE")
					ans[1]++;
				else if(hashing[i]=="TWO")
					ans[2]++;
				else if(hashing[i]=="THREE")
					ans[3]++;
				else if(hashing[i]=="FOUR")
					ans[4]++;
				else if(hashing[i]=="FIVE")
					ans[5]++;
				else if(hashing[i]=="SIX")
					ans[6]++;
				else if(hashing[i]=="SEVEN")
					ans[7]++;
				else if(hashing[i]=="EIGHT")
					ans[8]++;
				else if(hashing[i]=="NINE")
					ans[9]++;

			}
		}
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<10;i++)
		{
			while(ans[i]--)
				cout<<i;
		}
		cout<<endl;
	}

}
