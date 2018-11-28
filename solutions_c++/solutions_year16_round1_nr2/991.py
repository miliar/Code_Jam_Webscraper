#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
    int t,tt,n,i,j,s,cnt[3000];
    vector<int> sol;
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>n;
        memset(cnt,0,sizeof(cnt));
        for (i=0;i<2*n-1;i++)
            for (j=0;j<n;j++)
            {
                cin>>s;
                cnt[s]++;
            }
        sol.clear();
        for (i=1;i<=2500;i++) if (cnt[i]&1) sol.push_back(i);
        cout<<"Case #"<<tt<<":";
        for (i=0;i<n;i++) cout<<" "<<sol[i];
        cout<<endl;
    }
    return 0;
}
