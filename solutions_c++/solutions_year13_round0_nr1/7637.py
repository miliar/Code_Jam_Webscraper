#include <fstream>
#include <string>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

string S[4];

bool win(char c)
{
    int i,j;bool ok;
    for(i=0;i<4;++i)
    {
          ok=true;
        for(j=0;j<4;++j)if( S[i][j]!='T' && S[i][j]!=c )ok=false;
        if(ok)return true;
    }
    for(i=0;i<4;++i)
    {
          ok=true;
        for(j=0;j<4;++j)if( S[j][i]!='T' && S[j][i]!=c )ok=false;
        if(ok)return true;
    }

      ok=true;
      for(j=0;j<4;++j)if( S[j][j]!='T' && S[j][j]!=c )ok=false;
      if(ok)return true;


      ok=true;
      for(j=0;j<4;++j)if( S[3-j][j]!='T' && S[3-j][j]!=c )ok=false;
      if(ok)return true;
}





int main()
{
    int n,i,j,k;
    cin>>n;
    for(i=0;i<n;++i)
    {
        for(j=0;j<4;++j)cin>>S[j];
        bool comp=true;
        for(j=0;j<4;++j)
            for(k=0;k<4;++k)
                if(S[j][k]=='.')comp=false;
        cout<<"Case #" <<(i+1)<<": ";
        if(win('X'))cout<<"X won\n";
        else if (win('O'))cout<<"O won\n";
        else if (comp)cout<<"Draw\n";
        else cout<<"Game has not completed\n";


    }
    return 0;
}
