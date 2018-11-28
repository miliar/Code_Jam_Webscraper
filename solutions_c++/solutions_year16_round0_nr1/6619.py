#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1;i <= t;i++){
        long long int n,temp,temp1;
        cin>>n;
        temp1 = n;
        if(n == 0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        set<long long int> myset;
        while(myset.size() != 10){
            temp = n;
            while(temp != 0){
                myset.insert(temp%10);
                temp = temp/10;
            }
            n += temp1;
        }
        cout<<"Case #"<<i<<": "<<n - temp1<<endl;
    }
    return 0;
}
