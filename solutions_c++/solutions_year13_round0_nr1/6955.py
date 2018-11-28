#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 10;
char g[MAXN][MAXN];

int check(char ch)
{
    int nc, nt;
    
    for (int i = 0; i < 4; i++)
    {
        nc = nt = 0;
        for (int j = 0; j < 4; j++)
            if (g[i][j] == ch)
               nc++;
            else if (g[i][j] == 'T')
                nt++;
        
        if (nc == 4 || (nc == 3 && nt == 1))
        {
			//printf ("1. ch=%c nc=%d nt=%d\n", ch, nc, nt); 
        	return 1;
		}
	}
	
	for (int j = 0; j < 4; j++)
	{
		nc = nt = 0;
		for (int i = 0; i < 4; i++)
			if (g[i][j] == ch)
				nc++;
			else if (g[i][j] == 'T') 
				nt++;
		
		if (nc == 4 || (nc == 3 && nt == 1))
        {
		//	printf ("2. ch=%c nc=%d nt=%d\n", ch, nc, nt); 
        	return 1;
		}
	}
	nc = nt = 0;
	for (int i = 0; i < 4; i++)
		if (g[i][i] == ch)
			nc++;
		else if (g[i][i] == 'T')
			nt++;
	if (nc == 4 || (nc == 3 && nt == 1))
    {
		//printf ("3. ch=%c nc=%d nt=%d\n", ch, nc, nt); 
       	return 1;
	}
	
	nc = nt = 0;
	for (int i = 0; i < 4; i++)
		if (g[3 - i][i] == ch)
			nc++;
		else if (g[3 - i][i] == 'T')
			nt++;
	if (nc == 4 || (nc == 3 && nt == 1))
    {
		//printf ("4. ch=%c nc=%d nt=%d\n", ch, nc, nt); 
       	return 1;
	}
	
	return 0;
}
        
void pr()
{
	puts("--------------");
	for (int i = 0; i < 4; i++)
		printf ("%s\n", g[i]);
	puts ("---------------");
}
	         
int main()
{
    //freopen ("A-small-attempt0.in", "r", stdin);

 	freopen ("A-large.in", "r", stdin); 
 
    freopen ("1.out.large", "w", stdout);
     
    int csnum, cs;
    scanf ("%d", &csnum);
    getchar();
    for (cs = 1; cs <= csnum; cs++)
    {
        int pFlg = 0;
        for (int i = 0; i < 4; i++)
        {
            gets (g[i]);
            for (int j = 0; j < 4; j++)
                if (g[i][j] == '.')
                   pFlg = 1;
        }
     	gets(g[5]);
		//pr();
		//printf ("pFlg=%d\n", pFlg);
		 
        printf ("Case #%d: ", cs);
        
        if (check('X'))
            printf ("X won\n");
        else if (check('O'))
            printf ("O won\n");
        else if (pFlg == 0)
            printf ("Draw\n");
        else
            printf ("Game has not completed\n");
    }
    
    //while(1);
    return 0;
}
                    
