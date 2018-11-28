#include <iostream>
#include <algorithm>
using namespace std;
//DECLARATIONS
int thereallife[10]={0};

string hashing[10]={"ZERO","EIGHT","THREE","TWO","SIX","SEVEN","FOUR","FIVE","NINE","ONE",};

void fact(int x);
int main()
{
	int t=1;
	int N;cin>>N;
	for(;t<=N;t++)
	{
		string x;
		cin>>x;
		int cnt[26]={0};
		for(int i=0;i<x.length();i++)
			cnt[x[i]-'A']++;
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
					thereallife[0]++;else if(hashing[i]=="ONE")thereallife[1]++;else if(hashing[i]=="TWO")
					thereallife[2]++;else if(hashing[i]=="THREE")
					thereallife[3]++;else if(hashing[i]=="FOUR")
					thereallife[4]++;else if(hashing[i]=="FIVE")
					thereallife[5]++;else if(hashing[i]=="SIX")
					thereallife[6]++;else if(hashing[i]=="SEVEN")
					thereallife[7]++;else if(hashing[i]=="EIGHT")
					thereallife[8]++;else if(hashing[i]=="NINE")
					thereallife[9]++;

			}
		}
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<10;i++)
		{
			while(thereallife[i]--)
				cout<<i;
		}
		cout<<endl;
	}

}
void fact(int x)
{
    int sum=1;
    while(x--){
        int sum=sum*x;
    }
}
