#include<fstream>
#include<string.h>
using namespace std;
const int M1 = 110;
ifstream fin("B-large.in");
ofstream fout("bout.txt");

int N,M;
int mat[M1][M1];
int lef[M1][M1];
int rig[M1][M1];
int up[M1][M1];
int dw[M1][M1];
int main()
{
    int T;
	fin>>T;
	for(int c=1;c<=T;++c)
	{   fin>>N>>M;
	    memset(lef,0,sizeof(lef));
		memset(rig,0,sizeof(rig));
		memset(up,0,sizeof(up));
		memset(dw,0,sizeof(dw));
	    for(int i=1;i<=N;++i)
		    for(int j=1;j<=M;++j)
		        fin>>mat[i][j];
		for(int i=1;i<=N;++i)
		{   for(int j=1;j<=M;++j)
		    {   lef[i][j] = lef[i][j-1];
			    if(mat[i][j]>lef[i][j])
			        lef[i][j] = mat[i][j];
			}
		}
		for(int i=1;i<=N;++i)
		{   for(int j=M;j>0;--j)
		    {   rig[i][j] = rig[i][j+1];
			    if(mat[i][j]>rig[i][j])
			        rig[i][j] = mat[i][j];
			}
		}
		for(int j=1;j<=M;++j)
		{   for(int i=1;i<=N;++i)
		    {   up[i][j] = up[i-1][j];
			    if(mat[i][j]>up[i][j])
			        up[i][j] = mat[i][j];
			}
		}
		for(int j=1;j<=M;++j)
		{   for(int i=N;i>0;--i)
		    {   dw[i][j] = dw[i+1][j];
			    if(mat[i][j]>dw[i][j])
			        dw[i][j] = mat[i][j];
			}
		}
		bool ans = true;
		for(int i=1;i<=N&&ans;++i)
		    for(int j=1;j<=M&&ans;++j)
			{   if((mat[i][j]<lef[i][j-1]||mat[i][j]<rig[i][j+1])&&(mat[i][j]<up[i-1][j]||mat[i][j]<dw[i+1][j]))
			        ans = false;
			}
		fout<<"Case #"<<c<<": ";
		if(ans)
		    fout<<"YES"<<endl;
		else
		    fout<<"NO"<<endl;
	}
	
    return 0;
}