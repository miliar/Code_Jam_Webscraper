#include<iostream>
#include<string>
#include<map>
#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<queue>

using namespace std;

int T;

bool isPal(int x)
{
    //cout <<"checking "<<x<<endl;
    string num;
    int i,j;
    while(x)
    {
        num+=(x%10+'0');
        x/=10;
    }
   // cout<<num<<" "<<num.size()<<endl;
    if(num.size() == 1) return true;
    for(i=0, j = num.size()-1; i != j; i++, j--)
    {
        if(num[i] != num[j]) break;
    }
    //cout<<"ii - "<<i<<" "<<j<<endl;

    return i >= j;
}

int checkNum(int x, int y)
{
    int i,ans = 0;

    for(i = x; i <= y; i++)
    {

        if(sqrt(i) == ((int) sqrt(i)) )
        {
            if(isPal(i) && isPal(sqrt(i))) ans++;

        }

    }
    return ans;
}

void solve()
{
    cin>>T;
    int x,y;
    for(int TT = 0 ; TT < T; TT++)
    {
        cin>>x>>y;
        printf("Case #%d: %d\n", TT+1, checkNum(x,y));
    }
}

int main()
{
    solve();

    return 0;
}
