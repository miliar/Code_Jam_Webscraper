#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;

#define M 105
#define inf 0x3fffffff

//记得初始化equ, var, a[M][M]
int equ, var, fn, rk, ans;
int a[M][M], f[M], x[M];
bool has[M]; 	//自由变元标志

void ini () { memset (a, 0, sizeof(a)); }

void dfs (int k)
{
	if (k == fn)
	{
		int i, j, vx = var - 1, sum = 0;
		for (i = rk-1; i >= 0; i--)
		{
			while (vx >= 0 && has[vx]) sum += x[vx--];
			if (vx >= 0)
			{
				x[vx] = a[i][var];
				for (j = vx+1; j < var; j++)
					x[vx] ^= (a[i][j] && x[j]);
				sum += x[vx--];
			}
			else break;
		}
		if (sum < ans) ans = sum;
		return ;
	}
	x[f[k]] = 0; dfs (k+1);
	x[f[k]] = 1; dfs (k+1);
}



int Gauss ()
{
	memset (has, false, sizeof(has));
	int i, j, k, col, max_r;
	fn = 0;
	for (k = col = 0; k < equ && col < var; k++, col++)
	{
		max_r = k;
		for (i = k+1; i < equ; i++)
			if (a[i][col] > a[max_r][col])
				max_r = i;
		if (k != max_r) for (j = k; j <= var; j++) swap (a[k][j], a[max_r][j]);
		if (a[k][col] == 0)
		{
			has[col] = true;
			f[fn++] = col; --k;
			continue;
		}
		for (i = k+1; i < equ; i++)
		{
			if (a[i][col] == 0) continue;
			for (j = col; j <= var; j++) a[i][j] ^= a[k][j];
		}
	}
	ans = inf;		//无解标志
	for (i = k; i < equ; i++) if (a[i][col] != 0) return -1;
	rk = k;		//矩阵的秩
	dfs (0);
	return var-k;
}


int main()
{
    int tcase;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    scanf("%d", &tcase);
    char str[M];
    for(int k = 1; k <= tcase; ++ k) {
        scanf("%s", str);
        int n = strlen(str);
        //printf("%s\n", str);
        equ = var = n;
        ini();
        for(int i = 0; i < n; ++ i) {
            for(int j = i; j < n; ++ j)
                a[i][j] = 1;
        }
        for (int i = 0; i < n; i++)
        {
            if(str[i] == '+')
                a[i][n] = 0;
            else a[i][n] = 1;
        }
        Gauss();
        printf ("Case #%d: %d\n", k, ans);
    }

    fclose(stdout);
    fclose(stdin);

    return 0;
}

