#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    
    int t;
    cin>>t;
    
    for(int x=1; x<=t; x++)
    {
        int k, c, s;
        cin>>k>>c>>s;
        
        cout<<"Case #"<<x<<": ";
        for(int i=1; i<=s; i++)
            cout<<i<<" ";
        cout<<"\n";
    }
    
    
    return 0;
}
