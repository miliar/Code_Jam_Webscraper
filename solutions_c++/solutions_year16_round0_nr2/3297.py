#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");

    int t;
    // scanf("%d",&t);
    fin>>t;
    for(int i=1;i<=t;i++)
    {
    	int res=0;
    	string s;
    	// cin>>s;
    	fin>>s;
    	if(s[0]=='-')
    	{
    		int idx=0;
    		while(s[idx]=='-')
    		{
    			s[idx]='+';
    			idx++;
    		}
    		res++;
    	}
    	for(int j=0;j<s.size();j++)
		{
			if(s[j]=='+') continue;
			else
			{
				int idx=j;
				while(s[idx]=='-')
				{
					s[idx]='+';
					idx++;
				}
				res+=2;
				j=idx;
			}
		}
    	// printf("Case #%d: %d\n",i,res);
    	fout<<"Case #"<<i<<": "<<res<<endl;
    }
}

