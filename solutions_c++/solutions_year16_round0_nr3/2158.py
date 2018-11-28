#include <bits/stdc++.h>

using namespace std;

int cnt = 0;

void rec(int pos, int rem, int delta, string s){
    if(cnt == 500)
        return;
    if(rem == 0 && delta == 0){
        ++cnt;
        cout<<s;
        for(int i = 1; i <= 31 - s.size(); ++i)
            cout<<0;
        cout<<1;
        //cout<<s.size()<<endl;
        for(int k = 2; k <= 10; ++k)
            if(k%2==1)
                cout<<" 2";
            else
                cout<<" "<<k+1;
        cout<<endl;
    }
    if(rem == 0)
        return;
    if(pos > 30)
        return;
    if(pos%2 == 0)
        rec(pos + 1, rem - 1, delta + 1, s + "1");
    else
        rec(pos + 1, rem - 1, delta - 1, s + "1");
    rec(pos+1, rem, delta, s + "0");
}


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    /*for(int i = 2; i <= 14; i += 2){
        rec(1, i, 0);
    }
    */

    int t, n, k;
    cin>>t;
    cin>>n>>k;

    cout<<"Case #1:"<<endl;
    rec(1, 0, 0, "1");
    rec(1, 2, 0, "1");
    rec(1, 4, 0, "1");

    return 0;
}
