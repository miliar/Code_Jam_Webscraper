#include <iostream>
using namespace std;
int visited[10],sum;
int checkForVisited(unsigned long long int mul){
    int r;
    while(mul){
        r=mul%10;
        mul=mul/10;
        if(visited[r]!=1){
            visited[r]=1;
            if(sum!=45){
                sum=sum+r;
            }
            if(sum==45&&visited[0]==1){
                return 1;
            }
        }
    }
    return 0;
}
int main(){
    unsigned long long int t,N,mul,j,i,flag=0;
    cin>>t;
    for(int k=1;k<=t;k++){
        cin>>N;
        flag=0;
        sum=0;
        for(j=0;j<10;j++)
            visited[j]=0;
        for(i=1;i<=500;i++){
            mul=N*i;
            flag=checkForVisited(mul);
            if(flag==1){
                cout<<"Case #"<<k<<": "<<mul<<endl;
                break;
            }
        }
        if(flag==0){
            cout<<"Case#"<<k<<": INSOMNIA"<<endl;
        }
    }
}
