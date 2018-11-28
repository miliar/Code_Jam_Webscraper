#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

template<class T>
class array
{
public:
	T f[300];
	T& operator[] (int x)
	{
		return f[x + 150];
	}
};

array<array<int> > table;

int alphaset[] = {'1', 'i', 'k', 'j'};
char s[100000];

char circ[100000000];

int preSum[100000000];

int main()
{
	table['1']['1'] = '1';
	table['1']['i'] = 'i';
	table['1']['j'] = 'j';
	table['1']['k'] = 'k';
	table['i']['1'] = 'i';
	table['i']['i'] = -int('1');
	table['i']['j'] = 'k';
	table['i']['k'] = -int('j');
	table['j']['1'] = 'j';
	table['j']['i'] = -int('k');
	table['j']['j'] = -int('1');
	table['j']['k'] = 'i';
	table['k']['1'] = 'k';
	table['k']['i'] = 'j';
	table['k']['j'] = -int('i');
	table['k']['k'] = -int('1');
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
		{
			table[-alphaset[i]][alphaset[j]] = table[alphaset[i]][-alphaset[j]] = -table[alphaset[i]][alphaset[j]];
			table[-alphaset[i]][-alphaset[j]] = table[alphaset[i]][alphaset[j]];
		}
	
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: ", cas);
		int l, x;
		scanf("%d%d", &l, &x);
		scanf("%s", s);
		int cur = '1', oneCirc;
		for(int i = 0; i < l; ++i)
			cur = table[cur][s[i]];
		oneCirc = cur;
		cur = '1';
		int circle = 0;
		do
		{
			cur = table[cur][oneCirc];
			circle++;
		}while(cur != '1');
		circle = x;
		for(int i = 0; i < circle; ++i)
		{
			for(int j = 0; j < l; ++j)
				circ[i * l + j] = s[j];
		}
		preSum[0] = circ[0];
		for(int i = 1; i < circle * l; ++i)
			preSum[i] = table[preSum[i - 1]][circ[i]];
		bool succ = false;
		for(int i = 0; i < circle * l && !succ; ++i)
			for(int j = i + 1; j < circle * l && !succ; ++j)
			{
				int a = preSum[i];
				int b = table[-preSum[i]][preSum[j]];
				int c = table[-preSum[j]][preSum[circle * l - 1]];
				if(abs(a) == 'i' && abs(b) == 'j' && abs(c) == 'k')
				{
					if(a * b * c > 0)
						succ = true;
				}
			}
		if(succ) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
