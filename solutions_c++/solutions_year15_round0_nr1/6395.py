#include <bits/stdc++.h>

using namespace std;

int arr[1000+100];

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int N;
    cin>>N;
    for(int casos=1;casos<=N;casos++){
        int S, cant=0;
        string cad;
        cin>>S;
        cin>>cad;
        arr[0]=(cad[0]-'0');
        for(int i=1;i<=S;i++){
            if(i>arr[i-1]){
                cant+=i-arr[i-1];
                arr[i-1]=i;
            }
            arr[i]=arr[i-1]+(cad[i]-'0');
        }
        cout<<"Case #"<<casos<<": "<<cant<<endl;
    }
    return 0;
}
