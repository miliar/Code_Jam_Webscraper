#include<iostream>
#include<cstring>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string str;
    ifstream in("input.txt");
    ofstream out("output.txt");
	long long int n=0,i,sum=0,ttl=0;
	int t=0,j=1;
	in>>t;
	while(t--)
	{
		sum=0;
		in>>n;
		in>>str;
		ttl=0;
		for(i=0;i<n+1;i++)
		if(sum>=i)
			sum=sum+(int)str[i]-48;
        else
			{
				ttl=ttl+i-sum;
				sum=sum+(int)str[i]-48+i-sum;
            }
		out<<"Case #"<<j<<": "<<ttl<<endl;
		j++;
    }
    in.close();
    out.close();
	return 0;
}
