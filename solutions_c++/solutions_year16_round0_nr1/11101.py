#include<iostream>
#include<fstream>

using namespace std;
int main(){
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("A-large.out");
    int N, T, dig, V[10], aux, k, c=0;
    bool exit, insomnia;
    fin>>T;
    while(T--){
        //exit=false;
        for(int i=0; i<10; i++)
            V[i]=i;
        insomnia=false;
        c++;
        k=0;
        fin>>N;
        if(N==0) insomnia=true;
        do{
            k++;
            aux=N*k;
            while(aux>0){
                dig=aux%10;
                aux/=10;
                for(int i=0; i<10; i++){
                    if(dig==V[i]){
                        V[i]=-1;
                    }
                }
            }
            for(int i=0; i<10; i++){
                if(V[i]<0) exit=false;
                else{
                    exit=true;
                    break;
                }
            }
            if(insomnia) exit=false;
        }while(exit);
        fout<<"Case #"<<c<<": ";
        if(insomnia) fout<<"INSOMNIA"<<endl;
        else fout<<N*k<<endl;
    }
    return 0;
}
