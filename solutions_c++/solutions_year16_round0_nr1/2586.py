#include <bits/stdc++.h>

using namespace std;

bool used[10];

long long ans[1000100];

bool check(){
    for(int i = 0; i < 10; ++i)
        if(!used[i])
            return false;
    return true;
}

void makeituse(long long n){
    while(n != 0){
        used[n % 10] = true;
        n /= 10;
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    for(long long i = 1; i <= 1000000; ++i){
        for(int j = 0; j < 10; ++j)
            used[j] = false;
        for(long long j = 1; j <= 1000000; ++j){
            makeituse(i*j);
            if(check()){
                ans[i] = i * j;
                break;
            }
        }

    }

    /*for(int i = 0; i <= 1000000; ++i)
        if(ans[i] == 0)
            cout<<i<<" INSOMNIA"<<endl;
*/
    int t, n;
    cin>>t;
    for(int i = 1; i <= t; ++i){
        cin>>n;
        cout<<"Case #"<<i<<": ";
        if(n == 0)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<ans[n]<<endl;
    }

    return 0;
}
