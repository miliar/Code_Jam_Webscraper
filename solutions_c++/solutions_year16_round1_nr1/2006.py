#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#define ll long long
using namespace std;

int main()
{
	//freopen("R11LL.in", "r", stdin);
	//freopen("R11LL.out", "w", stdout);
	ll T,it,i;
	string str,btr;
	scanf("%lld", &T);
	for(it = 1; it <= T; it++)
	{
		str.clear();
		btr.clear();
		cin >> str;
		for(i = 0; i < str.size(); i++)
		{
			if(str[i] >= btr[0])
				btr.insert (0, 1, str[i]);
			else btr.push_back(str[i]);
		}
		printf("Case #%lld: ", it);
		for(i = 0; i < btr.size(); i++)
			cout << btr[i];
		putchar('\n');
	}
	return 0;
}
