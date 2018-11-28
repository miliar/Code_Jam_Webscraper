#include <bits/stdc++.h>
#define gc getchar//_unlocked
typedef long long ll;
void sct(long long int &x)
{
    register long long int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

using namespace std;

int main() {

	//freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

    ll t,q=1;
    cin>>t;;
    while(t--)
    {
        ll x,i,m=0,cur_count=0,p,z;
        cin>>x;;
        string s;
        cin>>s;

        p = ((int)s[0]);
            cur_count = p-48;
          // cout<<cur_count<<" ";
        for(i=1;i<s.size();i++)
        {
            p = ((int)s[i]) - 48;

            if(cur_count >= i)
            {
             if(p>0) cur_count += p;
            }
            else if(p > 0)
            {
                z = (i-cur_count);//cout<<z<<" "<<i<<" ";
                cur_count += (z+p);
                m += z;
            }
        }
        cout<<"Case #"<<q<<": "<<m<<"\n";
        q++;
    }
   return 0;
}
