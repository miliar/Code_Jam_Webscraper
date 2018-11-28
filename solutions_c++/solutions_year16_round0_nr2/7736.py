#include <bits/stdc++.h>
using namespace std;
#define gc() getchar_unlocked()
inline long long int read_int()
{
	char c = gc();
    	while(c<'0' || c>'9')
    	c = gc();
    	long long int ret = 0;
    	while(c>='0' && c<='9')
    	{
    		ret = (ret<<3) + (ret<<1) + c - 48;
    		c = gc();
    	}
    	return ret;
}
int main()
{
	int t;
	t = read_int();
	int j=1;
	while(t--)
	{
		string s;
		cin >> s;
		int count = 0;
		int length = s.size();
		for(int i=length-1;i>=0;i--)
		{
			if(((s[i]=='+') && (count&1)) || ((s[i]=='-') && (count%2==0)))
			{
				count++;
			}
		}
		cout << "Case #" << j << ": " << count << endl;
		j++;
	}
	return 0;
}
