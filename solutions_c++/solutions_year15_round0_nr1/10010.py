#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main(){
    int casos;
    int smax;
    int sacum[1001];
    int x=1;
    string cad;
    int i, cont;
    cin>>casos;
    while(x<=casos){
        cont=0;
        cin>>smax>>cad;
        sacum[0]=cad.at(0)-48;
        for(i=1; i<=smax; i++){
            sacum[i]=cad.at(i)-48;
            if(sacum[i-1]>=i){                
                sacum[i]+=sacum[i-1];
            }else{
                cont+=i-sacum[i-1];
                sacum[i]+=sacum[i-1]+(i-sacum[i-1]);
            }
        }

        cout<<"Case #"<<x<<": "<<cont<<endl;   
        x++;
    }

    return 0;

}
