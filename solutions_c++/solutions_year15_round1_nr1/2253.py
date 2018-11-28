# include<bits/stdc++.h>
using namespace std;

int arr[2000];

int main(){
    //freopen("A3.in","r",stdin);
    //freopen("A.out","w",stdout);

    int t;
    cin>>t;
    for(int k=1 ;k<=t ; k++){

        int m1=0,m2=0;
        int n;
        cin>>n;

        for(int i=0 ; i<n ; i++ ) cin>>arr[i];

        int maxDx = 0;
        int r = 0;
        if(arr[0]-arr[1]>0){
            maxDx = arr[1]-arr[0];
            r = 1;
        }

        for(int i=1 ; i<n ; i++){
            if(arr[i-1]-arr[i]  > maxDx){
                maxDx = arr[i-1]-arr[i];
                r = i;
            }
        }

        m2 = maxDx;


        for(int i=1; i<n ; i++){
            if(i!=r){
                //if (arr[i-1]>arr[i]){
                    m2+=min(maxDx,arr[i-1]);
                    //cout<<arr[i-1]<<endl;
                //}
            }




            if(arr[i-1]>arr[i]){
                m1 += (arr[i-1]-arr[i]);
            }
        }

        cout<<"Case #"<<k<<": "<<m1<<" "<<m2<<endl;


    }

}
