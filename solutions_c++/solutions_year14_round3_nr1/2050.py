#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int map1[4];
int map2[4];

int gcd(int a, int b)
{
    if (b==0)
        return a;
    return gcd(b, a % b);
}

int isPowerOfTwo(unsigned int x)
{
    return ((x != 0) && ((x & (~x + 1)) == x));
}

int main()
{
    int t;
    scanf("%d", &t);
    int id = 1;
    while (t--)
	{
        bool ok = true;
	
        int num, den;
		scanf("%d/%d", &num, &den);
        
        if( num<0 || num > den )
            ok = false;
		
        int gen = 0;
        if( ok )
        {
            int d = gcd(num, den);
            num /= d;
            den /= d;
            
            if( isPowerOfTwo(den) )
            {
                while( num<den )
                {
                    den/=2;
                    gen++;
                }
            }
            else
                ok = false;
        }
		
        if( gen > 40 )
         ok = false;

		if( !ok )
            printf("Case #%d: impossible\n", id++);
		else
            printf("Case #%d: %d\n", id++, gen);
	}
	return 0;
}
