#include <bits/stdc++.h>
using namespace std;
#define ll long long
double arr[1010] ;
double arr2[1010] ;
bool table[1010];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,CASE=0,n,i,rt,wr,j;
    cin>>T;
    while(T--){
        memset(table,0,sizeof(table));
        cin>>n;
        for(i=0;i<n;i++)    cin>>arr[i];sort(arr,arr+n);
        for(i=0;i<n;i++)    cin>>arr2[i];sort(arr2,arr2+n);
        rt = 0; wr = 0;
        /*for(i=0;i<n;i++){
            cout<<arr[i]<<' ';
        }
        cout<<endl;
        for(i=0;i<n;i++){
            cout<<arr2[i]<<' ';
        }
        cout<<endl;*/
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(table[j])    continue ;
                if(arr[j]>arr2[i]){
                    rt++;
                    table[j] = true;
                    break;
                }
            }
        }
        memset(table,0,sizeof(table));
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(table[j])    continue ;
                if(arr2[j]>arr[i]){
                    wr++;
                    table[j] = true;
                    break;
                }
            }
        }
        cout<<"Case #"<<++CASE<<": "<<rt<<' '<<n-wr<<endl;
    }
}
