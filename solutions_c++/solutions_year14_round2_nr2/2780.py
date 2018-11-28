#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int main(){
    if (fopen("input.txt", "r")) freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin>>T;
    for (int test = 0; test<T; test++){
        cout<<"CASE #"<<test+1<<": ";
        int A,B,K;
        int ans = 0;
        cin>>A>>B>>K;
        for (int i =0; i<A; i++){
            for (int j=0; j<B; j++){
                if ((i&j) < K){
                    ans++;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
