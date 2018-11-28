#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;


int arr[11] ={0};

int check(int arr[]){

    for(int i=0;i<10;i++){
        if(arr[i]!=1){
            return 0;
        }
    }
    return 1;
}

void compute(long long N , int arr[]){

    while(N){
        int p = N%10;
        N=N/10;
        arr[p]=1;
    }

}

int main() {

    int T;
    cin>>T;
    int k=0;
    while(T--) {
        k++;
        long long N ;
        cin>>N;

        memset(arr,0,sizeof(arr));

        if(N==0){

            cout <<"Case #"<<k<<": "<<"INSOMNIA"<<endl;;
        }else{
            long long p = N;
            compute(N,arr);
            int flag = check(arr);

            int i=2;
            while(!flag && (p<1000000000000L )){
                p = i*N;

                compute(p,arr);
                flag = check(arr);
                i++;
            }
            if(flag){
                cout <<"Case #"<<k<<": "<<p<<endl;
            }else{
                cout <<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
            } 
        }  
        
    }
    return 0;

}