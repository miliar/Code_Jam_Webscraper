#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("output.out","w",stdout);
    int t;
    cin>>t;
    int cases=0;
    while(cases<t){
        cases++;
        int n;
        int foundSoFar=0;
        int i=1;
        cin>>n;
        if(n==0){
            cout<<"Case #"<<cases<<": INSOMNIA\n";
            continue;
        }
        while(foundSoFar!=(1<<10)-1){
            int temp=n;
            while(temp!=0){
                int chiff=temp%10;
                temp/=10;
                foundSoFar=foundSoFar|(1<<chiff);
            }
            n=n/i;
            i++;
            n=n*i;
        }
        n/=i;
        i--;
        n*=i;
        cout<<"Case #"<<cases<<": "<<n;
        if(cases!=t)cout<<"\n";
    }
    return 0;
}
