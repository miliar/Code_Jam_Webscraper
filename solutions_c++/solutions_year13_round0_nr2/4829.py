#include <iostream>
#include <vector>
#include <cstdio>
#define FOR(i,a)    for(int i = 0;i<a;i++)
#include <string>

using namespace std;

int main(){
    freopen("ip.txt","r",stdin);
    freopen("op.txt","w",stdout);
    int t;
    int caseno = 1;
    cin>>t;
    FOR(i,t){
        cout<<"Case #"<<caseno<<": ";
        int c,r;
        cin>>r>>c;
        int arr[101][101];
        int maxr[101] = {0},maxc[101] = {0};
        FOR(j,r){
            FOR(k,c){
                cin>>arr[j][k];
                maxr[j] = max(maxr[j],arr[j][k]);
                maxc[k] = max(maxc[k],arr[j][k]);
            }
        }
        bool b = true;
        FOR(j,r)    FOR(k,c)    if(maxr[j] == arr[j][k] || maxc[k] == arr[j][k])    ;   else    b = false;
        if(!b)  cout<<"NO"; else    cout<<"YES";
        cout<<"\n";
        caseno++;
    }
    return 0;
}
