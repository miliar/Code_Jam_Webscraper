#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
long long int input[100005];
bool flag[10];
int main()
{
    freopen ("A-large.in","r",stdin);
    int c;
    scanf("%d",&c);
    for(int i=0; i<c ;++i)
    {
        scanf("%lld",&input[i]);
    }

    fclose (stdin);
freopen ("out.txt","w",stdout);

    for(int i=0;i<c;++i){
    memset(flag,0,sizeof(flag));
    int mul=0;
    if(input[i]==0)
    {
        printf("Case \#%d: INSOMNIA\n",i+1);
        continue;
    }
    while(!flag[0]||!flag[1]||!flag[2]||!flag[3]||!flag[4]||!flag[5]||!flag[6]||!flag[7]||!flag[8]||!flag[9])
    {

        mul++;
        long long int a = input[i]*mul;

        while(a)
        {
            flag[a%10] =true;
            a/=10;
        }
    }
        printf("Case \#%d: %lld\n",i+1,mul*input[i]);
    }


    fclose (stdout);
}
