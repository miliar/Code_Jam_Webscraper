#include <bits/stdc++.h>
#define mp make_pair
#define f first
#define s second

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int e=0;
    while(t--){
        e++;
        set<int> s;
        int n;
        cin>>n;
        if(n==0){
            cout<<"Case #"<<e<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int k=1;
        while(s.size()<10){
            int m=n*k;
            k++;
            while(m){
                int a=m%10;
                m/=10;
                s.insert(a);
            }

        }
        cout<<"Case #"<<e<<": "<<n*(k-1)<<endl;

    }

    return 0;
}
