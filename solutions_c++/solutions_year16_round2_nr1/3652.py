#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
        char s[20001];
        int d[10],a[26];
        scanf("%s",&s);
        for(int i=0;i<10;i++)
            d[i]=0;
        for(int i=0;i<26;i++)
            a[i]=0;
        for(int i=0;s[i]!='\0';i++)
        {
            int x=(int)s[i]-'A';
            //printf("%i ",x);
            a[x]++;
        }
        d[0]=a[25];
        //printf("%i",d[0]);
        d[2]=a[(int)'W'-'A'];
        d[4]=a[(int)'U'-'A'];
        d[6]=a[(int)'X'-'A'];
        d[8]=a[(int)'G'-'A'];
        d[1]=a[(int)'O'-'A']-d[0]-d[2]-d[4];
        d[3]=a[(int)'R'-'A']-d[0]-d[4];
        d[5]=a[(int)'F'-'A']-d[4];
        d[7]=a[(int)'S'-'A']-d[6];
        d[9]=(a[(int)'N'-'A']-d[1]-d[7])/2;
        printf("Case #%i: ",x);
        for(int i=0;i<10;i++)
        {
            while(d[i]!=0)
            {
                printf("%i",i);
                d[i]--;
            }
        }
        printf("\n");
        x++;
    }
	return 0;
}
