#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int a, b;
int flag[17];

int main(void)
{
    int ncase;
    int v = 0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        memset(flag, 0, sizeof(flag));
        int a, tmp;
        for(int e = 1; e <= 2; ++e)
        {
        scanf("%d",&a);
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
        {
            scanf("%d",&tmp);
           if(i == a)
            flag[tmp]++;
        }
        }
        int ans = -1, num = 0;
        for(int i = 1; i <= 16; ++i)
            if(flag[i] == 2)
        {
            num++;
            ans = i;
        }
        cout<<"Case #"<<++v<<": ";
        if(num == 1)
            cout<<ans;
        else if(num > 1)
            cout<<"Bad magician!";
        else
            cout<<"Volunteer cheated!";
        cout<<endl;
    }
    return 0;
}
