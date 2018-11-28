#include <cstdio>
#include <algorithm>

class Vector2i
{
public:
	int x;
	int y;
};

Vector2i mushrooms()
{
	Vector2i out{0,0};
	int n, tab[1001], max=0;
	scanf("%d", &n);

	for(int i = 0; i < n; i++)
		scanf("%d", &tab[i]);

	for(int i = 1; i < n; i++)
	{
		if(tab[i-1]-tab[i] > 0)
		{
			out.x+=tab[i-1]-tab[i];
			max=std::max(tab[i-1]-tab[i], max);
		}
	}

	for(int i = 0; i < n-1; i++)
		out.y+=std::min(max, tab[i]);
	
	return out;
}

int main()
{
	Vector2i out;
	int T;
	scanf("%d", &T);

	for(int i = 1; i <= T; i++)
	{
		out=mushrooms();
		printf("Case #%d: %d %d\n", i, out.x, out.y);
	}
}