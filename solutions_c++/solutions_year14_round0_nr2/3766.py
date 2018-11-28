#include<bits/stdc++.h>

using namespace std;

int main(){
        freopen("B-large.in","r",stdin);
        freopen("out3.txt","w",stdout);
        int tc,cas=0;
        cin>>tc;
        while(tc--){
                long double c,f,x,rate=2.0;
                cin>>c>>f>>x;

                long double initial = x/2.0;
                long double current=initial;
                long double intmid=0.0;

                while(current <= initial){
                        initial=current;
                        current = intmid + c/rate + x/(rate+f);
                        intmid+= c/rate;
                        rate+=f;
                }

                cout<<"Case #"<<++cas<<": "<<fixed<<setprecision(7)<<initial<<endl;
        }
}
