#include<bits/stdc++.h>
using namespace std;
const int TAM = 16;
bool isPrime(long long int n){
    for(long long int i=2;i*i<=n;i++){
        if(n%i==0)return false;
    }
    return true;
}

long long int convertir(bitset<TAM> bits, long long int b){
    long long int r = 0;
    long long int potencia = 1;
    for(long long int i=0;i<16;i++){
        if(bits[i]==1){
            r+=potencia;
        }
        potencia*=b;
    }
    return r;
}
bool isPrimeBases(bitset<TAM> bits){
    for(long long int i=2;i<=10;i++){
        if(isPrime(convertir(bits,i)))return true;
    }
    return false;
}
long long int divisor(long long int valor){
    for(long long int i=2;i<valor;i++){
        if(valor%i==0)return i;
    }return -1;
}
void pintarBitset(bitset<TAM> bits,long long int N){
    for(long long int i=N-1;i>=0;i--){
        cout<<bits[i];
    }
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
    long long int T;cin>>T;
    for(long long int i=1;i<=T;i++){
        cout<<"Case #"<<i<<":"<<endl;
        bitset<TAM> bits =0;
        long long int N,J;cin>>N>>J;
        long long int caso = 0;
        bits[0] = 1;
        bits[N-1] = 1;
        long long int valorBits = bits.to_ulong();
        while(caso<J){
            if(!isPrimeBases(bits)){
                pintarBitset(bits,N);
                cout<<" ";
                for(long long int x=2;x<=10;x++){
                    cout<<divisor(convertir(bits,x))<<" ";
                }
                cout<<endl;
                caso++;
            }
            valorBits+=2;
            bits = valorBits;
        }
    }
}
