#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define MAX 1005


int  main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i1=1;i1<=t;i1++)
    {
        char s[MAX],s1[MAX],s2[MAX];
        scanf("%s",s);
        int c=strlen(s);
        for(int i=0;i<c;i++)
        {
            if(i==0)
            {
                s1[i]=s[i];
                s1[1]='\0';
            }
            else
            {
                if(s1[0]<=s[i])
                {
                    for(int j=0;j<i;j++)
                    {
                        s2[j]=s1[j];
                    }
                    for(int j=1;j<=i;j++)
                    {
                        s1[j]=s2[j-1];
                    }
                    s1[0]=s[i];
                }
                else
                {
                    s1[i]=s[i];
                    s1[i+1]='\0';
                }
            }
        }
        cout<<"Case #"<<i1<<":"<<" ";
        for(int i=0;i<c;i++)
        cout<<s1[i];
        cout<<endl;
    }
    return 0;
}
