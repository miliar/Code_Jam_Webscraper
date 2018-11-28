#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

bool judge(int a)
{
    int c[10];
    int ans = a,num = 0,j = 0;
    while(ans)
    {
        c[j++] = ans%10;
        ans /= 10;
    }
    for(int i=0;i<j;i++)
    num = num * 10 + c[i];
    if(num==a)
    return true;
    return false;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas = 1,a,b,i,temp,total;
    cin >> t;
    while(t--)
    {
        scanf("%d%d",&a,&b);
        total = 0;
        printf("Case #%d: ",cas++);
        for(i=a;i<=b;i++)
        {
            temp = (int)sqrt((double)i);
            if(temp * temp ==i)
            {
                if(judge(temp) && judge(i))
                total++;
            }
        }
        cout << total << endl;
    }
    return 0;
}
