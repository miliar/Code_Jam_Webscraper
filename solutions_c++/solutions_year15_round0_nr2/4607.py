#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
//const int MOD = 1000000007;
const int MOD = 1000003;
int mi;

void myfunction(vector<int>v,int sz,int sum)
{
    if(sum>9)return;
    sort(v.begin(),v.end());
    /*for(int i=0;i<v.size();++i)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl;*/
    if(v[sz-1]<4)
    {
        //cout<<"sz is "<<sz<<"\n";
        sum += v[sz-1];
        mi = min(mi,sum);
        //cout<<"sum is "<<sum<<"\n";
        return;
    }
    int tmp = v[sz-1];
    mi = min(sum+tmp,mi);
    v.push_back(0);
    for(int i=2;i<=tmp/2;++i)
    {
        v[sz-1] = i;
        v[sz] = tmp-i;
        //cout<<"i is "<<i<<" j is "<<tmp-i<<" sz is "<<sz<<"\n";
        myfunction(v,sz+1,sum+1);
    }
    return;
}


int main(int argc, char *argv[]) {
    //ios_base::sync_with_stdio(false);
    freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
    vector<int>v;
    int d,t,val,i,n,ctr,tmp,c=1;
    cin>>t;
    while(t--)
    {
        //cout<<"taking input\n";
        cin>>d;
        mi=0;
        for(i=0;i<d;++i)
        {
            cin>>val;
            v.push_back(val);
            mi = max(mi,val);
        }
        //cout<<"input taken\n";
        n = v.size();
        myfunction(v,n,0);
        v.clear();
        printf("Case #%d: %d\n",c++,mi);
    }
    return 0;
}
