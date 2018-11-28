#include <bits/stdc++.h>
//#define DEBUG
using namespace std;
int sol[1000001];
typedef long long ll;
typedef pair<int,int> pii;

int rev(int n)
{
    int a = 0;
    while(n > 0)
    {
        a = a*10 + n%10;
        n /= 10;
    }
    return a;
}

int main()
{
    #ifndef DEBUG

    ifstream in("a_s2.in");
    cin.rdbuf(in.rdbuf());
    ofstream out("a_s2.out");
    cout.rdbuf(out.rdbuf());

    #endif
    sol[1] = 1;
    for(int i = 1; i < 21; i++)
        sol[i] = i;
    for(int i = 21; i < 1000001; i++)
    {
        int j = rev(i);
        if(i%10 == 0|| i <= j)
            sol[i] = sol[i-1] + 1;
        else
            sol[i] = min(sol[i-1],sol[j]) + 1;
    }

    int T;
    cin>>T;
    for(int X = 1; X <= T; X++)
    {
        ll N,ans = 0,cnt = 0;
        cin>>N;

        cout<<"Case #"<<X<<": ";
        cout<<sol[N]<<endl;
    }
    return 0;
}

