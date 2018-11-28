#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;

string s;
int l;
int a[100];
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;++i)
    {
        cin>>s;
        l=s.size();
        for(int j=0;j!=l;++j)
            a[j]=s[j]=='-'? 0:1;
        int s=0;
        for(int k=l-1;k>=0;--k)
        {
            if(a[k]==0)
            {
                ++s;
                for(int j=k;j>=0;--j) a[j]=1-a[j];
            }
        }
        printf("Case #%d: %d\n",i,s);
    }
    return 0;
}
