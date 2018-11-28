#include<bits/stdc++.h>
using namespace std;

int main (){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int Test ;
    cin >> Test ;

    for (int i=0 ; i < Test ; ++i){
        long long int S,needed=0,have;
        string Smax;
        cin >> S >> Smax;
        have = Smax[0]-48;
        for (int j=1 ; j <Smax.size();++j){
            if (have < j){
                needed += (j-have);
                have +=(j-have);
            }
            have += (Smax[j]-48);
        }

    cout << "Case #" << i+1 << ": " << needed << endl;


    }











    return 0;
}
