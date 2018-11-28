#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int key[400];
int a[400],ans[400];
bool c[400],rm[400];
int up;
vector<int> b[400];
int n,cs,cc,k,x;
int idx;
int ck[50];
bool check() {
    memset(ck,0,sizeof(ck));
    for (int i=0;i<50;++i) ck[i]+=key[i];
    for (int i=0;i<n;++i)
    if (!c[i]) {
        ck[a[i]]--;
        for (int j=0;j<b[i].size();++j)
            ck[b[i][j]]++;
    }
    for (int i=0;i<50;++i) if (ck[i]<0) return false;
    return true;
}
bool dfs(int d) {
    if (d==n)
        return true;
//    cout<<endl;
//    for (int i=0;i<20;++i) cout<<key[i]<<' ';
//    cout<<endl;
//    for (int i=0;i<n;++i) cout<<c[i]<<' ';
//    cout<<check()<<endl;
    if (!check()) return false;
    for (int i=0;i<n;++i)
    if (!c[i] && key[a[i]]>0) {
        c[i] = true, key[a[i]]--;
        for (int j=0;j<b[i].size();++j) key[b[i][j]]++;
        ans[d]= i;
        if (dfs(d+1))
            return true;
        for (int j=0;j<b[i].size();++j) key[b[i][j]]--;
        c[i] = false, key[a[i]]++;
        if (rm[i]) return false;
    }

    return false;
}

int main() {
    freopen("p5.in","r",stdin);
    freopen("p5.out","w",stdout);
	cin>>cs;
	cc = cs;
	while (cs-->0) {
	    memset(key,0,sizeof(key));
        memset(c,0,sizeof(c));
        memset(rm,0,sizeof(rm));
        idx = 0;

		cin>>k>>n;
		cout<<"Case #"<<cc-cs<<":";
		for (int i=0;i<k;++i) {
            cin>>x;
            key[x]++;
		}
	//	cout<<key[13]<<endl;
        for (int i=0;i<n;++i) {
            cin>>a[i];
            cin>> up;
            b[i].clear();
            while (up-->0) {
                cin>>x;
                if (x==a[i])
                    rm[i] = true;
                b[i].push_back(x);
            }
           // cout<<rm<<":"<<endl;
        //   cout<<key[13]<<endl;
//            if (rm) {
//                c[i] = true;
//                for (int j=0;j<b[i].size();++j) {
//                    key[b[i][j]]++;
//                }
//                key[a[i]]--;
//                ans[idx++] = i;
//            }
        }

        if (dfs(idx)) {
            for (int i=0;i<n;++i) cout<<" "<<ans[i]+1;
            cout<<endl;
        } else {
            cout<<" IMPOSSIBLE"<<endl;
        }
	}
	return 0;
}
