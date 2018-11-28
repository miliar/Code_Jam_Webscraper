#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;

int main(){
	
	freopen("in.txt", "r", stdin);
	freopen("out2-l.txt", "w", stdout);
    int t, n=0;
    cin>>t;
    while(t--){
        n++;
        int arr[2501] = {0};
        int N , i, tt, j, k;
        cin>>N;
        j = N;
        N = ((N*2) - 1);
        
        for(i=1;i<=N;i++)
            for(k=0;k<j;k++){
                cin>>tt;
                arr[tt]++;
            }
            
        cout<<"Case #"<<n<<": ";
        for(i=1;i<2501;i++)
            if(arr[i]%2!=0)
                cout<<i<<" ";
        cout<<endl;

    }
}

