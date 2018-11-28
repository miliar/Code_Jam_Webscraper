#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int solve(){
    long long r,t,result=0;
    cin >> r >> t;
    while(t>=(2*r+1)){
        t-=2*r+1;
        r+=2;
        result++;
    }
    return result;
}

int main()
{
    int t; cin>>t;
    for (int i=1; i<=t; i++){
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    }
    return 0;
}
