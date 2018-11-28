#include <bits/stdc++.h>

using namespace std;
#define ll long long
int main(){

    freopen("B-large.in", "r", stdin);

    freopen("yoyo.txt", "w",stdout);

    int t, n, i;

    string sss;

    cin>>t;

    for(i=1; i<=t; i++){

        cin>>sss;

        int l=sss.size()-1;

        int ans=0;

        while(1){

            if(ans%2==0){

                while(l>=0 && sss[l]=='+')l--;

                if(l>=0)ans++;

            }else{

                while(l>=0 && sss[l]=='-')l--;

                if(l>=0)ans++;

            }

            if(l<0)break;
        }

        printf("Case #%d: %d\n", i, ans);

    }

}
