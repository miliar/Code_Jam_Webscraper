#include <iostream>

using namespace std;

int resp,R1,R2,m[10][10];

void verifica (int i, int j,int X,int Y){
    int valor=m[i][j];
    R1=R2=1;
    for(int k=0;k<10;k++){
        if(k<Y && valor<m[i][k]){
                R1=0;
        }
        if(k<X && valor<m[k][j]){
            R2=0;
        }
        if(R1==0 && R2==0){
            resp=0;
        }
    }

}

int main (){
    int n,counter=0,X,Y;
    cin>>n;

    while(counter<n){
        cin>>X>>Y;
        resp=1;
        for(int i=0;i<X;i++){
            for(int j=0;j<Y;j++){
                cin>>m[i][j];
            }
        }

        for(int i=0;i<X;i++){
            for(int j=0;j<Y;j++){
                        verifica(i,j,X,Y);
            }
        }
        if(resp==0) cout<<"Case #"<<counter+1<<": NO"<<endl;
        else cout<<"Case #"<<counter+1<<": YES"<<endl;


        counter++;
    }


    return 0;
}
