#include <bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename __Tp1>
void __f(const char* name, __Tp1&& __tp1){
    cerr << name << " : " << __tp1 << std::endl;
}
template <typename __Tp1, typename... __Tps>
void __f(const char* names, __Tp1&& __tp1, __Tps&&... __tps){
    const char* comma = strchr(names + 1, ',');
	cerr.write(names, comma - names) << " : " <<  __tp1 << " | " ;
	__f(comma+1, __tps...);
}
#else
#define trace(...)
#endif

bool is(string& s, char c)
{
	for (auto &ss: s)
		if (ss != c)
			return false;
	return true;
}

void change(string& s, int lim, char c)
{
	for (int i = 0; i <= lim; i++)
		s[i] = c;
}

int main()
{
	int __T;
	scanf("%d", &__T);
	for (int t = 1; t <= __T; t++)
	{
		printf("Case #%d: ", t);
		string s;
		cin >> s;
		if (is(s, '-'))
			printf("1");
		else
		{
			bool found = false;
			int ans = 0;
			while (not found)
			{
				int i = 1;
				for (; i < (int) s.size(); i++)
					if (s[i] != s[i - 1])
						break;
				if (i == (int) s.size())
				{
					if (s[0] == '-')
						ans++;
					found = true;
					break;
				}
				else
					change(s, i - 1, s[i]);
				ans++;
			}
			printf("%d", ans);
		}
		printf("\n");
	}
	return 0;
}
