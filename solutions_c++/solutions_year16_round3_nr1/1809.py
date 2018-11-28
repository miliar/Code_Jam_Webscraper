#include<bits/stdc++.h>
using namespace std;
struct node{
    int val;
    char c;
    bool operator< ( const node& other ) const
      { return val < other.val; }
};
struct node a[26];
int main(){
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int c = 1;
    while(t--){
        int n;
        cin>>n;
        int i;
        for(i = 0; i < n; i++){
            cin>>a[i].val;
            a[i].c = 'A' + i;
        }
        sort(a,a+n);
        cout<<"Case #"<<c++<<": ";
        i = n-1;
        while(i > 0){
            while(a[i].val > a[i-1].val){
                cout<<a[i].c<<" ";
                a[i].val--;
            }
            i--;
            if(i == 0){
                break;
            }
            while(a[i].val > a[i-1].val){
                cout<<a[i].c<<a[i+1].c<<" ";
                a[i].val--;
                a[i+1].val--;
            }
            while(a[i+1].val > 0){
                cout<<a[i+1].c<<" ";
                a[i+1].val--;
            }
        }
        while(a[0].val > 0){
            cout<<a[0].c<<a[1].c<<" ";
            a[0].val--;
        }
        cout<<"\n";
    }
    return 0;
}
