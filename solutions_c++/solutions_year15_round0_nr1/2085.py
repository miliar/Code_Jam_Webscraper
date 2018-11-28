#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,len,total;
    char str[1002];
    int min_friends=0;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        scanf("%d%s",&len,str);
        min_friends=0;
        total=str[0]-'0';
        for(int j=1;j<=len;j++)
        {
            if(j>total)
            {
                min_friends+=j-total;
                total=j;
            }
            total+=str[j]-'0';
        }
        printf("Case #%d: %d\n",i,min_friends);
    }

    return 0;
}
