#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#define REG  int
int isPalindrome(int n)
{
    int a=0,m=n;
    while(n)
    {
        a=a*10;
        a=a+n%10;
        n=n/10;
    }
    if(a==m)return 1;
    return 0;
}
int isinarray(int ita,int j,int *array)
{
    int f=0;
    int i=0;
    for(i;i<ita;i++)
        {if(array[i]==j)return 1;
        if(array[i]>j) return 0;
        }
        return 0;
}
int main()
{
    int n,i,j,k,l,sq,it,t;
    int array[200],ita=0;
      freopen ("C-small-attempt1.in","r",stdin);
    freopen ("C-small-attempt1.out","w",stdout);
    //FILE *fin=fopen("C-small-attempt0.in", "r");
   //  FILE *fout=fopen("C-small-attempt0.out", "w");
    //   printf("%d   %d",isPalindrome(121),isPalindrome(16));
    scanf("%d",&n);
    for(i=0; i<n; i++)
    {
        scanf("%d%d/n",&k,&l);
        //printf("%d %d\n",sq,k);
        it=3;
        for(j=1; j<k; it=it+2)
        {
            //if(isPalindrome(j))array[ita++]=j;
            j=j+it;
           // printf("%d ",j);
        }
            k=0;
        for(j; j<=l; )
        {
            if(isPalindrome(j))
            {ita=sqrt(j);
            if(isPalindrome(ita))
            {
                k++;
               // printf("%d ",j);
            }}
            j=j+it;
            it=it+2;
        }
        printf("Case #%d: %d\n",i+1,k);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
