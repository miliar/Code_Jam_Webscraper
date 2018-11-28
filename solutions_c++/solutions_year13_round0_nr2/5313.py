#include<cstdio>
#include<iostream>

using namespace std;

int matriz[100][100];
int maior_linha[100];
int maior_coluna[100];

bool checa(int linha,int coluna)
{
    int i,j;

    for(int i=0;i<linha;i++)
    {
        for(int j=0;j<coluna;j++)
        {
            //cout<< matriz[i][j]<<'['<<i<<']' <<'[' <<j <<']'<<' '<< maior_linha[i]  <<' '<<maior_coluna[j] << endl;

            if(maior_coluna[j]>matriz[i][j] && maior_linha[i]>matriz[i][j]) return false;
        }
    }

    return true;
}

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);

    int quantidade_de_casos,caso=0;

    cin >> quantidade_de_casos;

    while(quantidade_de_casos--)
    {
        caso++;
        int linha,coluna,i,j;

        cin >> linha >> coluna;

        for(i=0;i<linha;i++)
        {
            maior_linha[i]=-1;

            for(j=0;j<coluna;j++)
            {
                int numero;
                cin >> numero;
                matriz[i][j]=numero;
                if(numero>maior_linha[i]) maior_linha[i] = numero;
            }
        }

        for(j=0;j<coluna;j++)
        {
           maior_coluna[j]=-1;

            for(i=0;i<linha;i++)
            {
                if(matriz[i][j]>maior_coluna[j]) maior_coluna[j] = matriz[i][j];
            }
        }

        if(checa(linha,coluna)) cout << "Case #"<<caso<<": YES"<<endl;
        else  cout << "Case #"<<caso<<": NO"<<endl;

    }

    return 0;
}
