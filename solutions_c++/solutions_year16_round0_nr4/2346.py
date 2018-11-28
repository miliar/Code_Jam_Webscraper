#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    long long int t,k,c,s,i,j,ans,count=1;
    cin>>t;
    //ofstream out;
    //out.open("smallans.out");
    while(t--)
    {
        cin>>k>>c>>s;
        ans=0;
        cout<<"Case #"<<count<<": ";
        count++;
        for(i=1;i<=k;i++)
        {
            ans=i;
            for(j=1;j<c;j++)
            {
                ans=(ans-1)*k+i;
            }
            cout<<" "<<ans;
        }
        cout<<endl;


    }
    return 0;
}
