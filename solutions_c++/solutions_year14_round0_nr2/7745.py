#include<iostream>
using namespace std;
int main()
{
    int t,n=0;
    long double c,f,x,r,ans;
    cout.precision(20);
    cin>>t;
    while(t--)
    {
        r=2.0;
        ans=0;
        cin>>c>>f>>x;
        while((x-c)/r>x/(r+f))
        {
            ans+=c/r;
            r+=f;
        }
        ans+=x/r;
        cout<<"Case #"<<++n<<": "<<ans<<endl;
    }
    return 0;
}
