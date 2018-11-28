#include <cstdlib>
#include <cstdio>

#define X(x, y) tab[y*4+x]

void solve(int T, char *tab)
{
    /*for(int y=0; y<4; ++y)
    {
	for(int x=0; x<4; ++x)
	{
	    printf("%c", tab[y*4+x]);
	}
    }*/

    int total = 0;
    int nX = 0, nO = 0, nT = 0;
    for(int y=0; y<4; ++y)
    {
	nX = nO = nT = 0;
	for(int x=0; x<4; ++x)
	{
	    if(X(x, y) == 'X') nX++;
	    else if(X(x, y) == 'O') nO++;
	    else if(X(x, y) == 'T') nT++;
	}
	
	total = total + nX + nO + nT;
	
	if(nX + nT == 4)
	{
	    printf("Case #%d: X won\n", T); 
	    return;
	}
	else if(nO + nT == 4)
	{
	    printf("Case #%d: O won\n", T); 
	    return;
	}
    }
	
    for(int x=0; x<4; ++x)
    {
	nX = nO = nT = 0;
	for(int y=0; y<4; ++y)
	{
	    if(X(x, y) == 'X') nX++;
	    else if(X(x, y) == 'O') nO++;
	    else if(X(x, y) == 'T') nT++;
	}
	
	if(nX + nT == 4)
	{
	    printf("Case #%d: X won\n", T); 
	    return;
	}
	else if(nO + nT == 4)
	{
	    printf("Case #%d: O won\n", T); 
	    return;
	}
    }
    
    nX = nO = nT = 0;
    for(int x=0, y=0; x<4; ++x, ++y)
    {	
	if(X(x, y) == 'X') nX++;
	else if(X(x, y) == 'O') nO++;
	else if(X(x, y) == 'T') nT++;
    }
    
    if(nX + nT == 4)
    {
	printf("Case #%d: X won\n", T); 
	return;
    }
    else if(nO + nT == 4)
    {
	printf("Case #%d: O won\n", T); 
	return;
    }
    
    nX = nO = nT = 0;
    for(int x=0, y=3; x<4; ++x, --y)
    {	
	if(X(x, y) == 'X') nX++;
	else if(X(x, y) == 'O') nO++;
	else if(X(x, y) == 'T') nT++;
    }
    
    if(nX + nT == 4)
    {
	printf("Case #%d: X won\n", T); 
	return;
    }
    else if(nO + nT == 4)
    {
	printf("Case #%d: O won\n", T); 
	return;
    }
    
    if(total == 16)
    {
	printf("Case #%d: Draw\n", T);
	return;
    }
    else
	printf("Case #%d: Game has not completed\n", T); 
}

int main(int argc, char **argv)
{
    int T = 0;
    scanf("%d\n", &T);
    
    for(int i=0; i<T; ++i)
    {
	char tab[16];
	for(int y=0; y<4; ++y)
	    scanf("%c%c%c%c\n", &tab[y*4], &tab[y*4+1], &tab[y*4+2], &tab[y*4+3]);
	
	solve(i+1, tab);
    }
    
    return 0;
}
