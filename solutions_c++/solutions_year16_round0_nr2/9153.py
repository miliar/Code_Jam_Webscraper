#include <bits/stdc++.h>

using namespace std;

string cad;

int dp[109][109][109];

int sol(int ind, int pos, int neg){

    if(ind == cad.size())   {
        if(pos == cad.size())   return 0;
        return 200;
    }

    int ans = 200;

    if(dp[ind][pos][neg]!=-1)   return dp[ind][pos][neg];

    if(cad[ind] == '+'){
        ans = min(ans, sol(ind+1, pos+1, neg));
        ans = min(ans, 1 + sol(ind+1, neg, pos+1));
    }else{
        ans = min(ans, sol(ind+1, pos, neg+1));
        ans = min(ans, 1 + sol(ind+1, neg+1, pos));
    }

    return dp[ind][pos][neg] = ans;
}


int main(){

    freopen("in.c","r",stdin);
    freopen("out.c","w",stdout);

    int TC;
    int NC = 0;
    cin>>TC;

    while(TC--){
        NC++;

        cin>>cad;

        memset(dp, -1, sizeof dp);

        int answer = sol(0,0,0);
        printf("Case #%d: %d\n" , NC , answer);



    }




    return 0;
}
