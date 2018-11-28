#include<string.h>
#include<stdio.h>
using namespace std;

int main() 
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int n;
        char ch[101];
        scanf("%s",ch);
        int q,k=0;
        int l=strlen(ch);
        //printf("%s %d\n",ch,l);
        char a[101];
        a[0]=ch[0];
        k++;
        
        for(int q=1;q<l;q++)
        {
            if(ch[q]!=ch[q-1])
            {
                a[k]=ch[q];
                //printf("%c",a[k]);
                k++;
            }
        }
        //printf("\n");
        int m=k;
        while(m--)
        {
            if(a[m]!='+')
            {
                break;
            }
        }
        printf("Case #%d: %d\n",i,m+1);
    }
	return 0;
}

