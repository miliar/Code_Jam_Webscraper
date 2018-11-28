/**
ariel0
**/
#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0_armt.out","w",stdout);
    int casos,k,c,s;
    long long int salt;
    cin>>casos;
    for(int ic=1;ic<=casos;ic++){
        cin>>k>>c>>s;
        salt=pow(k,c-1);
        cout<<"Case #"<<ic<<":";
        for(int i=0;i<s;i++){
            long long int a=pow(k,c-1);
            cout<<" "<<(i*(a)+1);
        }
        cout<<endl;
    }
    return 0;
}

