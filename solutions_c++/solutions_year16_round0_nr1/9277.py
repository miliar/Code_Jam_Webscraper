#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
bool u[10];
int br;
int n,t,tt,ans;
long long da(){
    int i;
    br=0;
    int a1,a2,a3;
    a1=a2=a3=n;
    while(a3){
        if(!u[a3%10])br++;
        u[a3%10]=true;
        a3/=10;
    }
    for(i=1;i<=1000100;i++){
        if(br==10)return a2;
        a2+=a1;
        a3=a2;
        while(a3){
            if(!u[a3%10])br++;
            u[a3%10]=true;
            a3/=10;
        }
    }
}
int main(){
    ifstream fin("A.in");
    ofstream fout("A.out");
    cin>>t;
//    fin>>t;
    int i;
    for(tt=1;tt<=t;tt++){
        cin>>n;
//        fin>>n;
        cout<<"Case #"<<tt<<": ";
//        fout<<"Case #"<<tt<<": ";
        if(n==0)cout<<"INSOMNIA\n";
        else cout<<da()<<endl;
//        if(n==0)fout<<"INSOMNIA\n";
//        else fout<<da()<<endl;
        for(i=0;i<10;i++)
            u[i]=false;
    }
	return 0;
}
