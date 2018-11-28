#include <iostream>

using namespace std;

char panel[4][4];
int empty;

void init()
{
    empty = 0;
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            char temp;
            cin >> temp;
            if(temp == '.') empty++;
            panel[i][j] = temp;
        }
    }    
}

char checkwin()
{
    //row
    for (int i=0; i<4; i++)
    {      
        char start;
        if (panel[i][0] == 'T')
        {
            start = panel[i][1];
            for (int j=2; j<4; j++)
            {
                if (panel[i][j] != start) goto r;
            }
        }
        else 
        {
            start = panel[i][0];
            for (int j=1; j<4; j++)
            {
                if (panel[i][j] != start && panel[i][j] != 'T') goto r;
            }
        }
        if(start=='.') goto r;
        return start;
r:
        continue;
    }
    //column
    for (int j=0; j<4; j++)
    {      
        char start;
        if (panel[0][j] == 'T')
        {
            start = panel[1][j];
            for (int i=2; i<4; i++)
            {
                if (panel[i][j] != start) goto l;
            }
        }
        else 
        {
            start = panel[0][j];
            for (int i=1; i<4; i++)
            {
                if (panel[i][j] != start && panel[i][j] != 'T') goto l;
            }
        }
        if(start=='.') goto l;
        return start;
l:
        continue;
    }
    //diagonal
    char start;
    if (panel[0][0] == 'T') start = panel[1][1];
    else start = panel[0][0];
    for (int k=1; k<4; k++)
    {
        if (panel[k][k] != start && panel[k][k] != 'T') goto n;
    }
    if (start!='.') return start;
n:
    if (panel[0][3] == 'T') start = panel[1][3];
    else start = panel[0][3];
    for (int k=1; k<4; k++)
    {
        if (panel[k][3-k] != start && panel[k][3-k] != 'T') goto d;
    }
    if(start=='.')goto d;
    return start;
d:
    return 'N';
}

int main()
{
   int N,n; 
   cin >> N;
   n = N;
   while(n--)
   {
       init();
       char r = checkwin();
       if (r=='X') cout << "Case #" << N-n << ": X won\n";
       if (r=='O') cout << "Case #" << N-n << ": O won\n";
       if (r=='N' && empty==0) cout << "Case #" << N-n << ": Draw\n";
       if (r=='N' && empty!=0) 
           cout << "Case #" << N-n << ": Game has not completed\n";
   }
   return 0;
}
