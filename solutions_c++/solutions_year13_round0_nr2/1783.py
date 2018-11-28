#include<stdio.h>
#include<map>
using namespace std;

int t, R, C, table1[101][101], table2[101][101], aLen[101], size;
map<int, int> mLen;

void read()
{
    int tmp;

    for(int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
        {
            scanf("%d", &tmp);
            mLen[tmp] = 1;
            table1[r][c] = tmp;
        }

    size = 0;
    typedef std::map<int, int>::iterator it_type;
    for(it_type iterator = mLen.begin(); iterator != mLen.end(); iterator++) 
        aLen[size++] = iterator->first;
}

bool checkR(int r, int val)
{
    for(int c = 0; c < C; c++)
        if(table1[r][c] != val)
            return false;
    return true;
}

void fillR(int r, int val)
{
    for(int c = 0; c < C; c++)
        table2[r][c] = val;
}

bool checkC(int c, int val)
{
    for(int r = 0; r < R; r++)
        if(table1[r][c] != val)
            return false;
    return true;
}

void fillC(int c, int val)
{
    for(int r = 0; r < R; r++)
        table2[r][c] = val;
}

bool isSexist(int val)
{
    for(int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
            if(table1[r][c] == val)
                return false;
    return true;
}

bool isGoback(int s, int t)
{
    for(int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
            table2[r][c] = table1[r][c];

    for(int r = 0; r < R; r++)
    {
        if(checkR(r, s))
            fillR(r, t);
    }

    for(int c = 0; c < C; c++)
    {
        if(checkC(c, s))
            fillC(c, t);
    }
    
    for(int r = 0; r < R; r++)
        for(int c = 0; c < C; c++)
            table1[r][c] = table2[r][c];

    if(!isSexist(s))
        return false;
    
    return true;
}

bool solve()
{
    for(int i = 0; i < size-1; i++)
        if(!isGoback(aLen[i], aLen[i+1]))
            return false;
    return true;

}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    

    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
         scanf("%d %d", &R, &C);
         read();
         if(solve())
             printf("Case #%d: YES\n", i);
         else
             printf("Case #%d: NO\n", i);
    }

	return 0;

}
