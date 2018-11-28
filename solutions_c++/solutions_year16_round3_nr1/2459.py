#include<bits/stdc++.h>
#define scd(x) scanf("%d",&x)
#define prd(x) printf("%d",x)
#define sclld(x) scanf("%lld",&x)
#define prlld(x) printf("%lld",x)
#define f_in(x) freopen(x,"r",stdin)
#define f_out(x) freopen(x,"w",stdout)

using namespace std;

typedef long long int llt;
class cmp
{
    public :bool operator()(pair<int,int> &a , pair<int,int> &b)
    {
        if(a.first < b.first)
            return true;
        else
            return false;
    };
};

int main()
{
    ios::sync_with_stdio(false);
    //f_in("input.txt");
    //f_out("output.txt");
     int T,n;
     char ch;
     priority_queue< pair<int,int> ,vector< pair<int,int> >, cmp > pq;
     vector< string > v;
    cin>>T;
    string s;
    for(int t = 1 ; t<=T ; t++)
    {
        cin>>n;
        for(int i = 0 ; i < n ; i++)
        {
            int x;
            cin>>x;
            if(x>0)
                pq.push(make_pair(x,i));
        }
                cout<<"Case #"<<t<<": ";

        while(!pq.empty())
        {
            auto a = pq.top();
            //cout<<"\nPopped "<<a.second<<"\t"<<a.first<<"\n";
            pq.pop();
            if(!pq.empty() && pq.top().first==a.first)
            {
                auto b = pq.top();
                pq.pop();
              //  cout<<"Popped "<<b.second<<"\t"<<b.first<<"\n";
                s.push_back('A'+a.second);
                s.push_back('A'+b.second);
                a.first--;
                b.first--;
                if(a.first >0)
                    pq.push(a);
                if(b.first > 0)
                    pq.push(b);
            }
            else
            {
                ch='A'+a.second;
                if(a.first > 1)
                {
                    s.push_back(ch);
                    s.push_back(ch);
                    a.first-=2;
                }
                else
                {
                    s.push_back(ch);
                    a.first--;
                }
                if(a.first > 0)
                    pq.push(a);
            }
            v.push_back(s);
            s.clear();
        }

        int len = v.size();
        int j=0;
        for(j = 0 ; j < len - 2 ; j++ )
            cout<<v[j]<<" ";
        if(len >=2)
        {
            if(v[len-1].length()==1)
                cout<<v[len-1]<<" "<<v[len-2];
            else
                cout<<v[len-2]<<" "<<v[len-1];
        }
        else
            cout<<v[len-1];
        cout<<"\n";
        v.clear();
    }

    return 0;
}
