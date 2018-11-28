#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main ()
{
    freopen("B-large.in","r",stdin);   
    freopen("Bl.txt","w",stdout);
    
    int T;
    cin>>T;
    int ans;
    string pancakes;
    
    getline (cin, pancakes);
    for (int t=1;t<=T;++t)
    {
            ans = 0;
            getline (cin, pancakes);
            
            char cur = pancakes[0];
            for (int i=1;i<pancakes.length();++i)
            {
             if (cur!=pancakes[i])
             {
                cur = pancakes[i];
                ans++;                     
             }    
            }
            if (cur!='+')
               ans++;
            cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
    return 0;   
}
