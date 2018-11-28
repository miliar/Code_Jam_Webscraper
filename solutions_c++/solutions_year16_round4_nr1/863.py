#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))

using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

const int INF=0x3f3f3f3f;

int ww(int a, int b) {
    if((a+1)%3==b)return 0;
    return 1;
}
string x(int a) {
    if(a==0)
        return "P";
    if(a==1)
        return "R";
    return "S";
}

vi v;
int n;

string f(int l, int h) {
    if(l>=n)
        return x(h);
    if(h==0) {
        string s1 = f(l+1, 0), s2=f(l+1, 1);
        //cout<<s1<<" " << s2 <<"!\n";
        return min(s1+s2, s2+s1);
    }
    else if(h==1) {
        string s1 = f(l+1, 1), s2=f(l+1, 2);
        return min(s1+s2, s2+s1);
    }
    string s1 = f(l+1, 2), s2=f(l+1, 0);
    return min(s1+s2, s2+s1);
}


int main(void) {
	ios::sync_with_stdio(false);
    int T;cin>>T;
    For(tt, 0, T) {
        cin>>n;
        int seq[] = {1, 0, 2};

        string cm;
        for(int j=0;j<3;j++) {
            int r;cin>>r;
            while(r--) {
                string aa=x(seq[j]);
                cm.pb(aa[0]);
            }
        }
        sort(cm.begin(), cm.end());

        string ans;
        bool ok=0;
        cout<<"Case #"<<tt+1<<": ";
        for(int j=0;j<3;j++) {
            string s = f(0, j);
            string s2 =  s;
            sort(s.begin(), s.end());
            if(s == cm)
                if(ans.size()==0 or ans > s2)
                    ans=s2;
        }
        if(ans.size())
            cout<<ans<<endl;
        else cout<<"IMPOSSIBLE\n";
    }
	
	return 0;
}
