#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <utility>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
const int maxn = 10005;

class Quater{
public:
    char c;
    bool ng;
    Quater(char _c='1', bool _ng=false): c(_c), ng(_ng){};
    //Quater(char _c, bool _ng): c(_c), ng(_ng){};
    Quater operator *(const Quater & a) const
    {
        if (c == '1')  return Quater(a.c, ng ^ a.ng);
        if (a.c == '1') return Quater(c, ng ^ a.ng);
        if (c == a.c) return Quater('1', !(ng ^ a.ng));
        
        switch (c)
        {
            case 'i':
                switch(a.c)
                {
                case 'j': return Quater('k', ng ^ a.ng);
                case 'k': return Quater('j', !(ng ^ a.ng));
                }
                break;
            case 'j':
                switch(a.c)
                {
                case 'i': return Quater('k', !(ng ^ a.ng));
                case 'k': return Quater('i', ng ^ a.ng);
                }
                break;
            case 'k':
                switch(a.c)
                {
                case 'i': return Quater('j', ng ^ a.ng);
                case 'j': return Quater('i', !(ng ^ a.ng));
                }
                break;
        }
        return Quater('1', (ng ^ a.ng));
    }
};

char str[maxn];

int main()
{
    int T, I, n, x, i, j, k, lx, rx;
   	Quater all, a, b, c, lwhole, rwhole;
    
    scanf ("%d", &T);
    for (I=1; I<=T; I++)
    {
        scanf ("%d%d%s", &n, &x, str);
        printf ("Case #%d: ", I);
        
        all = Quater('1', false);
        for (i=0; i<n; i++) all = all * Quater(str[i], false);
        
        lwhole = Quater('1', false);
        for (lx = 0; lx < 4; lx ++)
        {
            a = lwhole;
            for (i=0; i<n; i++)
            {
                a = a * Quater(str[i], false);
                if (a.c == 'i' && a.ng == false) break;
            }
            if (a.c == 'i' && a.ng == false) break;
            
            lwhole = lwhole * all;
        }
        if (!(a.c == 'i' && a.ng == false))
        {
            printf ("NO\n");
            continue;
        }
        //lx, i;
        
        rwhole = Quater('1', false);
        for (rx = 0; rx < 4; rx++)
        {
            c = rwhole;
            for (j=n-1; j>=0; j--)
            {
                c = Quater(str[j], false) * c;
                if (c.c == 'k' && c.ng == false) break;
            }
            if (c.c == 'k' && c.ng == false) break;
            
            rwhole = all * rwhole;
        }
        if (!(c.c == 'k' && c.ng == false))
        {
            printf ("NO\n");
            continue;
        }
        // j, rx;
        
        //special case:
        if (lx + rx + 1 == x && i < j)
        {
            b = Quater('1', false);
            for (k=i+1; k<j; k++)
            {
                b = b * Quater(str[k], false);
            }
            if (b.c == 'j' && b.ng == false)
            {
                printf ("YES\n");
                continue;
            }
        }
        
        if (lx + rx + 2 > x)
        {
            printf ("NO\n");
            continue;
        }
        x -= lx + rx + 2;
        x %= 4;
        
        b = Quater('1', false);
        for (k=i+1; k<n; k++)
        {
            b = b * Quater(str[k], false);
        }
        while (x--)
        {
            b = b * all;
        }
        for (k=0; k<j; k++)
        {
            b = b * Quater(str[k], false);
        }
        
        if (b.c == 'j' && b.ng == false)
        {
            printf ("YES\n"); 
        }
        else
            printf ("NO\n"); 
        
    }
}