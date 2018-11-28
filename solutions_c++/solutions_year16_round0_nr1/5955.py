#include<bits/stdc++.h>
using namespace std;
int arreglo[10];
void meter(int n){
    while(n!=0){
        int a = n%10;
        arreglo[a] = 1;
        n = n/10;
    }
}
bool verificar(){
    for(int i=0;i<=9;i++){
        if(arreglo[i]==0)return false;
    }
    return true;
}
int main(){
    freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
    int T;scanf("%d",&T);
    for(int i=1;i<=T;i++){
        memset(arreglo,0,sizeof(arreglo));
        long long int n;cin>>n;
        long long int temp = n;
        if(n==0){
            printf("Case #%d: INSOMNIA\n",i);
        }
        else{
            meter(temp);
            while(!verificar()){
                temp+=n;
                meter(temp);
            }
            printf("Case #%d: %lli\n",i,temp);
        }
    }
    return 0;
}
