#include <bits/stdc++.h>

using namespace std;

int n, le, mosta, mostb, ea, eb,ki;
bool sz[26][26], volt[26], volt2[26];
vector<pair<int,int>> v1,v2;
void bejar2(int a);
void bejar(int a) {
    volt[a]=true;
    mosta++;
    for(int i=0;i<n;i++) {
        if(sz[a][i] && !volt2[i]) bejar2(i);
    }
}
void bejar2(int a) {
    volt2[a]=true;
    mostb++;
    for(int i=0;i<n;i++) {
        if(sz[i][a] && !volt[i]) bejar(i);
    }
}

int befejez(vector<pair<int,int>>& v1,vector<pair<int,int>>& v2) {
    int ki=0, h=0;
    for(int i=0;i<v1.size();i++) {
        ki+=v1[i].second*v1[i].second;
        h+=v1[i].second-v1[i].first;
    }
    for(int i=0;i<v2.size();i++) {
        ki+=v2[i].first*v2[i].first;
    }
    if(h>ea) return n*n;
    return ki+ea-h;
}

int megold(vector<pair<int,int>> v1,vector<pair<int,int>> v2);
int fuzio(vector<pair<int,int>> v1,vector<pair<int,int>> v2, int i) {
    pair<int,int> a=v1[v1.size()-1], b=v2[i], c=make_pair(a.first+b.first,a.second+b.second);
    v1.resize(v1.size()-1);
    for(int j=i;j<v2.size()-1;j++) {
        v2[j]=v2[j+1];
    }
    v2.resize(v2.size()-1);
    int ki=0;
    if(c.first<c.second) v1.push_back(c);
    if(c.first>c.second) v2.push_back(c);
    if(c.first==c.second) ki=c.first*c.first;
    return ki+megold(v1,v2);
}

int megold(vector<pair<int,int>> v1,vector<pair<int,int>> v2) {
    int ki=befejez(v1,v2);
    if(!v1.empty() && !v2.empty()){
        sort(v2.begin(),v2.end());
        for(int i=0;i<v2.size();i++) {
            if(i>0 && v2[i]==v2[i-1]) continue;
            int a=fuzio(v1,v2,i);
            if(a<ki) ki=a;
        }
    }
    return ki;
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("out.txt","w",stdout);
    int q;
    cin >> q;
    for(int x=0;x<q;x++) {
        cin >> n;
        le=0;
        char c;
        v1.clear();
        v2.clear();
        ea=0;
        eb=0;
        for(int i=0;i<n;i++) {
            volt[i]=volt2[i]=false;
            for(int j=0;j<n;j++) {
                cin >> c;
                if(c=='1') {
                    sz[i][j]=true;
                    le++;
                } else sz[i][j]=false;
            }
        }
        for(int i=0;i<n;i++) {
            mosta=mostb=0;
            if(!volt[i]) {
                bejar(i);
                if(mostb==0) ea++;
                else if(mosta==0) eb++;
                else if(mosta<mostb) v1.push_back(make_pair(mosta,mostb));
                else if(mostb<mosta) v2.push_back(make_pair(mosta,mostb));
                else le-=mosta*mostb;
                //cout << mosta << "*" << mostb << endl;
            }
        }
        for(int i=0;i<n;i++) {
            mosta=mostb=0;
            if(!volt2[i]) {
                bejar2(i);
                if(mostb==0) ea++;
                else if(mosta==0) eb++;
                else if(mosta<mostb) v1.push_back(make_pair(mosta,mostb));
                else if(mostb<mosta) v2.push_back(make_pair(mosta,mostb));
                else le-=mosta*mostb;
                //cout << mosta << "*" << mostb << endl;
            }
        }
        int ki=megold(v1,v2);
        cout << "CASE #" << x+1 << ": ";
        cout << ki-le << endl;

    }
    return 0;
}
