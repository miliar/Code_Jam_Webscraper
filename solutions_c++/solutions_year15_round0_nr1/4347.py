#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("Alargein.txt","r",stdin);
    freopen("Alargeout.txt","w",stdout);
    int n, q;
    string c;
    cin>>n;
    for (int i=0; i<n; i++){
        cin>>q;
        cin>>c;
        int numApp=c[0]-'0';
        int numToAdd=0;
        for (int j=1; j<q+1; j++){
            if (numApp<j){
                numToAdd+=j-numApp;
                numApp=j;
            }
            numApp+=c[j]-'0';
        }
        cout<<"Case #"<<i+1<<": "<<numToAdd<<endl;
    }
    return 0;
}
