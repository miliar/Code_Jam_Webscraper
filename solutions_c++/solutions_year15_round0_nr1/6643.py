#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	int t,z,smax,i,ns,rs;
	string str;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for(z=1;z<=t;z++)
	{
		cin >> smax;
		cin >> str;
		ns=rs=0;
		for(i=0;i<=smax;i++)
		{
			if(str[i]=='0')
			continue;
			if(ns>=i)
			{
				ns+=str[i]-'0';
			}
			else
			{
				rs+=i-ns;
				ns+=rs+str[i]-'0';
			}
		}
		cout << "Case #" << z << ": " << rs << endl;
	}
	return 0;
}

