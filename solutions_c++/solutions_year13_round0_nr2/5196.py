#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int k;
    cin>>k;
    int mat[105][105];
    int filas[105];
    for(int c=0; c<k; c++)
    {
        int n, m;
        cin>>n>>m;
        int voy;
        memset(filas, -1, sizeof(filas));

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                cin>>mat[i][j];
                if(mat[i][j] > filas[i])
                    filas[i] = mat[i][j];
            }
        }

        bool flag = false;
        for(int i=0; i<m; i++)
        {
            voy = 1;
            int mayor = 0;
            int menor = 1000000;
            bool uno = false;
            for(int j=0; j<n; j++)
            {
                if(mat[j][i] > mayor)
                {
                    mayor = mat[j][i];
                }
                if(mat[j][i] < filas[j] && mat[j][i] < menor)//no esty marcado
                {
                    menor = mat[j][i];
                }
            }
            if(menor != 1000000 && menor != mayor)
            {
                cout<<"Case #"<<c+1<<": NO"<<endl;
                flag = true;
                break;
            }
        }
        if(!flag)
            cout<<"Case #"<<c+1<<": YES"<<endl;
    }

    return 0;
}
