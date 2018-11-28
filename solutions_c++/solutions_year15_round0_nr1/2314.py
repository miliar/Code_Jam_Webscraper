#include <iostream>
#include <cstdio>
using namespace std;
int ntest,n;
string s;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    cin>>ntest;
    for (int kk =1 ;kk<=ntest; kk++)
    {
        cin>>n>>s;
        int dem = s[0] - '0';
        int ans = 0;
        for (int i = 1; i<s.size(); i++)
            if (s[i] > '0')
            {
               if (dem < i)
               {
                   ans += (i - dem);
                   dem = i;
               }
               dem+= (s[i] - '0');
            }
        cout<<"Case #"<<kk<<": "<<ans<<"\n";
    }
    return 0;
}
