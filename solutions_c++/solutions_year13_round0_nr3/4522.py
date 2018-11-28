
#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)

// Problem C //

int A,B;

#define toIndex(row,column) ((row)*M+(column) )

int    isSqure(int number)
{
    int squared = (int)sqrt(number);
    
    if ( squared * squared == number)
        return squared;
    else
        return 0;
}

bool    isFair( int number )
{
    
    int digits[10];
    int index = 0;

    while (number != 0) {
        
        digits[index++] = number % 10;
        number /= 10;
        
    }
    
    int middle = index/2;
    int first , second;
    
    first = 0, second = index-1;
    while(middle--)
    {
        if (digits[first] != digits[second] )
            return false;
    }
  
    return true;;
    
}

void solve() {
    int found = 0;
    int root = 0;
    scanf("%d %d", &A, &B);
    for( int i = A; i <=B; i++)
    {
        if( isFair(i))
        {
            root = isSqure(i);
            if (root != 0 && isFair(root))
            {
                found++;
            }
        }
    }
    
    cout  << found << endl;
}

int main() {
    
#ifdef ALEX_PRIVATE_TEST
    freopen("/Users/admin/Documents/input.txt", "rt", stdin);
    freopen("/Users/admin/Documents/output.txt", "wt", stdout);
#endif
    
    int tt;
    scanf("%d", &tt);
    forn(ii, tt) {
        printf("Case #%d: ", ii + 1);
        solve();
    }
    return 0;
    
}




