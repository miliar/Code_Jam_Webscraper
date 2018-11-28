#include <bits/stdc++.h>

using namespace std;

int solve(int N)
{
    int done = 0,cnt=0;
    while(done!=1023) {
        cnt++;
        int val=cnt*1LL*N;
        while(val>0) {
            done |= (1<<(val%10));
            val/=10;
        }
    }
    return cnt*N;
}

int main()
{
    int t,n;
    cin>>t;
    for(int T=1;T<=t;T++) {
        cin>>n;
        if(n==0) cout<<"Case #"<<T<<": INSOMNIA\n";
        else cout<<"Case #"<<T<<": "<<solve(n)<<"\n";
    }
    return 0;
}
