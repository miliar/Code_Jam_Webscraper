#include<bits/stdc++.h>
#include<list>
#define INT long long int
using namespace std;

int main()
{
    FILE *fp,*fq;
    fp=fopen("A-large.in","r");
    fq=fopen("output.txt","w");
    INT t,caseno=0,i,j,n,m;
    char str[1010],c,ch;
    fscanf(fp,"%lld",&t);
    while(t--)
    {
        list<char>dq;
        fscanf(fp,"%s",str);
        for(i=0;str[i]!='\0';i++)
        {
            if(i==0)
            {
                dq.push_front(str[i]);
                c=str[i];
            }
            else if(str[i]>=c)
            {
                dq.push_front(str[i]);
                c=str[i];
            }
            else
                dq.push_back(str[i]);
        }
        list<char>::iterator it;
        fprintf(fq,"Case #%lld: ",++caseno);
        for(it=dq.begin();it!=dq.end();it++)
        {
            c=*it;
            fprintf(fq,"%c",c);
        }
        fprintf(fq,"\n");
    }
    return 0;
}
