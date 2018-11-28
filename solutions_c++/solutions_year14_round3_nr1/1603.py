#include <iostream>
#include <map>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <stdlib.h>

using namespace std;
#define ull unsigned long long
#define ll long long
void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}
char* itoa(ull num, char* str, int base)
{
    ull i = 0;
    bool isNegative = false;

    /* Handle 0 explicitely, otherwise empty string is printed for 0 */
    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }

    // In standard itoa(), negative numbers are handled only with
    // base 10. Otherwise numbers are considered unsigned.
    if (num < 0 && base == 10)
    {
        isNegative = true;
        num = -num;
    }

    // Process individual digits
    while (num != 0)
    {
        ull rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }

    // If number is negative, append '-'
    if (isNegative)
        str[i++] = '-';

    str[i] = '\0'; // Append string terminator

    // Reverse the string
    reverse(str, i);

    return str;
}

ull gcd(ull a,ull b)
{
    if(b==0)
        return a;
    else return gcd(b,a%b);
}
int main()
{
    int t,j;
    scanf("%d",&t);

    for(j=1;j<=t;j++)
        {
            ull p,q;
            scanf("%llu",&p);
            getchar();
            scanf("%llu",&q);
            ull temp;
            temp=gcd(p,q);
            p/=temp;
            q/=temp;
            int count=0;
            if((q&(q-1))!=0)
            {
                 printf("Case #%d: impossible\n",j);
                 continue;
            }
           //char q1[1000000],p1[1000000];
            //atoi()
            char a[10000],b[10000];
            itoa(p,a,2);
            itoa(q,b,2);

                printf("Case #%d: %d\n",j,strlen(b)-strlen(a));




        }
    return 0;
}
