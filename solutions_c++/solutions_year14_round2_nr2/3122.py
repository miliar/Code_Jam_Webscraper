#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#define ll long long int
using namespace std;
int main()
{
    int t;
    cin>>t;
    for (int s=0; s<t; s++){
    int a,b,k;
    cin>>a>>b>>k;
    int count=0;
    for (int i=0; i<a; i++)
    {
        for (int j=0; j<b; j++)
        {
            int r=(i&j);
            if (r<k)
            {
                count+=1;
               // cout<<i<<" "<<j<<endl;
            }
        }
    }
    cout<<"Case #"<<s+1<<": "<<count<<endl;}
}
