#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("tes.txt");
    fout.open("ou.txt");
    int n;
    fin >> n;
    for (int num=0; num<n; num++)
    {
        fout << "Case #" << num+1 << ": ";
        int f[100][100],ffff[100][100];
        int fff[100][100],ff[100][100];
        int a,b;
        fin >> a >> b;
        int p[100][100];
        for (int i=0; i<a; i++)
            for (int j=0; j<b; j++)
            {
                fin >> p[i][j];
            }
        for (int i=0; i<a; i++)
        {
            f[i][0] = p[i][0];
            for (int j=1; j<b; j++)
            {
                f[i][j] = max(f[i][j-1],p[i][j]);
            }
            ff[i][b-1] = p[i][b-1];
            for (int j=b-2; j>=0; j--)
            {
                ff[i][j] = max(ff[i][j+1],p[i][j]);
            }
        }


        for (int j=0; j<b; j++)
        {
            fff[0][j] = p[0][j];
            for (int i=1; i<a; i++)
            {
                fff[i][j] = max(fff[i-1][j],p[i][j]);
            }
            ffff[a-1][j] = p[a-1][j];
            for (int i=a-2; i>=0; i--)
            {
                ffff[i][j] = max(ffff[i+1][j],p[i][j]);
            }
        }
        int tot=0;
        for (int i=0; i<a; i++)
            for (int j=0; j<b; j++)
            {
                if ((p[i][j]>=max(f[i][j],ff[i][j]))||(p[i][j]>=max(fff[i][j],ffff[i][j]))) tot++;
            }
        if (/*(sum==a*b)&&*/(tot==a*b)) fout << "YES" <<endl; else fout << "NO" <<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
