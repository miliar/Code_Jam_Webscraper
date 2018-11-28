#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
   freopen("A-large.in","r",stdin);
   freopen("output1.out","w",stdout);

    int t;
    cin>>t;
    for(int i=1 ; i<=t ; i++){
        string s;
        int n;
        cin>>n;
        cin>>s;
        int test=s[0]-48,friends=0;
        for(int l=1; l<n+1 ; l++){
            if( l > test ){
                friends+=l-test;
                 test++;
            }
            test+=s[l]-48;
        }
        cout<<"Case #"<<i<<": "<<friends<<endl;
        friends=0;
    }

    return 0;
}
