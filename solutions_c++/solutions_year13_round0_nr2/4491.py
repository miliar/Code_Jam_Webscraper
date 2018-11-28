#include <iostream>
#include <cstring>
using namespace std;

#define M 102
#define N 102
int 
//lawn[M][N],
    m, n;

int main()
{
    int T;
    cin>>T;
    
    for(int ti = 1; ti <= T; ++ti)
    {
        cin>>n>>m;
        int lawn[n+1][m+1];
        memset(lawn,0,(n+1)*(m+1)*sizeof(int));
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < m; ++j)
            {
                cin>>lawn[i][j];
                if(lawn[i][j] > lawn[i][m]) lawn[i][m] = lawn[i][j];
                if(lawn[i][j] > lawn[n][j]) lawn[n][j] = lawn[i][j];
            }
        }

        int mn = n*m;
        
        for(int k = 0; k < mn; ++k)
        {
            for(int i = 0; i < n; ++i)
            {
                int j = 1;
                while(j < m && lawn[i][j] == lawn[i][0]) ++j;
                if(j == m)
                {
                    for(int j = 0; j < m; ++j)
                    {
                        lawn[i][j] = lawn[n][j];
                        if(lawn[i][j] > lawn[i][m]) lawn[i][m] = lawn[i][j];
                    }
                }
            }
            
            for(int j = 0; j < m; ++j)
            {
                int i = 1;
                while(i < n && lawn[i][j] == lawn[0][j]) ++i;
                if(i == n)
                {                
                    for(int i = 0; i < n; ++i)
                    {
                        lawn[i][j] = lawn[i][m];
                        if(lawn[i][j] > lawn[n][j]) lawn[n][j] = lawn[i][j];
                    }
                }
            }
        }

        bool yes=true;
        for(int i = 0; i < n; ++i)
        {
            for(int j = 0; j < m; ++j)
            {
                if(lawn[i][j]!=lawn[0][0]) 
                {
                    yes=false;
                    i = n;
                    break;
                }
            }
        }
        cout<<"Case #"<<ti<<": "<<(yes?"YES":"NO")<<endl;
    }
    
    return 0;
}
