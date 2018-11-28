#include <bits/stdc++.h>
using namespace std;
int test;

bool b[12][(1<<12)+5][(1<<12)+5];


void sol(){
    int n,a,b,c;
    cin>>n>>b>>a>>c;
    vector <pair <char,string> >  v;
    for (int i=0;i<a;i++) v.push_back({'P',"P"});
    for (int i=0;i<b;i++) v.push_back({'R',"R"});
    for (int i=0;i<c;i++) v.push_back({'S',"S"});
    while (a+b+c>1){
        int A=(a+b-c)/2;
        int B=(b+c-a)/2;
        int C=(c+a-b)/2;
        a=A;
        b=B;
        c=C;
        if (A<0 || B<0 || C<0) {
            cout<<"Case #"<<++test<<": "<<"IMPOSSIBLE"<<endl;
            return;
        }
        sort(v.begin(),v.end());
        vector <pair <char,string> > vv;
        for (int i=0;i<A;i++)
        {
            string s,ss;
            for (int j=0;j<v.size();j++)
            if (v[j].first=='P') {
                s=v[j].second;
                v[j].first='#';
                break;
            }
            for (int j=0;j<v.size();j++)
            if (v[j].first=='R') {
                ss=v[j].second;
                v[j].first='#';
                break;
            }
            if (s>ss) swap(s,ss);
            vv.push_back({'P',s+ss});
        }
        for (int i=0;i<C;i++)
        {
            string s,ss;
            for (int j=0;j<v.size();j++)
            if (v[j].first=='P') {
                s=v[j].second;
                v[j].first='#';
                break;
            }
            for (int j=0;j<v.size();j++)
            if (v[j].first=='S') {
                ss=v[j].second;
                v[j].first='#';
                break;
            }
            if (s>ss) swap(s,ss);
            vv.push_back({'S',s+ss});
        }
        for (int i=0;i<B;i++)
        {
            string s,ss;
            for (int j=0;j<v.size();j++)
            if (v[j].first=='R') {
                s=v[j].second;
                v[j].first='#';
                break;
            }
            for (int j=0;j<v.size();j++)
            if (v[j].first=='S') {
                ss=v[j].second;
                v[j].first='#';
                break;
            }
            if (s>ss) swap(s,ss);
            vv.push_back({'R',s+ss});
        }
        v=vv;
    }
    cout<<"Case #"<<++test<<": "<<v[0].second<<endl;
}

int main() {
    freopen("AL.in","r",stdin);
    freopen("AL.txt","w",stdout);
    int t;
    cin>>t;
    while (t--){
        sol();
    }
    return 0;
}
