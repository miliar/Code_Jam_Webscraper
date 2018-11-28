#include <iostream>
#include <cmath>
#define MAX_N 1001
#define MAX_M 10001
using namespace std;
int arr[MAX_N];

bool valid(int eat,int N){
    int sum = 0;
    for(int i=0;i<N-1;i++){
        if(max(0,arr[i]-eat) > arr[i+1]) { 
            return false;
        }
    }
    
    return true;
}

int binary(int N){
    int p = 0, q = 10000, m;
    while(p<=q){
        m = (p+q)/2;
        if(valid(m,N) && !valid(m-1,N)){
            return m;
        } else if(valid(m,N)){
            q = m-1;
        } else {
            p = m+1;
        }
    }
    return 0;
}

int main(){
    int T, N, M, counter = 1;
    int sum1,sum2;
    cin>>T;
    while(T--){
        cin>>N;
        sum1 = sum2 = 0;
        for(int i=0;i<N;i++)
            cin>>arr[i];

        int eat = binary(N);
        sum2 = min(arr[0],eat);
        for(int i=1;i<N;i++){
            if(arr[i] < arr[i-1]) sum1+= (arr[i-1]-arr[i]);
    
            if(i+1!=N)
                sum2 += min(arr[i],eat);
        }

        cout<<"Case #"<<counter++<<": "<<sum1<<" "<<sum2<<endl;
    }
    return 0;
}
