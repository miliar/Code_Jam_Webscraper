#include<bits/stdc++.h>
using namespace std;
#define ll long long
vector<int>v;
struct node
{
    vector<int>rep;
    vector<ll>divs;
};
vector< node >ans;
int main()
{
    int N=16;
    for(int i=0; i<(1<<(N-2)); i++)
    {
        int k=i,j=0,c=0;
        v.clear();
        v.push_back(1);
        while(k>0)
        {
            v.push_back(k&1);
            k=k>>1;
            j++;
            c++;
        }
        if((c+2)%3==0)
            continue;
        for(; j<N-2; j++)
            v.push_back(0);
        v.push_back(1);
        reverse(v.begin(),v.end());
        for(j=2; j<=10; j++)
        {
            ll num=0;
            for(k=0; k<N; k++)
                num=(num*j)+v[k];
            ll k;
            for(k=2; k<=sqrt(num); k++)
                if(num%k==0)
                    break;
            ll l=sqrt(num)+1;
            if(k==l)
                break;
        }
        if(j==11)
        {
            //cout<<i<<" "<<ans.size()<<endl;
            node p;
            p.rep=v;
            for(j=2; j<=10; j++)
            {
                ll num=0;
                for(k=0; k<N; k++)
                    num=(num*j)+v[k];
                for(ll k=2; k<=sqrt(num); k++)
                    if(num%k==0)
                    {
                        p.divs.push_back(k);
                        break;
                    }
            }
            ans.push_back(p);
            if(ans.size()==500)
                break;
        }
    }
    freopen("1-out.txt","w",stdout);
    printf("Case #%d:\n",1);
    for(int i=0; i<ans.size(); i++)
    {
        for(int j=0; j<ans[i].rep.size(); j++)
            printf("%d",ans[i].rep[j]);
        for(int j=0; j<ans[i].rep.size(); j++)
            printf("%d",ans[i].rep[j]);
        printf(" ");
        for(int j=0; j<ans[i].divs.size(); j++)
            printf("%d ",ans[i].divs[j]);
        printf("\n");
    }
    return 0;
}
