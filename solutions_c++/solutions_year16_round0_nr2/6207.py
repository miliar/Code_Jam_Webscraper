#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

void flip(int s, int len, string &str)
{
	string tmp = str.substr(s, len);
	for(int i=0; i<tmp.length(); i++)
	{
		if(tmp[i]=='-')
			tmp[i] = '+';
		else
			tmp[i] = '-';
	}
	reverse(tmp.begin(), tmp.end());
	str.replace(s, len, tmp);
}

int main()
{
	//string str;
	//cin >> str;
	//cout << str << endl;
	//flip(1, 2, str);
	//cout << str << endl;
	
	int cas;
	scanf("%d", &cas);
	for(int z=1; z<=cas; z++)
	{
		string str;
		cin >> str;
		int len = str.length();
		int r = len-1, l=0;
		long long cnt = 0;
		while(r>0)
		{
			if(str[r]=='+')
				r--;
			else
			{
				/* flip first segment */
				l = 0;
				while(str[l]=='+') l++;
				if(l!=0)
				{
					for(int i=0; i<l; i++)
						str[i] = '-';
					cnt++;
				}

				/* flip rest segment */
				flip(0, r+1, str);
				cnt++;
			}
		}
		if(str[0]=='-')
			cnt++;
		printf("Case #%d: ", z);
		printf("%lld\n", cnt);
	}
	return 0;
}
