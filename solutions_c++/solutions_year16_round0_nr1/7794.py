#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int isMarked(int num[])
{
    for(int i=0;i<10;i++)
    {
        if(num[i]==0)
            return 0;
        if((i==9)&&(num[i]==1))
            return 1;
    }
}
int main()
{
    #ifndef GOOGLE_CODE_JAM
    freopen("A-large.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    #endif
     int i,j,T;
    cin>>T;
    long int ansT[T];
    for(i=0;i<T;i++)
    {
        long int N,temp;
        int num[10]={0,0,0,0,0,0,0,0,0,0};
        cin>>N;
        if(N==0)
        {
            ansT[i]=-1;
            continue;
        }
        for(j=1;!isMarked(num);j++)
        {
            temp=N*j;
            int ind;
           while(temp)
            {
            ind=temp%10; temp=temp/10;
            num[ind]=1;
            }
        }
        ansT[i]=N*(j-1);
    }
    for(int ansi=0;ansi<T;ansi++)
    {
        if(ansT[ansi]==-1)
            printf("Case #%d: INSOMNIA\n",ansi+1);
        else
            printf("Case #%d: %ld\n",ansi+1,ansT[ansi]);
    }
    return 0;
}
