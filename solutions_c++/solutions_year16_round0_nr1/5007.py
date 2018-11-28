#include<fstream>
#include<algorithm>
using namespace std;
ifstream cin("A-large.in");
ofstream cout("A-large.out");
long long n,t,k,aux;
bool b[10];
void imparte(int x){
    while(x){
        b[x%10]=1;
        x/=10;
    }
}
int main(){
    cin>>t;
    for(int o=1;o<=t;o++){
        cin>>n;
        if(n==0)cout<<"Case #"<<o<<": INSOMNIA\n";
        else{
             for(int i=0;i<=9;i++)b[i]=0;
             bool u=true;
             long long i=1;
             while(u){
                    aux=n*i;
                    i++;
                    imparte(aux);
                    k=0;
                    for(int j=0;j<=9;j++)if(b[j]==true)k++;
                    //for(int j=0;j<=9;j++)cout<<b[j]<<" ";
                    //cout<<"\n";
                    if(k==10)u=false;
                    if(!u)cout<<"Case #"<<o<<": "<<aux<<"\n";
                   }
         }
    }
}
