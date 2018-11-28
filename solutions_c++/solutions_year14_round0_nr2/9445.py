#include <iostream>
#include <fstream>
#include <conio.h>
const int M=100;

using namespace std;
ifstream fin;
FILE *fout;
bool BestStrategy(double C, double F, double X, double sp=2, double bt=0, double nt_prev=-1, double ck=0)
{
    cout<<"------------------------"<<'\n';
    double nt, t;
    for(; ck<X;)
    {
        nt=bt+X/sp; cout<<"To win:="<<nt<<'\n';
        if(nt>nt_prev)
        {
            if(nt_prev!=-1)
            {
                cout<<'\n'<<'\n'<<"Best Strategy: "<<nt_prev<<'s'<<'\n';
                fprintf(fout, "%.7f\n", nt_prev);
                return 1;
            }
        }
        t=C/sp;
        bt+=t;
        sp+=F;
        if(BestStrategy(C, F, X, sp, bt, nt))
            return 1;
    }
}

int main()
{
    char S[M]; cout<<"Input file: "; cin.getline(S, M); fin.open(S);
    if(!fin) 
    { 
        cout<<"Файла не существует";
        return 0;
    }
    cout<<"Output file: "; cin.getline(S, M); fout = fopen(S, "w");
    double C, F, X;
    int N; fin>>N;
    for(int i=0; i<N; i++)
    {
        fin>>C>>F>>X; 
        cout<<"Farm Cost :"<<C<<" Farm Procduction: "<<F<<" Win: "<<X<<'\n';        
        cout<<"We are STARTING TEST: #"<<i+1<<'\n';
        fprintf(fout, "Case #%d: ", i+1);
        BestStrategy(C, F, X);
    }
    fclose(fout);
    getch();
    return 0;
}
