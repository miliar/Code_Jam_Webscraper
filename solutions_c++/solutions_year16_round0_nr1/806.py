#include <iostream>
using namespace std;
int main()
{
    int t,tt,n,cnt,i,tmp;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>n;
        if (n==0)
        {
            cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
            continue;
        }
        cnt=0;
        for (i=1;;i++)
        {
            tmp=i*n;
            while (tmp)
            {
                cnt|=(1<<(tmp%10));
                tmp/=10;
            }
            if (cnt==(1<<10)-1) break;
        }
        cout<<"Case #"<<tt<<": "<<i*n<<endl;
    }
    return 0;
}
