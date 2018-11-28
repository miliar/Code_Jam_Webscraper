#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int main()
{
    int number[] = {1,4,9,121,484};
    int t,i,j,max_len,a,b,k;
    scanf ("%d", &t);
    for (k=0;k<t;k++) {
        scanf ("%d%d", &a,&b);
        int x = upper_bound(number, number+5, b)-lower_bound(number,number+5,a);
        printf ("Case #%d: %d\n",k+1,x);
    }

}
