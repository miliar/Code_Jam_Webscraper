#include <iostream>
#define K 4
#define X 'X'
#define O 'O'
#define T 'T'
#define N '.'
#define FORI for(int i=0;i<K;i++)
#define FORJ for(int j=0;j<K;j++)

using namespace std;
char table[K][K];

char verify(int x,int o,int t){
    if(x==4 || (x==3 && t==1) )
        return X;
    else if(o==4 || (o==3 && t==1) )
        return O;
    return N;
}
int isIn(int i,int j,char type){
    return (table[i][j]==type)?1:0;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    int x;
    int o;
    int t;
    cin>>n;
    bool is_full;
    char won;
    for(int c=1;c<=n;c++){
        is_full = true;
        won = N;
        FORI{
            x = o = t = 0;
            FORJ {
                cin>>table[i][j];
                 x+= isIn(i,j,X);
                 o+= isIn(i,j,O);
                 t+= isIn(i,j,T);
                 is_full = (is_full && table[i][j]!=N);
            }
            if(won==N)
                won = verify(x,o,t);
        }
/*
        FORI {
            FORJ{
                 cout<<table[i][j];
            }cout<<endl;
        }
*/
        if(won==N){
            FORI{
                x = o = t = 0;
                FORJ {
                    x+= isIn(j,i,X);
                    o+= isIn(j,i,O);
                    t+= isIn(j,i,T);
                }
                if(won==N)
                    won = verify(x,o,t);
            }
        }
        if(won==N){
            x = o = t = 0;
            FORI{
                 x+= isIn(i,i,X);
                 o+= isIn(i,i,O);
                 t+= isIn(i,i,T);
            }
            if(won==N)
                won = verify(x,o,t);
        }
        if(won==N){
            x = o = t = 0;
            FORI{
                 x+= isIn(i,K-1-i,X);
                 o+= isIn(i,K-1-i,O);
                 t+= isIn(i,K-1-i,T);
            }
            if(won==N)
                won = verify(x,o,t);
        }
        cout<<"Case #"<<c<<": ";
        switch(won){
            case X:
                cout<<"X won";
            break;
            case O:
                cout<<"O won";
            break;
            case N:
                cout<<((!is_full)?"Game has not completed":"Draw");
            break;
        }
//        if(n!=c)
        cout<<endl;
//        FORI FORJ cout<<table[i][j];
    }
    return 0;
}
