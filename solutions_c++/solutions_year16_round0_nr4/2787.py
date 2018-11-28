
#include <iostream>

using namespace std;

int main()
{
    int n=0,k=0,c=0,s=0;
    cin>>n;
    for(int x=0;x<n;x++)
    {
        cin>>k;
        cin>>c;
        cin>>s;
        cout<<"Case #"<<x+1<<": ";
        for(int j=1;j<=s;j++)
        	cout<<j<<" ";
        cout<<"\n";
    }
    return 0;
}


