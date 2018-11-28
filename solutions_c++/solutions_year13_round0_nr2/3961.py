#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[])
{
    int t, n, m, a[102][102];
    int rmax[102], cmax[102];
    ifstream fin("B-large.in", ios::in);
    ofstream fout("B.out", ios::out);
    fin >> t;
    for(int k=1; k<=t; k++)
    {
        fin >> n >> m;
        for(int i=1; i<=n; i++) 
        {
            rmax[i] = 0;
        }
        for(int i=1; i<=m; i++) 
        {
            cmax[i] = 0;
        }
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                fin >> a[i][j];
                if(a[i][j] > rmax[i]) rmax[i] = a[i][j];
                if(a[i][j] > cmax[j]) cmax[j] = a[i][j];
            }
        }
        int flag = 0;
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                if((a[i][j]<rmax[i] && a[i][j]<cmax[j])) 
                {
                    fout << "Case #" << k << ": NO" << endl;
                    flag = 1;
                    break;
                }
            }
            if(flag) break;
        }
        if(!flag) fout << "Case #" << k << ": YES" << endl;
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
