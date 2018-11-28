#include<bits/stdc++.h>
using namespace std;

void mark(long long a, vector<bool>& arr){
    while(a){
        arr[a%10] = true;
        a /= 10;
    }
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    for(int T=0 ; T<t ; ++T){
        long long n;
        cin>>n;
        if(n == 0){
            cout<<"Case #"<<T+1<<": INSOMNIA\n";
            continue;
        }
        vector<bool> visited(10, false);
        long long mul = 1;
        bool flag = false;
        while(!flag){
            flag = true;
            for(int i=0 ; i<10 ; ++i)
                flag &= visited[i];
            if(flag)
                break;
            mark(n*mul, visited);
            mul++;
        }
        cout<<"Case #"<<T+1<<": "<<n*(mul-1)<<"\n";
    }
    return 0;
}
