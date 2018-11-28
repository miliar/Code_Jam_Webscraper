#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
#define DEBUG(x) {cout<< #x <<" = " << x <<endl;}

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    ios::sync_with_stdio(false);
    int test;
    cin>>test;
    int test_case = 1 ;
    while (test--){
        string s;
        cin>>s;
        string st  = "";
        st +=s[0];
        for(int i = 1; i < s.length(); ++i){
            if (st[st.size()-1] != s[i])
                st+=s[i];
        }
        //cout<<st<<endl;
        int res=0;
        if (st[st.size()-1] == '-')
            res = st.size();
        else
            res = st.size() - 1;

        cout<< "Case " << "#" << test_case << ": "<< res << endl;
        test_case++;
    }

    return 0;
}
