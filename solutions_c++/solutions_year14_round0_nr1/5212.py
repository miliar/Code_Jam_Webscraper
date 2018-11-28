#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int m,matriz1[4][4],vetor1[4],vetor2[4];
        cin>>m;
        for(int k=0;k<4;k++)
        {
            for(int h=0;h<4;h++)
            {
                cin>>matriz1[k][h];
            }
        }
        for(int k=0;k<4;k++)
        vetor1[k]=matriz1[m-1][k];
        int m2,matriz2[4][4];
        cin>>m2;
        for(int k=0;k<4;k++)
        {
            for(int h=0;h<4;h++)
            {
                cin>>matriz2[k][h];
            }
        }
        for(int k=0;k<4;k++)
        vetor2[k]=matriz2[m2-1][k];
        int contador=0,valor;
        for(int k=0;k<4;k++)
        {
            for(int h=0;h<4;h++)
            {
                if(vetor1[k]==vetor2[h])
                {
                    contador++;
                    valor=vetor1[k];
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(contador==1)
        cout<<valor<<endl;
        else if(contador>1)
        cout<<"Bad magician!"<<endl;
        else
        cout<<"Volunteer cheated!"<<endl;
    }

    return 0;
}
