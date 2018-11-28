#include<iostream>
using namespace std;

int main()
{
    int t,i,n,m[1001],max_diff=0,y,z;
    for(i=1,cin>>t; i<=t; i++)
    {
        cin>>n; cin>>m[0]; max_diff=0; y=0; z=0;
        for(int j=1;j<n;j++)
        {
            cin>>m[j];
            if(m[j-1]>m[j])
            {
                y+=m[j-1]-m[j];
                if(max_diff<(m[j-1]-m[j])) max_diff=m[j-1]-m[j];
            }
        }
        for(int j=0;j<n-1;j++) z+=(m[j]>max_diff)? max_diff : m[j];
        cout<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
    }
}
