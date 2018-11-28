#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int T,R,C,a[110][110]; bool arr[110][110][6];

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin >> T;

    int i,j,k,o,res; char c;
    for (o=1; o<=T; o++){
        fin >> R >> C;
        for (i=1; i<=R; i++)
            for (j=1; j<=C; j++){
                fin >> c;
                if (c=='.') a[i][j]=0;
                else if (c=='^') a[i][j]=1;
                else if (c=='>') a[i][j]=2;
                else if (c=='v') a[i][j]=3;
                else a[i][j]=4;
            }

        fout << "Case #" << o <<": ";

        memset(arr,0,sizeof(arr));
        res=0;
        for (i=1; i<=R; i++)
            for (j=1; j<=C; j++)
                if (a[i][j]!=0){
                    for (k=1; k<i; k++)
                        if (a[k][j]!=0) arr[i][j][1]=1;
                    for (k=i+1; k<=R; k++)
                        if (a[k][j]!=0) arr[i][j][3]=1;
                    for (k=j+1; k<=C; k++)
                        if (a[i][k]!=0) arr[i][j][2]=1;
                    for (k=1; k<j; k++)
                        if (a[i][k]!=0) arr[i][j][4]=1;
                }
        bool ans=1;
        for (i=1; i<=R; i++)
            for (j=1; j<=C; j++)
                if (a[i][j]!=0 && arr[i][j][a[i][j]]==0){
                    if (arr[i][j][1]==0 && arr[i][j][2]==0 && arr[i][j][3]==0 && arr[i][j][4]==0) ans=0;
                    res++;
                }

        if (ans) fout << res << "\n";
        else fout << "IMPOSSIBLE\n";
    }
    return 0;
}
