#include <iostream>
#include <fstream>
#include <conio.h>
const int M=100;

using namespace std;
ifstream fin;
ofstream fout;
int Check(int Ans1, int Ans2, int Arr1[4][4], int Arr2[4][4])
{
    cout<<"We are in FUNCTION:"<<'\n';
    Ans2--; Ans1--;
    bool f=false;
    int B[4], res;
    for(int i=0; i<4; i++)
        B[i]=Arr1[Ans1][i];
        
    cout<<"-------------------------"<<'\n';
    for(int j=0; j<4; j++)
    {
        cout<<"Comp: A["<<Ans2<<']'<<'['<<j<<"]="<<Arr2[Ans2][j]<<'\n';
        for(int k=0; k<4; k++)
        {
            cout<<"     with B["<<k<<"]="<<B[k]<<' ';
            if(Arr2[Ans2][j]==B[k])
            {
                cout<<"<--WE FOUND IT";
                if(f)
                { 
                    cout<<" AGAIN!"<<'\n';
                    return 0;
                }
                f=true;
                res=B[k];
            }
            cout<<'\n';
        }
    }
    cout<<"-------------------------"<<'\n';
    if(!f) cout<<"ERROR"<<'\n';
    else cout<<"OK"<<'\n';
    if(!f) return -1;
    return res;
}

int main()
{
    char S[M]; cin.getline(S, M); fin.open(S);
    if(!fin) 
    { 
        cout<<"Файла не существует";
        return 0;
    }
    cin.getline(S, M); fout.open(S);
    int N, Ans1, Ans2, Arr1[4][4], Arr2[4][4], res;
    fin>>N;
    for(int i=0; i<N; i++)
    {
        fin>>Ans1; cout<<Ans1<<'\n';
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                fin>>Arr1[j][k];
                cout<<Arr1[j][k]<<' ';
            }
            cout<<'\n';
        }
        cout<<'\n';
        fin>>Ans2; cout<<Ans2<<'\n';
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                fin>>Arr2[j][k];
                cout<<Arr2[j][k]<<' ';
            }
            cout<<'\n';
        }
        cout<<'\n';
        
        cout<<"We are STARTING TEST: #"<<i+1<<'\n';
        res=Check(Ans1, Ans2, Arr1, Arr2);
        switch(res)
        {
            case 0: fout<<"Case #"<<i+1<<": Bad magician!"<<'\n'; break;
            case -1: fout<<"Case #"<<i+1<<": Volunteer cheated!"<<'\n'; break;
            default: fout<<"Case #"<<i+1<<": "<<res<<'\n'; break;
        }
    }
    
    getch();
    return 0;
}
