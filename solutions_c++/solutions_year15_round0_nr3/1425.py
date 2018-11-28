#include <bits/stdc++.h>
#define reset(arr,j) memset(arr,j,sizeof(arr));
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define LL long long
#define fa(i,n) for(int i=0;i<n;i++)
#define take(vec,n) vector<int> vec; for(int i=0;i<n;i++){int a; cin >> a; vec.pb(a);};
#define print(arr,n) fa(i,n) cout << arr[i] << " "; cout << endl;
#define fd(i,n) for(int i=n-1;i>=0;i--)
#define vpair vector < pair <int ,int> >
#define Vec(name,size) vector<int> name(size);
#define matrix vector<vector<LL> >
#define initmatrix(m,a,b,x) fa(i,a){ vector<LL> c; m.pb(c); fa(j,b) m[i].pb(x);};
#define printmatrix(M) fa(i,M.size()){ fa(j,M[i].size()) cout << M[i][j].f <<" "; cout << endl;}
int dx[] = {0,1,-1,0,1,-1,1,-1,-2,2,0,0},dy[] = {1,0,0,-1,-1,1,1,-1,0,0,-2,2};
using namespace std;
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
bool isneg(char x){
    if(x == '-' || x == 'I' || x == 'J' || x == 'K')
        return 1;
    return 0;
}
char neg(char x){
    if(x == '1')
        return '-';
    if(x == '-')
        return '1';
    if(x == 'i' || x =='j' || x == 'k') return toupper(x);

    return tolower(x);
}
char mul(char a,char b){
    bool ng = isneg(a) ^ isneg(b);
    if(isneg(a))
        a = neg(a);
    if(isneg(b))
        b = neg(b);
    if(a == '1'){
        if(ng)
            return neg(b);
        return b;
    }
    if(b == '1'){
        if(ng)
            return neg(a);
        return a;
    }
    if(a == '1' && b == '1'){
        if(ng)
            return '-';
        return '1';
    }
    if(a == 'i' && b == 'j'){
        if(ng)
            return neg('k');
        return 'k';
    }
    if(a == 'i' && b == 'k'){
        if(ng)
            return 'j';
        return neg('j');
    }
    if(a == 'j' && b == 'k'){
        if(ng)
            return neg('i');
        return 'i';
    }
    if(a == 'j' && b == 'i'){
        if(ng)
            return 'k';
        return neg('k');
    }
    if(a == 'k' && b == 'i'){
        if(ng)
            return neg('j');
        return 'j';
    }
    if(a == 'k' && b == 'j'){
        if(ng)
            return 'i';
        return neg('i');
    }
    if(a == b){
        if(ng)
            return '1';
        return '-';
    }
}
main(){
    freopen("input.in","r",stdin);
    freopen("out.in","w",stdout);
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        LL L,X;
        cin >> L >> X;
        string s,temp;
        cin >> temp;
        fa(i,X)
            s+= temp;
        int n = s.size();
        char pref[10004],suff[10004];
        pref[0] = s[0];
        suff[s.size()-1] = s[s.size()-1];
        for(int i = 1;i < s.size();i++)
            pref[i] = mul(pref[i-1],s[i]);
        for(int i = s.size()-2;i>= 0;i--)
            suff[i] = mul(s[i],suff[i+1]);
//        fa(i,n)
//            cout << pref[i] << " ";
//        cout << endl;
//        fa(i,n)
//            cout << suff[i] << " ";
//        cout << endl;
        bool I = 0,K = 0;
        fa(i,n){
            if(pref[i]=='i'){
                I = 1;
                i++;
            }
            if(I && suff[i]=='k')
                K = 1;
        }
        if(pref[n-1]=='-' && K){
            printf("Case #%d: YES\n",t);
        }
        else
            printf("Case #%d: NO\n",t);
    }
}
