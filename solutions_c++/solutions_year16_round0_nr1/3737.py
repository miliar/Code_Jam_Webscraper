#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int digi[10];
int contg;

void limpiar(){
    for(int i=0;i<10;i++) digi[i]=0;
}

void ver(){
    for(int i=0;i<10;i++) cout<<digi[i]<<" ";
    cout<<endl;
}

bool verifica(){
    for(int i=0;i<10;i++)
        if(digi[i]==0)return false;
    return true;
}

void check(int n){
    if(digi[n]==0){
        digi[n]=1;
        contg++;
        //cout<<"MARCA:"<<n<<endl;
    }
}

void part(long long int n){
    long long int extr;
    while(n>=10){
        extr=n%10;
        n=n/10;
        check(extr);
        //cout<<extr<<"-";
    }
    check(n);
    //cout<<n<<endl;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large_armt.out","w",stdout);
    long long int n,inc,pres;
    int casos;
    cin>>casos;
    for(int ic=1;ic<=casos;ic++){
        cin>>n;
        if(n==0)cout<<"Case #"<<ic<<": INSOMNIA"<<endl;
        else{
            limpiar();
            contg=0;
            inc=1;
            int tmp=0;
            while(verifica()==false){
                pres=n*inc;

                //cout<<n<<"*"<<inc<<"="<<"PRES:"<<pres<<endl;
                part(pres);
                inc++;
                //ver();
                //cout<<"C:"<<contg<<endl;
                //cout<<"C:"<<contg<<endl;
                //cout<<pres<<","<<contg<<endl;
            }
            cout<<"Case #"<<ic<<": "<<pres<<endl;
        }
    }

    return 0;
}
