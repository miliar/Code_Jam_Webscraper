#include <fstream>
#include <cmath>
using namespace std;
bool stug(int x)
{
    int q[100], w=0, i;
    while(x!=0)
    {
        q[w]=x%10;
        w++;
        x=x/10;
    }
    for(i=0; i<w/2; ++i)
    {
        if(q[i]!=q[w-i-1])
        {
            return false;
        }
    }
    return true;
}
int main()
{
    long long a, b, o;
    long long i, t, k, ans=0;
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin>>t;
    for(k=0; k<t; ++k)
    {
        ans=0;
        cin>>a>>b;
        o=sqrt(a);
        if(o*o==a) a=o;
        else a=o+1;
        b=sqrt(b);
        for(i=a; i<=b; ++i)
        {
            if(stug(i) && stug(i*i)) ans++;
        }
        cout<<"Case #"<<k+1<<": "<<ans<<endl;
    }
    return 0;
}
