#include <bits/stdc++.h>
using namespace std;


int main(){
    freopen("output.txt", "w", stdout);
    freopen("input.in", "r", stdin);
    int t;
    cin>>t;
    for(int qq=1;qq<=t;qq++){
        cout<<"Case #"<<qq<<": ";
        int n;
        cin>>n;

        int k = 0;
        int  freq[2501];
        for(int i=0;i<2501;i++){
            freq[i]=0;
        }
        
        int x[n];
        int f;
        for(int i=0; i<2*n-1; i++){
            for(int j=0; j<n; j++){
                cin>>f;
                freq[f]++;
            }
        }
        for(int i=0;i<2501;i++){
            if(freq[i]%2){
                x[k++] = i;
            }
        }
        
        sort(x, x+k);
    
        for(int  i=0;i<n; i++){
            cout<<x[i]<<" ";
        }
        cout<<endl;
        
    }
    return 0;
}
