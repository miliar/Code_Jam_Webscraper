/*input

*/
#include <bits/stdc++.h>
#define X first
#define Y second
#define ll long long
using namespace std;
void solve(){
    int n;
    cin>>n;
    vector<int> v(n);
    for (int i = 0; i < n; i++){
        cin>>v[i];
    }
    int y=0;
    for (int i = 1; i < n; i++){
        if(v[i]<v[i-1]){
            y+=(v[i-1]-v[i] );
        }
    }
     int xx=-1;
    for (int i = 1; i < n; i++){
        if(v[i]<=v[i-1]){
            xx=max(xx,(v[i-1]-v[i]));
        }
    }
    int z=0;
    for (int i = 0; i <n-1; i++){
        z+=min(v[i],xx);
        //cout<<i<<" ";
    }
    cout<<y<<" "<<z;

}
int main(){
    ios_base::sync_with_stdio(false);
    freopen("C:/Users/Enjoy/Desktop/A-large.in","r",stdin);
    freopen("C:/Users/Enjoy/Desktop/output.txt","w",stdout);
    int t;cin>>t;
    int i=1;
    while(t--){
        cout<<"Case #"<<(i++)<<": ";
        solve();
        cout<<endl;
    }
    return 0;
}