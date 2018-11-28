#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int t,tt,k,c,s,i,st,inc,pos;
    long long tmp;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<tt<<":";
        if (s*c<k) cout<<" IMPOSSIBLE"<<endl;
        else
        {
            if (c>k)
            {
                tmp=1;
                for (inc=1;inc<=k;inc++) tmp=(tmp-1)*k+inc;
                cout<<" "<<tmp;
            }
            else
            {
                if (k%c==0) s=k/c;
                else s=k/c+1;
                for (i=0;i<s;i++)
                {
                    st=i*c+1;
                    if (st+c>k) st=k-c+1;
                    tmp=1;
                    for (inc=0;inc<c;inc++)
                    {
                        pos=st+inc;
                        tmp=(tmp-1)*k+pos;
                    }
                    cout<<" "<<tmp;
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
