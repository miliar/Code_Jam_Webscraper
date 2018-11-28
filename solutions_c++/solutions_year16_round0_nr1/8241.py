#include <bits/stdc++.h>

using namespace std;

bool valasz;
long long asd,barany,szaml,t,n;
bool szam[20];
long long tabl[1000100];

long long szamjegyek(long long x){
    while(x>0){
        if(!szam[x%10]) szaml++;
        szam[x%10]=true;
        x/=10;
    }
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    for(long long i=1;i<=1000010;i++){
            for(int j=0;j<=10;j++) szam[j]=false;
            valasz=false;
            asd=0;
            szaml=0;
            barany=i;
            szamjegyek(barany);
            while(szaml<10 && asd<1000000) {
                asd++;
                barany+=i;
                szamjegyek(barany);
            }
            if(asd==10000) tabl[i]=-1;
            else tabl[i]=barany;
        }
    cin>>t;
    for(int i=1;i<=t;i++) {
        cin>>n;
        if(tabl[n]==-1) cout<<"ERROR";
        if(n==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i<<": "<<tabl[n]<<endl;
    }
    return 0;
}
