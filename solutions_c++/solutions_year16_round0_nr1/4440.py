#include<bits/stdc++.h>
using namespace std;
bool b[10];
int ans;
void ok(int k)
{
    if(k)
    {
        if(!b[k%10])
            b[k%10]=1,
            ans++;
        ok(k/10);
    }
}
int main()
{
	freopen("1.out","w",stdout);
	freopen("1.in","r",stdin);
    int t;
    cin>>t;
    for(int _=0;_<t;_++)
    {
        for(int i=0;i<10;i++)
            b[i]=0;
        ans=0;
        int n;
        cin>>n;
        cout<<"Case #"<<_+1<<": ";
        if(!n)
            cout<<"INSOMNIA\n";
        else
            for(int i=1;;i++)
            {
                ok(i*n);
                if(ans==10)
                {
                    cout<<i*n<<"\n";
                    break;
                }
            }
    }
}
