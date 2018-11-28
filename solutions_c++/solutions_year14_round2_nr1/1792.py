#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

typedef struct
{
	char ch;
	int jmlh;
}huruf;
huruf daftar[110][110];
int bykDaftar[110];

int abS(int a)
{
	if(a < 0) return -1*a;
	else return a;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, tc;
	bool bisa;
	char str[110][110];
	int i, j;
	int N;
	int ans;
	
	cin >> T;
	
	for(tc=1;tc<=T;tc++)
	{
		scanf("%d", &N);
		for(i=0;i<N;i++)
		{
			scanf("%s", str[i]);
			bykDaftar[i] = 0;
		}
		bisa = true;
		for(i=0;i<N;i++)
		{
			int len= strlen(str[i]);
			for(j=0;j<len;j++)
			{
				char ct = str[i][j];
				int ctr = 1;
				while(j+1<len && str[i][j+1]==str[i][j])
				{
					j++; ctr++;
				}
				daftar[i][bykDaftar[i]].ch = ct;
				daftar[i][bykDaftar[i]].jmlh = ctr;
				bykDaftar[i] += 1;
			}
		}
		
		for(i=1;i<N;i++)
		{
			if(bykDaftar[i] != bykDaftar[0]) //klo sama yg pertama beda
				bisa = false;
		}
		
		if(bisa)//kalau jumlah semua daftar nya sama
		{
			for(j=0;j<bykDaftar[0];j++)
			{
				for(i=1;i<N;i++)
				{
					if(daftar[i][j].ch != daftar[0][j].ch) //kalau ada urutan huruf yg beda
					{
						bisa = false;
					}
				}
			}
		}
		
		if(bisa) // kalau juga masih bisa baru cek jawaban nya
		{
			ans = 0;
			for(j=0;j<bykDaftar[0];j++) //utk smua huruf
			{
				int tot = 0;
				for(i=0;i<N;i++)
				{
					tot += daftar[i][j].jmlh; //jumlahin smua kmunculan nya
				}
				int avg = (double)tot/N + 0.5;
				for(i=0;i<N;i++)
				{
					ans += abS(avg-daftar[i][j].jmlh); //geserin brp per - huruf nya..
				}
			}
			
			printf("Case #%d: %d\n", tc, ans);
		}
		else printf("Case #%d: Fegla Won\n", tc);
		
	}

	return 0;
}
