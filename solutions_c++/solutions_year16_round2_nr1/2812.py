#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;
#define ll long long int
int c[75];
int main()
{
    int t,i,p,temp,j=0;
    scanf("%d",&t);
    getchar();
    char a[2002];
    while(t--)
    {
        j++;
        scanf("%s",a);
        int b[91]={0};
        int c1=0;
        for(i=0;a[i]!='\0';i++)
        {
            p=a[i];
            b[p]++;
        }
        if(b[90]!=0)
        {
            temp=b[90];
            b[90]=0;
            b[69]-=temp;
            b[82]-=temp;
            b[79]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[k]=0;
        }
        if(b[87]!=0)
        {
            temp=b[87];
            b[87]=0;
            b[84]-=temp;
            b[79]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=2;
        }
        if(b[85]!=0)
        {
            temp=b[85];
            b[85]=0;
            b[70]-=temp;
            b[79]-=temp;
            b[82]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=4;
        }
        if(b[88]!=0)
        {
            temp=b[88];
            b[88]=0;
            b[83]-=temp;
            b[73]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=6;
        }
        if(b[71]!=0)
        {
            temp=b[71];
            b[71]=0;
            b[69]-=temp;
            b[73]-=temp;
            b[72]-=temp;
            b[84]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=8;
        }
        if(b[79]!=0)
        {
            temp=b[79];
            b[79]=0;
            b[78]-=temp;
            b[69]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=1;
        }
        if(b[70]!=0)
        {
            temp=b[70];
            b[70]=0;
            b[73]-=temp;
            b[86]-=temp;
            b[69]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=5;
        }
        if(b[83]!=0)
        {
            temp=b[83];
            b[83]=0;
            b[69]=b[69]-2*temp;
            b[86]-=temp;
            b[78]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=7;
        }
        if(b[84]!=0)
        {
            temp=b[84];
            b[84]=0;
            b[69]=b[69]-2*temp;
            b[72]-=temp;
            b[82]-=temp;
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=3;
        }
        if(b[73]!=0)
        {
            temp=b[73];
            for(int k=0;k<temp;k++,c1++)
                    c[c1]=9;
        }
        sort(c,c+c1);
        printf("Case #%d: ",j);
        for(i=0;i<c1;i++)
            printf("%d",c[i]);
        printf("\n");
    }
    return 0;
}
