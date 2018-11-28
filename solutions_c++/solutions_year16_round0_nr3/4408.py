#include <bits/stdc++.h>
#define Max 100005
#define ll long long

using namespace std;

class Ans {
public:
    ll arr[9];
    char str[100];

    void set(char *s, ll *a){
        strcpy(str, s);
        for(int i=0; i<9; i++){
            arr[i] = a[i];
        }

    }


};


ll prime(ll n){

    for(ll i=2; i*i<=n; i++){
        if(n%i==0) return i;
    }
    return 0;
}

ll ipow(int i, int j){
    if(j==0) return 1;
    ll p = ipow(i, j/2);
    if(j%2) return i*p*p;
    return p*p;

}

bool next(char s[], int n){
    for(int i = n-2; i>0; i--){
        if(s[i]== '1') {
            s[i] = '0';
        }
        else {
            s[i] = '1';
            return true;
        }
    }
    return false;
}

ll makeDec(const char * s, int base){
    ll sum = 0;
    int n = strlen(s);
    for(int i=0;i<n ;i++){

        if(s[n-1-i]=='1'){
            sum+= ipow(base, i);
        }
    }
    return sum;
}

int main()
{
    freopen("C-small-attempt2.in", "rb", stdin);
    freopen("Output.out", "wb", stdout);

    char str[100];
    ll i;
    int t, c;
    int n, j;
    cin>>t;
    int flag;
    ll arr[9];
    ll status;
    int ans;
    Ans anss[100];

    for(c=1; c<=t; c++){
        ans = 0;


        cin>>n>>j;
        for(int i=1; i<n-1; i++){
            str[i] = '0';
        }
        str[0] = '1';
        str[n-1] = '1';
        str[n] = '\0';



        while(true){
            if(ans>=j) break;
            flag = 1;
            for(int j=2; j<=10; j++){
                i = makeDec(str, j);
                //cout<<i<<endl;
                status = prime(i);
                if(status==0) {flag = 0; break;}
                arr[j-2] = status;

            }
            if(flag) {ans++; anss[ans-1].set(str, arr);}
            if(!next(str, n)) break;

            //cout<<"i'm here babe"<<endl;
        }
        cout<<"Case #"<<c<<":"<<endl;
        for(int i=0; i<j; i++){
            cout<<anss[i].str<<" ";
            for(int x = 0; x<9; x++){
                cout<<anss[i].arr[x]<<" ";
            }
            cout<<endl;
        }
    }


    return 0;
}
