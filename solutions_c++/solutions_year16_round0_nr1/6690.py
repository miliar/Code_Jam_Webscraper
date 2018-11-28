#include <iostream>
#include <fstream>

using namespace std;

int contar(int,int);

int main()
{
    //ifstream in("large-in.txt");
    //ofstream out("large-out.txt");

    long long T, N, i;

    cin>>T;
    for(i=0;i<T;i++){
        cout<<"Case #"<<i+1<<": ";
        cin>>N;
        if(0==N) cout<<"INSOMNIA"<<endl;
        else cout<<contar(N,i+1)<<endl;
    }
    return 0;
}

int contar(int n, int j){
    bool a[10] = {false};
    int cantElem = 10;
    long long k,aux=n, resto;

    ///Mientras no haya encontrado a los 10 digítos
    for(k=1;cantElem>0;k++){
        aux=k*n;
        while(aux>0 && cantElem>0){
            resto=aux%10;
            if(false==a[resto]){a[resto]=true; cantElem--;}
            aux/=10;
        }
    }
    return (k-1)*n;
}
