# include <bits/stdc++.h>
using namespace std;

int arr[2000];
int bef[2000];

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A.out","w",stdout);
    int n;
    cin>>n;
    for(int k=1 ; k<= n ; k++){

        int s;
        cin>>s;
        char x;
        int aux;
        for(int i=0 ; i<=s ; i++){
            cin>>x;
            arr[i] = (x-'0');
            if(arr[i]!=0){
                aux=i;
            }
        }

        s = aux;

        //bef[1]=arr[0];
        int ans=0;

        for(int i=1 ; i<=s; i++){
            bef[i] = bef[i-1]+arr[i-1];
            if (i<=bef[i]){
                continue;
            }
            //cout<<i<<" "<<bef[i]<<"******"<<endl;
            ans+=(i-bef[i]);
            arr[i-1]+=(i-bef[i]);
            i--;
        }

        /*for(int i=0 ; i<=s; i++){
           cout<<arr[i]<<" ";
        }cout<<endl;*/

        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
}
