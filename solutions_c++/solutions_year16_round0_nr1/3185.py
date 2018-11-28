#include <iostream>
#include <cstdlib>
#include <set>
#include <cstdio>
using namespace std;

set<int>s;

void spiltNumber(int n){
    while(n!=0){
        s.insert(n%10);
        n /= 10;
    }
}

int main()
{
    unsigned int t,n;
    //freopen("in.txt","r", stdin);
    //freopen("out.txt", "w+", stdout);
    cin>>t;
    for(int i=1; i<=t; i++){
        cin>>n;

        if(n==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else{
            int counter = 1;
            while(s.size()!= 10)
                spiltNumber(n*counter++);

            --counter;
            cout<<"Case #"<<i<<": "<<n*counter<<endl;
            s.clear();
        }
    }

    return 0;
}