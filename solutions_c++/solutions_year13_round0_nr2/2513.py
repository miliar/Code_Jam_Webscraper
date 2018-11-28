#include<fstream>
using namespace std;
ifstream in ("lawn.in");
ofstream out ("lawn.out");
int mat[1001][1001];
int maxLin[1001];
int maxCol[1001];
int maxim(int a,int b)
{
    if(a>b)
        return a;
    return b;
}
void readAndSolve(int caz)
{
    int n,m;
    bool sePoate=true;
    in>>n>>m;
    for(int i=1;i<=900;i++)
        maxLin[i]=maxCol[i]=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
        {
            in>>mat[i][j];
            maxLin[i]=maxim(maxLin[i],mat[i][j]);
            maxCol[j]=maxim(maxCol[j],mat[i][j]);

        }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            if(mat[i][j]<maxLin[i] && mat[i][j]<maxCol[j])
                sePoate=false;
    out<<"Case #"<<caz<<": ";
    if(sePoate==true)
        out<<"YES\n";
    else
        out<<"NO\n";
}
int main()
{
    int n;
    in>>n;
    for(int i=1;i<=n;i++)
        readAndSolve(i);
}
