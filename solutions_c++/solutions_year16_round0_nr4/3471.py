#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int ii = 1; ii<=t; ii++)
    {
        cout<<"Case #"<<ii<<": ";
        int k, c, s;
        cin>>k>>c>>s;
        
        for(int i = 1; i <= k; i++)
            cout<<i<<' ';
        
        cout<<"\n";
    }
    return 0;
}