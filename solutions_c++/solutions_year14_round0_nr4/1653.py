#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("Inp3.txt","r",stdin);
    //freopen("Output3.txt","w",stdout);
    int t,n,ans,ke_id,ans2,test=1;
    cin>>t;
    vector<double>naomi,ken;
    double x;
    while(t--)
    {
        naomi.clear();
        ken.clear();
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>x;
            naomi.push_back(x);
        }
        for(int i=0;i<n;i++)
        {
            cin>>x;
            ken.push_back(x);
        }
        ans=0;
        ke_id=0;
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());

        ans2=0;
        for(int i=0;i<n;i++)
        {
            for(;ke_id<n;ke_id++)
            {
                if(naomi[i]<ken[ke_id])
                {
                    ans2++;
                    ke_id++;
                    break;
                }
            }
        }
        ans2 = n-ans2;

        while(1)
        {
            int flag=0;
            for(int i=0;i<naomi.size();i++)
            {
                if(naomi[i]<ken[i])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
            {
               ans++;
               naomi.erase(naomi.begin());
               ken.erase(ken.end()-1);
            }
            else break;
        }
        ans=n-ans;
        printf("Case #%d: %d %d\n",test++,ans,ans2);
    }
    return 0;
}
