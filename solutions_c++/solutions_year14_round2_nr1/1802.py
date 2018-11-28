#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <math.h>
#include <map>
#include <utility>
#include <fstream>
using namespace std;

#define mp make_pair
#define pb push_back
#define INF -1
#define MAX 10000007
#define X first
#define Y second
#define all(x) x.begin(),x.end()
#define fi freopen("input.txt","r",stdin);
#define fo freopen("out.txt","w",stdout);
#define REP(i,n) for(int i=0;i<n;i++)
typedef pair<char,int> pii;

int t,n;

int main() {
    fi;
    fo;
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        cout<<"Case #"<<cas<<": ";
        cin>>n;
        string s[105];
        vector <pii> v[105];
        for(int i=0;i<n;i++)
            cin>>s[i];
        for(int i=0;i<n;i++) {
            int cnt=0;
            char ch;
            for(int j=0;j<s[i].size();j++) {
                if(j==0) {
                    ch=s[i][j];
                    cnt++;
                }
                else if(s[i][j]==s[i][j-1])
                    cnt++;
                else {
                    v[i].pb(pii(ch,cnt));
                    cnt=0;
                    ch=s[i][j];
                }
            }
            v[i].pb(pii(ch,cnt));
        }

        bool flag=true;
        for(int i=1;i<n;i++) {
            if(v[i].size()!=v[i-1].size())
                flag=false;
        }
        int ans=0;
        if(flag) {
            for(int i=0;i<v[0].size();i++) {
                int maxi=v[0][i].Y,mini=v[0][i].Y;
                char ch=v[0][i].X;
                for(int j=1;j<n;j++) {
                    if(v[j][i].X!=ch) {
                        flag=false;
                        break;
                    }
                    maxi=max(maxi,v[j][i].Y);
                    mini=min(mini,v[j][i].Y);
                }
                if(!flag)
                    break;
                ans=ans+maxi-mini;
            }
        }
        if(!flag)
            cout<<"Fegla Won\n";
        else
            cout<<ans<<"\n";
    }
}

