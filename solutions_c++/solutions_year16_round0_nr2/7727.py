#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("d:/work/large.in","r",stdin);
    freopen("d:/work/outputlar.out","w",stdout);
    int w;
    cin>>w;
    for(int i=1;i<=w;i++)
    {
        char ab[105];
        int a[105];
        cin>>ab;
        int j=0;
        while(ab[j]!='\0')
        {
            if(ab[j]=='+')
                a[j]=1;
            else
                a[j]=0;
            j++;
        }
        j--;
        int pos=-1,num=0,m=0;
        while(1)
        {
            for(int k=0;k<=j;k++)
            {
                if(a[k]==0)
                {
                    pos=k;
                    m=1;
                }
            }
            for(int k=0;k<=pos;k++)
            {
                a[k]-=1;
                if(a[k]<0)
                    a[k]=1;
            }
            if(m==0)
                break;
            num++;
            m=0;
        }
        cout << "Case #" << i << ": " << num << endl;
    }
    return 0;
}
