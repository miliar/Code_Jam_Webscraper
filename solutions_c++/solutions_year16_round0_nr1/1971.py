#include <stdio.h>
#include <set>
using namespace std;
set <int> s;
long long n,t;
void mete(long long n)
{
    while (n>0)
    {
        s.insert(n%10);
        n/=10;
    }
}
int main()
{
    freopen("input.txt","r+",stdin);
    freopen("output.txt","w+",stdout);
    scanf("%d",&t);
    for (int c=1;c<=t;c++)
    {
        scanf("%lld",&n);
        printf("Case #%d: ",c);
        if (n>0)
        {
            s.clear();
            long long i=1;
            while (s.size()<10)
            {
                mete(i*n);
                i++;
            }
            i--;
            printf("%lld\n",i*n);
        }
        else
            printf("INSOMNIA\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
