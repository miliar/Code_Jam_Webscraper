#include<bits/stdc++.h>

using namespace std;



struct hiker{
    long long d,m;
    hiker(long long dd,long long mm):d(dd),m(mm){}
};

void solve(){
    int n;
    cin >> n ;
    vector<hiker> h;
    long long best = 0;
    for(int i = 0 ; i < n ; ++ i ){
        int d,hh,m;
        cin >> d >> hh >> m;
        best+=hh;
        for(int k = 0 ; k < hh ; ++ k ){
            h.push_back(hiker(d,m+k));
        }
    }
    if(best==1){
        cout << 0 << endl;
        return ;
    }
    best=2;
    hiker h1=h[0];
    hiker h2=h[1];
    if(h1.d>h2.d)swap(h1,h2);
    if(h1.d==h2.d&&h1.m<h2.m)swap(h1,h2);
    if(h1.m==h2.m){
        best=0;
    }
    else if(h1.m<h2.m){
        best=1;
        if(h2.m*(360-h2.d)<h1.m*360+h1.m*(360-h1.d))best=0;
    }
    else{
        best=1;
        if(h2.m*360+ h2.m*(360-h2.d)>h1.m*(360-h1.d))best=0;
        //if(h2.m*360+ h2.m*(360-h2.d)==h1.m*(360-h1.d))best=2;

    }

    cout << best << endl;
}

int main(){
    freopen("C-small-1-attempt7"".in","r",stdin);
    freopen("C-small-1-attempt7"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i){
        printf("Case #%d: ",i);
    solve();
    }
}
