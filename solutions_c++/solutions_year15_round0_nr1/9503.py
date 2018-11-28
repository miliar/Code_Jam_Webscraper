#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("in.c","r",stdin);
    freopen("out.c","w",stdout);

    int TC , NC = 1;

    cin>>TC;

    while(TC--){
        int n;
        string cad;

        cin>>n;
        cin>>cad;

        int numberPersonStand = 0;
        int ans = 0;

        for(int i = 0 ; i<cad.size() ;i++){
            if(numberPersonStand>=i){
                numberPersonStand += cad[i]-'0';
            }else{
                int dif = (i-numberPersonStand);
                ans+=dif;
                numberPersonStand += dif;
                numberPersonStand += cad[i] - '0';
            }
        }

        cout<<"Case #"<<NC++<<": "<<ans<<endl;

    }

    return 0;
}
