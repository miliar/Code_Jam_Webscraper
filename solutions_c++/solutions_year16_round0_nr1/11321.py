#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("result.out", "wt", stdout);
    int t,n;
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        cin>>n;
        cout<<"Case #"<<cas<<": ";
        if(n==0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int bit = (1<<18);
        int i=0;
        while(bit < 263167){
            i++;
            int k = n*i;
            while(k>0){
                int x = k%10;
                k/=10;
                bit |= (1<<x);
            }
        }
        cout<<n*i<<endl;
    }
    return 0;
}