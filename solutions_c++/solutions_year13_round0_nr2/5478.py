#include <cstdio>
#include <iostream>
 
#define MAX 102
 
using namespace std;
 
int T[MAX][MAX],n,m;
bool Col[MAX], Row[MAX];
 
bool solve()
{
    int count = 0;
    for(int i = 0; i < n; ++i)
        Row[i]=true;
    
    for(int i = 0; i < m; ++i)
        Col[i]=true;
 
        for(int i = 0; i < n; ++i)
        {
                for(int j = 0; j < m; ++j)
                        if(T[i][j]==2)
                                Row[i]=false;
        }
 
        for(int i = 0; i < m; ++i)
        {
                for(int j = 0; j < n; ++j)
                        if(T[j][i]==2)
                                Col[i]=false;
        }
                        
        for(int i = 0; i < n; ++i)
        {
                for(int j = 0; j < m; ++j)
                {
                        if(T[i][j]==1)
                        {
                                if(Col[j]==false && Row[i]==false)
                                        return false;
 
 
                                /*if(i==0 && j>0)
                                        if((T[i][j-1]==2 || T[i][j+1]==2) && T[i+1][j]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j==0 && i>0)
                                        if((T[i-1][j]==2 || T[i+1][j]==2) && T[i][j+1]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j>0 && i>0 && j<m-1 && i<n-1)
                                        if((T[i-1][j]==2 || T[i+1][j]==2) && (T[i][j-1]==2 || T[i][j+1]==2))
                                                return false;//printf("%d %d\n", i,j);
 
                                if(i==n-1 && j>0)
                                        if((T[i][j-1]==2 || T[i][j+1]==2) && T[i-1][j]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j==m-1 && i>0)
                                        if((T[i-1][j]==2 || T[i+1][j]==2) && T[i][j-1]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j==0 && i==0)
                                        if(T[i+1][j]==2 && T[i][j+1]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j==m-1 && i==0)
                                        if(T[i+1][j]==2 && T[i][j-1]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j==0 && i==n-1)
                                        if(T[i-1][j]==2 && T[i][j+1]==2)
                                                return false;//printf("%d %d\n", i,j);
 
                                if(j==m-1 && i==n-1)
                                        if(T[i-1][j]==2 && T[i][j-1]==2)
                                                return false;//printf("%d %d\n", i,j);*/
                        }
                }
        }
 
        return true;
}
 
int main()
{
        int t;
        scanf("%d", &t);
        for (int i = 1; i <= t; ++i)
        {
                scanf("%d %d", &n,&m);
                for(int i = 0; i < MAX; ++i)
                        for(int j = 0; j < MAX; ++j)
                                T[i][j]=0;
 
                for(int j = 0; j < n; ++j)
                        for(int k = 0; k < m; ++k)
                                scanf("%d", &T[j][k]);
 
                cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << endl;
        }
        return 0;
}