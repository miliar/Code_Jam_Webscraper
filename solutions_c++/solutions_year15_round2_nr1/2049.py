
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
using namespace std;
int dp[1000001];
long long flip(long long a) {
    long long b=a,c=0,e,f;
    int d=ceil(log10(b));
    for(int i=0;i<d;i++) {
        e=pow(10.0,d-i-1);
        f=pow(10.0,i);
        c+=((b/e)%10)*f;
    }
    return c;
}
int main() {
    ifstream cin("wowo.in");
    ofstream cout("wow.in");
    dp[0]=1;
    long long a,b;
    int i,t,k,j=1;
    cin>>t;
    queue<int>hello;
    hello.push(1);
    while(!hello.empty()) {
        k=hello.size();
        for(i=0;i<k;i++) {
            if(!dp[hello.front()]) {
                dp[hello.front()]=j;
                b=flip(hello.front());
                if(hello.front()+1<=1000000&&!dp[hello.front()+1]) hello.push(hello.front()+1);
                if(b<=1000000&&!dp[b]) hello.push(flip(hello.front()));
            }
            hello.pop();
        }
        j++;
    }
    for(i=0;i<t;i++) {
        cin>>a;
        cout<<"Case #"<<i+1<<": "<<dp[a]<<endl;
    }
}
