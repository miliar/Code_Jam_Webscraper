#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
    freopen("infile.in","r",stdin);
    freopen("outfile.txt","w",stdout);
    int t, len, i, j;
    char str[1001];
    scanf("%d", &t);
    cin.ignore();
    for(j=1;j<=t;j++)
    {
        int cont=0;
        int cur=0;
        scanf("%d", &len);
        len++;
        cin.ignore();
        scanf("%s", &str);
        for(i=0;i<len;i++)
        {
            cur+=(int)(str[i]-48);
            if(cur<i+1)
            {
                cont+=i+1-cur;
                cur+=i+1-cur;
            }
        }
        printf("Case #%d: %d", j, cont);
        printf("\n");
    }
    return 0;
}
