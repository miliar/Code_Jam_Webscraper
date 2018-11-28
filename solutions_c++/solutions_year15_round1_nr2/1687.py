#include<bits/stdc++.h>
using namespace std;
struct bb {
    long long tt,ii;
    bb() {}
    bb(long long _tt,long long _ii) {
        tt=_tt,ii=_ii;
    }
    bool operator<(const bb&p)const {
        return (tt>p.tt || (tt==p.tt && ii>p.ii));
    }
};
int main() {
    // freopen("B-small-attempt0.in","r",stdin);
    // freopen("B-small-attempt0.out","w",stdout);
    int t;
    cin>>t;
    for(int z=1; z<=t; z++) {
        int b,n,x,y=-1,mx=1,gcd;
        cin>>b>>n;
        priority_queue<bb>q;
        long long int m[b+1];
        vector<int>v;
        for(int i=0; i<b; i++) {
            cin>>x;
            q.push(bb(x,i+1));
            v.push_back(i+1);
            m[i+1]=x;
            mx=(mx*x)/(__gcd(mx,x));
        }
        int ii=0;
        while(ii<=mx) {
            bb w=q.top();
            //cout<<w.ii<<endl;
            q.pop();
            v.push_back(w.ii);
            w.tt+=m[w.ii];
            q.push(w);
            ii=w.tt;//-m[w.ii];
            /*while(q.top().tt==mx) {
                //cout<<"ok\n";
                v.push_back(q.top().ii);
                bb r=q.top();
                q.pop();
                r.tt+=m[r.ii];
                q.push(r);
            }*/
        }
        v.pop_back();
        int sz=v.size();
        /*cout<<sz<<endl;
        for(int i=0;i<sz;i++){
            cout<<v[i]<<" ";
        }cout<<endl;*/
        n--;
        n%=sz;
        cout<<"Case #"<<z<<": "<<v[n]<<"\n";
    }
    return 0;
}

