#include <iostream>
using namespace std;
int main() {
    
 int t,k,c,s;
    int i,j,l;
    cin>>t;
    for(i=0;i<t;i++)
        {
        cin>>k;
        cin>>c;
        cin>>s;
if(k==1)cout<<"Case #"<<i+1<<": 1"<<endl;
else
{
        if(c==1)
            j=1;
        else
            j=2;
        cout<<"Case #"<<i+1<<": ";
        for(l=j;l<=k;l++)
            cout<<l<<" ";
        cout<<endl;
}
    }
    return 0;
}
