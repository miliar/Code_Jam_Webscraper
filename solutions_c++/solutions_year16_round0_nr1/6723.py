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

void f(unordered_set<int>& u_set, int val)
{
	while (val)
	{
		u_set.insert(val % 10);
		val /= 10;
	}
}

int main()
{
	int __T;
	scanf("%d", &__T);
	for (int t = 1; t <= __T; t++)
	{
		printf("Case #%d: ", t);
		int val;
		scanf("%d", &val);
		if (val == 0)
			printf("INSOMNIA");
		else
		{
			unordered_set<int> u_set;
			int i = 1;
			while (u_set.size() < 10)
			{
				f(u_set, val * i);
				if (u_set.size() == 10)
					break;
				i++;
			}
			printf("%d", val * i);
		}
		printf("\n");
	}
	return 0;
}
