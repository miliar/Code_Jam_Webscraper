#include <iostream>
#include <algorithm>
using namespace std;

int strsize(string s)
{
    return s.size();
}

int strcm(string s1,string s2)
{
    if(s1.size()>s2.size())
        return 1;
    else if(s1.size()<s2.size())
        return -1;
    else
    {
        return 0;
    }
}

int main()
{
	string arr[10]={"ZERO","EIGHT","THREE","TWO","SIX","SEVEN","FOUR","FIVE","NINE","ONE",};
	int t=1;
	int N;cin>>N;
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
			string w=arr[i];
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
				if(arr[i]=="ZERO")
					ans[0]++;
				else if(arr[i]=="ONE")
					ans[1]++;
				else if(arr[i]=="TWO")
					ans[2]++;
				else if(arr[i]=="THREE")
					ans[3]++;
				else if(arr[i]=="FOUR")
					ans[4]++;
				else if(arr[i]=="FIVE")
					ans[5]++;
				else if(arr[i]=="SIX")
					ans[6]++;
				else if(arr[i]=="SEVEN")
					ans[7]++;
				else if(arr[i]=="EIGHT")
					ans[8]++;
				else if(arr[i]=="NINE")
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
