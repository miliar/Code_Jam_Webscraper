//alias g++="g++-5 --std=c++1y"
#include<bits/stdc++.h>

using namespace std;

int main(){
    
    //std::ios_base::sync_with_stdio(false);cin.tie(false);
    
    int t,xx,i,j,k,l,n, nn;
    cin>>t;
    for(xx=1;xx<=t;xx++){
        cin>>n;
        j=0;
        pair<int, char> arr[n];
        for(i=0;i<n;i++){
            cin>>arr[i].first;
            arr[i].second = char(int('A')+i);
            j+= arr[i].first;
        }
        nn= n;
        sort(arr, arr+n);
        reverse(arr, arr+n);
        // cout<<arr[0].first<<"\t"<<j<<" "<<n<<endl;
        cout<<"Case #"<<xx<<": ";
        while(j>0){
            if(arr[0].first>1&& arr[1].first <= (j-2)/2){
                cout<<arr[0].second<<arr[0].second<<" ";
                arr[0].first--;
                arr[0].first--;
                j-=2;
            }
            else if(arr[0].first>1 && arr[1].first>(j-2)/2){
                cout<<arr[0].second<<arr[1].second<<" ";
                arr[0].first--;
                arr[1].first--;
                j-=2;
            }
            else if(arr[0].first ==1 && arr[1].first <= (j-1)/2){
                cout<<arr[0].second<<" ";
                arr[0].first--;
                j-=1;
            }
            else{
                cout<<arr[0].second<<arr[1].second<<" ";
                arr[0].first--;
                arr[1].first--;
                j-=2;
            }
            
            sort(arr, arr+nn);
            reverse(arr, arr+nn);
        }
        cout<<"\n";
    }
    return 0;
}
