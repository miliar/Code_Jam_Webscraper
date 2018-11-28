#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;
int ans;
vector<string> a;
bool v[101];
int d[101];
int n;
bool test(){
    char s[10001];
    bool v[27];
    memset(v,0,sizeof(v));
    int p=0;
    for (int i=0;i<n;i++){
        strcpy(s+p,a[d[i]].c_str());
        p+=a[d[i]].length();
    }
    //cout << "original: " << s << endl;
    char last=s[0];
    v[s[0]-'a']=true;
    for (int i=1;i<p;i++)
        if (s[i]!=last){
            if (v[s[i]-'a']){
                //cout << "i=" <<i<<"false!\n";
                return false;
            } else
                v[s[i]-'a']=true;
            last=s[i];
        }
    //cout << "true!\n";
    return true;
}
void dfs(int now){
    if (now==n)
        if (test())
            ans=(ans+1)%1000000007;
    if (now>=n) return;
    for (int i=0;i<n;i++)
        if (!v[i]){
            v[i]=true;
            d[now]=i;
            dfs(now+1);
            v[i]=false;
        }
}
int main(){
    int t;
    cin >> t;
    for (int ti=1;ti<=t;ti++){
        a.clear();
        ans=0;
        string s;
        cin >> n;
        for (int i=0;i<n;i++){
            cin >> s;
            a.push_back(s);
        }
        memset(v,0,sizeof(v));
        dfs(0);
        cout << "Case #" << ti << ": " << ans << endl;
    }
    return 0;
}
