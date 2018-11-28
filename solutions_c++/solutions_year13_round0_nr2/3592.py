#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("Blarge.in");
ofstream fout("Bout.txt");
int buff[100][100];
int N,M,T;
int row[100];
int col[100];
int main()
{
    fin >> T;
    for(int i=0;i<T;i++)
    {
            fin >> N >> M;
            for(int j=0;j<N;j++)
                    for(int k=0;k<M;k++)
                            fin >> buff[j][k];
            for(int j=0;j<100;j++)
            {row[j]=0;col[j]=0;}
            for(int j=0;j<N;j++)
            {
                    for(int k=0;k<M;k++)
                    {
                            if(buff[j][k]>row[j])row[j]=buff[j][k];
                            if(buff[j][k]>col[k])col[k]=buff[j][k];
                    }
            }
            bool possible=true;
            for(int j=0;j<N;j++)
            {
                    for(int k=0;k<M;k++)
                    {
                            if(buff[j][k]<row[j]&&buff[j][k]<col[k]){possible=false; break;}
                    }
                    if(possible==false)break;
            }
            fout << "Case #" << i+1 << ": ";
            if(possible) fout << "YES" << endl;
            else fout << "NO" << endl;
    }
    system("pause");
}
