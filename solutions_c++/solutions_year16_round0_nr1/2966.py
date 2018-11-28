#include <bits/stdc++.h>
using namespace std;

int test;
int n;
void input(){
    cin>>n;
}

void sol(){
    test++;
    long long y=0;
    int ans=0;
    int x=0;
    while (x!=(1<<10)-1 && ans<=10000){
        ans++;
        y=n*ans;
        if (y==0) x|=1;
        while (y){
            x|=(1<<(y%10));
            y/=10;
        }
    }

    if (x!=(1<<10)-1)
        cout<<"Case #"<<test<<": INSOMNIA"<<endl;
    else
        cout<<"Case #"<<test<<": "<<ans*n<<endl;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A1.txt","w",stdout);
    int t;
    cin>>t;
    while (t--){
        input();
        sol();
    }
    return 0;
}
