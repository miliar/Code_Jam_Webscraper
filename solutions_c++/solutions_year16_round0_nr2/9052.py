#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;
int main()
{
    int t;
    char s[1000];
    int caseCount=1;

    FILE* input=fopen("D:\\Education\\codes\\Google Code Jam\\B-large.in","r");
    FILE* output=fopen("D:\\Education\\codes\\Google Code Jam\\output.in","w");

    fscanf(input," %d",&t);

    while(t--)
    {
        fscanf(input," %s",s);
        int i=0;
        int count=0;
        int flag=0;
        char prev;
        int len=strlen(s);

        if(s[0]=='-') count=1;
        while(s[i]=='-' && i<len)
        {
            i++;
        }

        if(i==len)
        {
            fprintf(output,"Case #%d: %d\n",caseCount,count);
            caseCount++;
            continue;
        }
        prev=s[i];

        while(i<len)
        {
            while(s[i]==prev && i<len)
            {
                i++;
            }
            if(i<len&&s[i]=='-')
            {
                count=count+2;
            }
            if(i<len) prev=s[i];
        }

        fprintf(output,"Case #%d: %d\n",caseCount,count);
        caseCount++;
    }
    printf("Complete\n");
    return 0;
}
