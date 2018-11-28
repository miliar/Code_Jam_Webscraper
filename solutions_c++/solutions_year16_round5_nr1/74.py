#include<set>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<string>
#include<time.h>
#include<math.h>
#include<memory>
#include<vector>
#include<bitset>
#include<fstream>
#include<stdio.h>
#include<utility>
#include<sstream>
#include<string.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
using namespace std;
char a[100005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int zu;
    scanf("%d",&zu);
    int t;
    for (t=0;t<zu;t++)
    {
        printf("Case #%d: ",t+1);
        scanf("%s",a);
        int i;
        int cntc1=0,cntg1=0;
        int cntc2=0,cntg2=0;
        for (i=0;a[i]!='\0';i+=2)
        {
            if (a[i]=='C')
            {
                cntc1++;
            }
            else
            {
                cntg1++;
            }
            if (a[i+1]=='C')
            {
                cntc2++;
            }
            else
            {
                cntg2++;
            }
        }
        printf("%d\n",5*(min(cntc1,cntc2)+min(cntg1,cntg2)+(i/2)));
    }
    return 0;
}
