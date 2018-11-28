#include <iostream>

using namespace std;

int T;

int R,C,M;

char  tablero[51][51];
char  tabsol[51][51];
int haySol=0;

int esSolucion(int x,int y)
{
    int i,j,k;
    int nvistas=0;
    int nvistastmp=0;
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            tabsol[i][j]=0;
        }
    }
    
    tabsol[x][y]=1;
    nvistas++;
    
    while(nvistastmp!=nvistas)
    {
        nvistastmp=nvistas;
        for(i=0;i<R;i++)
        {
            for(j=0;j<C;j++)
            {
                // Expandimos y la ponemos a 2 como ya expandida
                if(tabsol[i][j]==1)
                {
                    tabsol[i][j]=2;
                    int minas=0;
                    // Contamos las minas
                    if(i>0 && tablero[i-1][j]=='*')
                    {
                        minas=1;
                    }
                    if(i<R-1 && tablero[i+1][j]=='*')
                    {
                        minas=1;
                    }
                    if(j>0 && tablero[i][j-1]=='*')
                    {
                        minas=1;
                    }
                    if(j<C-1 && tablero[i][j+1]=='*')
                    {
                        minas=1;
                    }
                    // Diagonal
                    
                    if(i>0 && j>0 && tablero[i-1][j-1]=='*')
                    {
                        minas=1;
                    }
                    if(i<R-1 && j>0 &&  tablero[i+1][j-1]=='*')
                    {
                        minas=1;
                    } 
                    if(i>0 && j<C-1 && tablero[i-1][j+1]=='*')
                    {
                        minas=1;
                    }
                    if(i<R-1 && j<C-1 &&  tablero[i+1][j+1]=='*')
                    {
                        minas=1;
                    }
                    
                    // Si es expandible
                    if(minas==0)
                    {
                        if(i>0 && tabsol[i-1][j]==0)
                        {
                            tabsol[i-1][j]=1;
                            nvistas++;
                        }
                        if(i<R-1 && tabsol[i+1][j]==0)
                        {
                            tabsol[i+1][j]=1;
                            nvistas++;
                        }
                        if(j>0 && tabsol[i][j-1]==0)
                        {
                            tabsol[i][j-1]=1;
                            nvistas++;
                        }
                        if(j<C-1 && tabsol[i][j+1]==0)
                        {
                            tabsol[i][j+1]=1;
                            nvistas++;
                        }
                        // Diagonal
                    
                        if(i>0 && j>0 && tabsol[i-1][j-1]==0)
                        {
                            tabsol[i-1][j-1]=1;
                            nvistas++;
                        }
                        if(i<R-1 && j>0 && tabsol[i+1][j-1]==0)
                        {
                            tabsol[i+1][j-1]=1;
                            nvistas++;
                        } 
                        if(i>0 && j<C-1 && tabsol[i-1][j+1]==0)
                        {
                            tabsol[i-1][j+1]=1;
                            nvistas++;
                        }
                        if(i<R-1 && j<C-1 && tabsol[i+1][j+1]==0)
                        {
                            tabsol[i+1][j+1]=1;
                            nvistas++;
                        }
                        
                    }
                    
                    
                }
            }
        }
    }
    // Caso solucion
    if(nvistas>=((R*C)-M)){
        return 1;
    }
    return 0;
    
    
}

void imprimeTablero()
{
    
    int i,j,k;
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            cout << tablero[i][j];
        }
        cout << endl;
    }
}

void t(int nminas, int x, int y)
{
    int i,j,k;
    if(nminas==M)
    {
        for(i=0;i<R;i++)
        {
            for(j=0;j<C;j++)
            {
                if(tablero[i][j]=='.')
                {
                    tablero[i][j]='c';
                   /* cout << "Tablero tmp " <<endl;
                    imprimeTablero();
                    
                    cout << "FIN Tablero tmp " <<endl;
                    system("pause");
                    */if(esSolucion(i,j))
                    {
                        imprimeTablero();
                        haySol=1;
                        return;
                    }
                    tablero[i][j]='.';
                }
            }
        }
    }
    else
    {
        for(i=x;i<R;i++)
        {
            int tmp;
            if(i==x)
            {
                tmp=y;
            }
            else
            {
                tmp=0;
            }
            for(j=tmp;j<C;j++)
            {
                if(tablero[i][j]=='.')
                {
                    tablero[i][j]='*';
                    t(nminas+1,i,j);
                    tablero[i][j]='.';
                }
                if(haySol==1)
                {
                    return;
                }
            }
        }
    }
}


void resuelve()
{
    int i,j,k;
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            tablero[i][j]='.';
        }
    }
    haySol=0;
    t(0,0,0);
    if(haySol==0)
    {
        cout << "Impossible" << endl;
   
    }
}


int main()
{
    int i,j,k;
    cin >> T;
    
    for(i=0;i<T;i++)
    {
        cin >> R >> C >> M;
        cout << "Case #"<<(i+1)<<":"<<endl;
        resuelve();
    }
    
    
}
