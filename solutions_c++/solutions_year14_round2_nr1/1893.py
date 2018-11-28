#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define fastin std::ios::sync_with_stdio(false);cin.tie(NULL)
#define cout_precision(x) cout<<std::fixed<<setprecision(x)
using namespace std;
#ifdef DEBUG
#include <Debug.h>
#endif
int ans;
bool possible;
void foo(string& a,string& b)
{
    int i=0,j=0;
    if(b.size()<a.size())
        swap(a,b);
    while(i<(int)a.size()&&j<(int)b.size())
    {
        if(a[i]!=b[j])
        {
            if(j>0&&b[j-1]==a[i])
            {
                b.insert(b.begin()+j,a[i]);
            }
            else if(i>0&&a[i-1]==b[j])
            {
                a.insert(a.begin()+i,b[j]);
            }
            else
            {
                possible=false;
                break;
            }
            ans++;
        }
        i++;
        j++;
    }
}
int main()
{
    int t,tc=1,n;
    string a,b;
    cin>>t;
    while(t--)
    {
        cin>>n;
        cin>>a>>b;
        a+='*';
        b+='*';
        ans=0;
        possible=true;
        foo(a,b);
        //debug(a);
        //debug(b);
        if(possible)
            cout<<"Case #"<<tc++<<": "<<ans<<"\n";
        else
            cout<<"Case #"<<tc++<<": "<<"Fegla Won"<<"\n";
    }
}
