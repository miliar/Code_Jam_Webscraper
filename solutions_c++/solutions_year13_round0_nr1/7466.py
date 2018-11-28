//#include<iostream>
#include <fstream>
using namespace std;
const int inf = 0x3f3f3f3f;
int kk[6][6];

ifstream fin("A-large.in");
ofstream fout("a.out");

inline bool solve(int d)
{
	if(d==3||d==4) {fout<<"X won"<<endl;return true;}
	if(d==-3||d==-4) {fout<<"O won"<<endl;return true;}
	return false;
}

int main()
{
       int T, e, i, j;
       char z;
       bool flag,judge;
       fin>>T;
       for(e=1; e<=T; ++e)
       {
              flag = false;
              judge = false;
              for(i=0; i<6; ++i)
                     for(j=0; j<6; ++j)
                            kk[i][j]=0;

              for(i=1; i<=4; ++i)
                     for(j=1; j<=4; ++j)
              {
                     fin>>z;
                     if(z=='X') kk[i][j]=1;
                     if(z=='O') kk[i][j]=-1;
                     if(z=='T')  kk[i][j]=0;
                     if(z=='.')   {kk[i][j]=999;flag=true;}
              }

              for(i=1; i<=4; ++i)
                     for(j=1; j<=4; ++j)
              {
                     kk[i][0]+=kk[i][j];
                     kk[0][j]+=kk[i][j];
					 if(i==j) kk[0][0]+=kk[i][j];
					 if(i+j==5) kk[0][5]+=kk[i][j]; 
              }
              
              fout<<"Case #"<<e<<": ";
              for(i=1;i<=4;++i)
              {
				if(solve(kk[0][i])) {judge=true;break;}
				if(solve(kk[i][0])) {judge=true;break;}
			  }
			  if(judge) continue;
			  else if(solve(kk[0][0])) continue;
			  else if(solve(kk[0][5])) continue;
			  else if (flag) fout<<"Game has not completed"<<endl;
			  else fout<<"Draw"<<endl;

       }
       return 0;
}
