#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>

using namespace std; 

const int INF = 1<<29;
typedef long long ll;
const ll MOD7 = 10e7;
const ll MOD9 = 10e9;

int main()
{
	// freopen("A-l.in", "r", stdin);
	// freopen("A-l.out", "w", stdout);	

	int tt;
	scanf("%d", &tt);
	for(int qq = 1; qq <= tt; qq++)
	{
		char s[1001];
		vector <int> v(1001);
		
		scanf("%s", s);
		int l = strlen(s);

		int num = s[0];
		v[0] = num;

		for(int i = 1; i < l; i++)
		{
			num = s[i];
			if(num < v[0]){
				v[i] = num;
			}
			else{
				for(int j = 1001; j >= 0; j--)v[j+1] = v[j];
				v[0] = num;
			}
		}

		printf("Case #%d: ", qq);
		for (int i = 0; i < v.size(); ++i)printf("%c", v[i]);
		printf("\n");
	}

	return 0;
}

		