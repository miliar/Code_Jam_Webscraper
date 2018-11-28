#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    int j;
    for(j = 1; j <= t; j++){
        int n;
        cin>>n;
        char b[n+1];
        int a[n+1];
        cin>>b;
        int i;
        for(i = 0; i <= n; i++){
            a[i] = b[i] - 48;
        }
        int count = 0;
        int sum = a[0];
        int k;
        for(i = 1; i <= n; i++){
            if(sum < i && a[i] != 0){
                count = count + (i - sum);
                sum = sum + count;
                sum = sum + a[i];
            }
            else{
                sum = sum + a[i];
            }
        }
        cout<<"Case #"<<j<<": "<<count<<"\n";
    }
    return 0;
}
