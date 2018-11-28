#include<iostream>
#include<algorithm>
#include<sstream>
#include<string>
using namespace std;

#define ll long long
ll solve(ll a, const int n, ll* ar, int ind){
    while(ind < n && a > ar[ind]){
        a += ar[ind];
        ind++;
    }
    if(ind >= n)
        return 0;
//cout<<"DEBUG: in removing or adding mote with index "<<ind<<endl;
//now ind<n AND a<=ar[ind]

    if(a==1){
        return 1 + solve(a, n, ar, ind+1); //remove mote
    }
    int tmp = 1 + min(
                     solve(a, n, ar, ind+1), //remove mote
                     solve((a<<1)-1, n, ar, ind));//add mote
//cout<<"DEBUG: returning "<<tmp<<endl;
    return tmp;
}
int main()
{
    unsigned ts;
    cin>>ts;
    for(unsigned t=1; t<=ts; t++){
//INPUT
        ll a;
        int n;
        cin>>a>>n;
        ll *ar = new ll[n];
        for(unsigned i=0; i<n; i++)
            cin>>ar[i];
//PROCESSING
        sort(ar, ar+n);
        ll ans = 0;
        ans = solve(a, n, ar, 0//start index
              );
        cout<<"Case #"<<t<<": "<<ans<<endl;
//CLEANUP
        delete[] ar;
    }
    return 0;
}
