#include <bits/stdc++.h>
using namespace std;


int main(int argc, char const *argv[])
{
	
	//freopen("input1.txt","r",stdin);
	//freopen("output1.txt","w",stdout);
	int t,ntc=0;
	cin >> t;
	while(t--)
	{
		ntc++;
		string s;
		cin >> s;
		int l = s.length();
		string str = "";
		str +=s[0];
		char start;
		start= s[0];
		for(int i=1;i<l;i++)
		{
			if(s[i]>=start) {str = s[i] + str;  start = s[i];}
			else
			{ str = str + s[i]; }
		}
		//cout << str << endl;
        printf("Case #%d: %s\n",ntc,str.c_str());
	}
	return 0;
}
