#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<unordered_set>
#include<sstream>


using namespace std;

int t;
int n;
int ans;
int baseans;

string s;

vector<string> w[30];
bool eng[30];
unordered_set<string> baseen;
unordered_set<string> basefr;
unordered_set<string> en;
unordered_set<string> fr;

void brute(int x) {
    if(x==n) {

        int tans=baseans;
        for(unordered_set<string>::iterator it = en.begin();it!=en.end();it++) {
            if(fr.find(*it)!=fr.end() ) {
                tans++;
            } else {
                if(basefr.find(*it)!=basefr.end()) {
                    tans++;
                }
            }
        }
        for(unordered_set<string>::iterator it = fr.begin();it!=fr.end();it++) {
            if(en.find(*it)==en.end() && baseen.find(*it)!=baseen.end() ) {
                tans++;
            }
        }

        if(tans<ans) ans=tans;
    }
    else {
        eng[x]=false;
        unordered_set<string> added;
        for(int j=0;j<w[x].size();j++) {
            if(basefr.find(w[x][j])==basefr.end()&&fr.find(w[x][j])==fr.end()) {
                added.insert(w[x][j]);
            }
        }
        fr.insert(added.begin(),added.end());
        brute(x+1);
        for(unordered_set<string>::iterator it = added.begin();it!=added.end();it++) {
            fr.erase(*it);
        }
        added.clear();
        eng[x]=true;
        for(int j=0;j<w[x].size();j++) {
            if(baseen.find(w[x][j])==baseen.end()&&en.find(w[x][j])==en.end()) {
                added.insert(w[x][j]);
            }
        }
        en.insert(added.begin(),added.end());
        brute(x+1);
        for(unordered_set<string>::iterator it = added.begin();it!=added.end();it++) {
            en.erase(*it);
        }
    }
}

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    cin>>t;
    for(int cases=0;cases<t;cases++) {
        cin>>n;
        cin.ignore();
        ans=0;
        for(int i=0;i<n;i++) {
            getline(cin,s);
            string buf;
            stringstream ss(s);
            while(ss>>buf) {
                w[i].push_back(buf);
                ans++;
            }
        }
        eng[0]=true;
        eng[1]=false;
        baseen.insert(w[0].begin(), w[0].end());
        basefr.insert(w[1].begin(), w[1].end());
        baseans=0;
        for(unordered_set<string>::iterator it = baseen.begin();it!=baseen.end();it++) {
            if(basefr.find(*it)!=basefr.end()) baseans++;
        }
        brute(2);
        for(int i=0;i<n;i++) w[i].clear();
        baseen.clear();
        basefr.clear();
        en.clear();
        fr.clear();
        cout<<"Case #"<<cases+1<<": "<<ans<<endl;

    }
}
