#include<bits/stdc++.h>
#define scd(x) scanf("%d",&x)
#define prd(x) printf("%d",x)
#define sclld(x) scanf("%lld",&x)
#define prlld(x) printf("%lld",x)
#define f_in(x) freopen(x,"r",stdin)
#define f_out(x) freopen(x,"w",stdout)

using namespace std;

typedef long long int llt;

vector<int> lazy;

void update(int ss,int se,int index,int l,int r)
{
    if(l>se || r < ss) //completely outside the range
        return ;
    if(l<=ss && r>=se) //completely inside the range
    {
        lazy[index]+=1;
        return;
    }
    int mid = (ss+se)/2;
    update(ss,mid,2*index+1,l,r);
    update(mid+1,se,2*index+2,l,r);
}

int query(int ss,int se,int index,int l,int r)
{
    if(ss!=se && lazy[index] != 0)
    {
        lazy[2*index+1] += lazy[index];
        lazy[2*index+2] += lazy[index];
        lazy[index] = 0;
    }

    if(l>se || r < ss) //completely outside the range
        return 0;
    if(l<=ss && r>=se) //completely inside the range
    {
        return lazy[index];
    }
    int mid = (ss+se)/2;
    return query(ss,mid,2*index+1,l,r) +
            query(mid+1,se,2*index+2,l,r);
}

int main()
{
    ios::sync_with_stdio(false);
    int t,len,ans;
    //f_in("in2.txt");
    //f_out("out2.txt");
    string s;
    cin>>t;
    for(int j = 1 ; j<= t ; j++)
    {
        cin>>s;
        ans=0;
        cout<<"Case #"<<j<<": ";
        len = s.length();
        lazy.assign(4*len,0);
        for(int i= 0 ; i< len ; i++)
        {
            if(s[i]=='-')
                update(0,len-1,0,i,i);
        }

        for(int i = len-1; i>=0 ; i--)
        {
            if(query(0,len-1,0,i,i) & 1)
            {
                ans++;
                update(0,len-1,0,0,i);
            }
        }
        cout<<ans;
        cout<<"\n";

        s.clear();
        lazy.clear();
    }

    return 0;
}
