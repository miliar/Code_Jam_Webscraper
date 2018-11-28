#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
void Solve(int);
int answer(int x)
{
    int mark[10] = {0};
    int cnt = 0;
    int y = 0;
    while(cnt < 10)
    {
        y = y + x;
        int temp = y;
        while(temp > 0)
        {
            if(mark[temp%10] == 0)
            {
                mark[temp%10] = 1;
                cnt++;
            }
            temp /= 10;
        }
    }
    return y;
}
int main()
{
    freopen("C:\\Users\\dell\\Downloads\\inputa.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputa.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++) Solve(t);
    return 0;
}
void Solve(int TestCase)
{
    int n;
    scanf("%d",&n);
    if(n > 0) printf("Case #%d: %d\n",TestCase,answer(n));
    else printf("Case #%d: INSOMNIA\n",TestCase);
}
