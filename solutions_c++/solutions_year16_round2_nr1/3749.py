#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
#define max 2000
int main()
{
    int t;
    freopen("A-small-attempt1.in","rt",stdin);
    freopen("output1.cpp","wt",stdout);
    cin>>t;
    int m=1;
    while(t--)
    {
       char ch[max];
       scanf("%s",ch);
       int l=strlen(ch);
       int a[10]={0,0,0,0,0,0,0,0,0,0};
       //int x;
       for(int i=0;i<l;i++)
       {
           if(ch[i]=='X')
            a[6]++;
           else if(ch[i]=='Z')
            a[0]++;
           else if(ch[i]=='U')
            a[4]++;
           else if(ch[i]=='G')
            a[8]++;
           else if(ch[i]=='W')
            a[2]++;
           else if(ch[i]=='O')
            a[1]++;
            else if(ch[i]=='T')
            a[3]++;
            else if(ch[i]=='F')
            a[5]++;
            else if(ch[i]=='S')
            a[7]++;
           else if(ch[i]=='I')
            a[9]++;
        }
        a[1]=a[1]-a[0]-a[4]-a[2];
        a[3]=a[3]-a[8]-a[2];
        a[5]=a[5]-a[4];
        a[7]=a[7]-a[6];
        a[9]=a[9]-a[6]-a[8]-a[5];
        int x=0;
        cout<<"Case #"<<m<<": ";
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<a[i];j++)
                cout<<x;
            x++;
        }
        cout<<endl;
        m++;

    }
}
