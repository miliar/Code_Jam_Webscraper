#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t,k,c,s;
    char ch;
    string str;
    cin >> t;
    for(int a0 = 1; a0 <=t; a0++){
        cin>>k>>c>>s;
        cout<<"Case #"<<a0<<": ";
        if(s>=k-1)
            {
            if(k==1)
                {
                cout<<"1 \n";
                continue;
            }
            if(c==1 && k==s)
                {
                for(int i=1; i<=k; i++)
                    {
                    cout<<i<<" ";
                }
            }
            else if(c==1 && k!=s)
                {
                cout<<"IMPOSSIBLE";
            }
            else{
                
                for(int i=2; i<=k; i++)
                    {
                    cout<<i<<" ";
                }
                
            }
        }
        else{
            cout<<"IMPOSSIBLE";
        }
        cout<<"\n";
    }
        
    return 0;
}
