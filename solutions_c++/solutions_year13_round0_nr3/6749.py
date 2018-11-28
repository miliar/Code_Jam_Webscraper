#include<iostream>
using namespace std;
int main(){
    int casos;
    cin>>casos;
    int i ;
    int a,b;
    for(i = 1 ; i <= casos; i++){
        cin>>a>>b;
        int respuesta =0;
        if( a <= 1 && b >=1)       
            respuesta = respuesta +1;
        if( a <= 4 && b >=4)       
            respuesta = respuesta +1;
        if( a <= 9 && b >=9)       
            respuesta = respuesta +1;
        if( a <= 121 && b >=121)       
            respuesta = respuesta +1;
        if( a <= 484 && b >=484)       
            respuesta = respuesta +1;
        cout<<"Case #"<<i<<": "<<respuesta<<endl;
    }
}
