# include <bits/stdc++.h>
using namespace std;

int main(){
    //freopen("Ds.in","r",stdin);
    //freopen("D.out","w",stdout);
    int t,x,c,r;
    cin>>t;
    for(int k=1 ; k<=t ; k++){
        cin>>x>>c>>r;
        string winner = "RICHARD";

        if( x<7 && (c*r) % x == 0){
            if (c>=x-1 && r>=x-1)
                winner = "GABRIEL";
        }

        cout<<"Case #"<<k<<": "<<winner<<endl;
    }
}
