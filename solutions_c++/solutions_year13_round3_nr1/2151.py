#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std ;
 char a[1000007];
 int pos[1000000];
int main()
{
    int i,j,count,l,t,c,n,temp,k;
     FILE *fp1,*fp2;
    fp1=fopen("A-small-attempt0.in","r");
    fp2=fopen("Goutput.txt","w");
    fscanf(fp1,"%d",&t);
    c=1;
    while(t--)
    {
        fscanf(fp1,"%s",a);
        fscanf(fp1,"%d",&n);
        l=strlen(a);
        temp=count=0;
        k=1;
        pos[0]=-1;
        for(i=0;i<l;i++)
        {
            if(a[i]!='a'&& a[i]!='e'&& a[i]!='i'&& a[i]!='o'&& a[i]!='u')
            {
                temp=0;
                j=i;
                while(a[j]!='a'&& a[j]!='e'&& a[j]!='i'&& a[j]!='o' && a[j]!='u' && j<l)
                {
                    temp++;
                    j++;
                }
                if(temp>=n)
                {
                    pos[k]=i;
                    k++;
                }
            }
        }
        for(i=1;i<k;i++)
        {
            temp=l-pos[i]-n+1;
            count+=temp*(pos[i]-pos[i-1]);
        }
        fprintf(fp2,"Case #%d: %d\n",c,count);
        c++;
    }
    return 0;
    }
    

