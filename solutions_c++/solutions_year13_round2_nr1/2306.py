#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
/*
4
2 2
2 1
2 4
2 1 1 6
10 4
25 20 9 100
1 4
1 1 1 1
*/
typedef long long int ll;
using namespace std;

int solve(){
    ll a,n;
    ll result=0;
    cin>>a>>n;

    vector <ll> mote;
    for (int i=0; i<n; i++){
         ll tmp; cin>>tmp;
         mote.push_back(tmp);
    }
    if (a==1) return n;
    sort (mote.begin(), mote.end());

    for (int i=0; i<n; i++){
        if (a>mote[i]){
            a+=mote[i];
        }
        else{
            ll anew=a; ll took=0;
            while (anew<=mote[i]){
                anew=anew*2-1; took ++;
            }
            if(took<(n-i)) {a=anew+mote[i];result+=took;}
            else return (result+n-i);
        }
    }

return result;
}

int main()
{
    int t; cin>>t;
    for (int i=1; i<=t; i++){
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    }
    return 0;
}
