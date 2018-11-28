#include<stdio.h>
#include<iostream>
#include<memory.h>

using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    
    int T,smax;
    string shyness;
    cin>>T;
    
    for(int i=0;i<T;++i){
        cin>>smax;
        cin>>shyness;
        int pl_sum = 0;
        int pl_need = 0;
        for(int j=0;j<=smax;++j){
            int pl_num = shyness[j] - '0';
            if(j <= pl_sum){
                pl_sum += pl_num;
            }else{
                pl_need += (j - pl_sum);
                pl_sum = j + pl_num;
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<pl_need<<endl;
    }
    
    return 0;
}
