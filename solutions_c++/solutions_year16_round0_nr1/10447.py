#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
#define s(x) scanf("%lld",&x)
#define READ(f) freopen(f,"r",stdin);
#define WRITE(f) freopen(f,"w",stdout);

bool array[10];
int count;

int main(){
    READ("1.in");
    WRITE("1.out");
    long long int t,n,ones;
    long long int dummy,result,j;
    s(t);
    for(int i = 1;i <= t;i++)
    {
        memset(array,false,10);
        count = 10;
        s(n);
        if(n != 0)
        {
            j = 1;
            while(true && count!=0)
            {
                dummy = n*j;
                result = dummy;
                while(dummy)
                {
                    ones = dummy%10;
                    dummy = dummy/10;
                    if(!array[ones])
                    {
                        array[ones] = true;
                        count--;
                    }
                }
                j++;
            }
            printf("Case #%d: %lld\n",i,result);
        }
        else
            printf("Case #%d: INSOMNIA\n",i);
    }
}

