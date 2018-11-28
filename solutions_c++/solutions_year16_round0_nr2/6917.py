#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
char a[105];
int main()
{
    /*FILE *in,*out;
    in=fopen("in","r+");
    out=fopen("out","w+");*/
    int t;
    char temp;
    //fscanf(in,"%d",&t);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int ant=0;
        //fscanf(in," %s",a);
        scanf(" %s",a);
        int len=strlen(a);
        temp=a[0];
        for(int j=1;j<len;j++)
        {
            if(a[j]!=temp)
            {
                ant++;
                temp=a[j];
            }
        }
        if(temp=='-') ant++;
        //fprintf(out,"Case #%d: %d\n",i,ant);
        printf("Case #%d: %d\n",i,ant);
    }
    return 0;
}
