# include <stdio.h>

int n, m;
int a[128][128];

int rowmax[128];
int colmax[128];

int main()
{
	int kase = 1, tests;
	int i, j;
	int flag = 0;

	freopen("B-large.in", "r", stdin);
	freopen("B-largeout.txt", "w", stdout);

	scanf("%d", &tests);

	while(tests-->0){
	
		scanf("%d %d", &n, &m);

		for(i = 0; i < 128; i++){
			rowmax[i] = colmax[i] = 0;
		}

		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				scanf("%d", &a[i][j]);

				if(a[i][j] > rowmax[i]) rowmax[i] = a[i][j];
				if(a[i][j] > colmax[j]) colmax[j] = a[i][j];

			}
		}


		flag = 0;
		for(i = 0; i < n && flag == 0; i++) {
			for(j = 0; j < m && flag == 0; j++) {

				if(a[i][j] >= rowmax[i] || a[i][j] >= colmax[j])
				{
				
				}
				else
				{
					flag = 1;
				}

			}
		}

		if(flag == 0)
		printf("Case #%d: YES\n", kase);
		else
			printf("Case #%d: NO\n", kase);

		kase++;

	}

	return 0;
}