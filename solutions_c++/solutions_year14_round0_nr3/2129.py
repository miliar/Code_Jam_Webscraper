#include  <iostream>
#define ll long long
#define ld long double
#define eps 10e-8
using namespace std;

ll T, R, C, M, N;
bool udalosie;
char bartus[30][30];
char tymczasowo[30][30];
int ilosc[30][30];

int ile(int x, int y)
{
    int res  =  0;
    for(int i = x-1; i <= x+1; ++i)
        for(int j = y-1; j <= y+1; ++j)
            if(bartus[i][j] == '*') res++;
    return res;
}

void sprobuj(int x, int y)
{
    bartus[x][y] = '+'; 
    int ileile = ile(x, y);
    if(ileile != 0) return;
    for(int i = x-1; i <= x+1; ++i)
    {
        for(int j = y-1; j <= y+1; ++j)
        {
            if(bartus[i][j] != '*' && bartus[i][j] != '+' && bartus[i][j] != '$')
            {
                ilosc[i][j] = ile(i, j);
                if(ilosc[i][j] == 0) sprobuj(i, j);
            }
        }
    }
}

bool sprawdz()
{
    for(int i = 1; i <= R; ++i)
        for(int j = 1; j <= C; ++j)
            tymczasowo[i][j] = bartus[i][j];
    for(int i = 1; i <= R; ++i)
    {
        for(int j = 1; j <= C; ++j)
        {
            if(bartus[i][j] == '.')
            {
                sprobuj(i, j);
                int ok = 0;
                for(int i = 1; i <= R; ++i)
                {
                    for(int j = 1; j <= C; ++j)
                    {
                        if(bartus[i][j] == '+' || ilosc[i][j] != 0) ok++;
                    }
                }
                if(ok == (R*C-M)) {bartus[i][j] = 'c'; return true;}
                else
                {
                    for(int i = 1; i <= R; ++i)
                        for(int j = 1; j <= C; ++j) {bartus[i][j] = tymczasowo[i][j]; ilosc[i][j] = 0;}
                }
            }
        }
    }
    return false;
}

int main()
{
    ios_base::sync_with_stdio(0);
    
    cin >> T;
    
    for(int lzd = 1; lzd <= T; ++lzd)
    {
        cin >> R >> C >> M;
        N = (1 <<(R*C));
        udalosie = false;
        
        for(int i = 0; i <= R+1; ++i) 
			bartus[i][0] = bartus[i][C+1] = '$';
			
        for(int i = 0; i <= C+1; ++i)
			 bartus[0][i] = bartus[R+1][i] = '$';
        for(int i = 1; i <= R; ++i)
        	for(int j = 1; j <= C; ++j) 
				{
					bartus[i][j] = '.'; ilosc[i][j] = 0;
				}
        for(ll S = 0; S <= N-1; ++S)
        {
            int ile = 0;
            
            for(ll i = 0; i <= R*C; ++i) 
				if((S & (1 <<i)) !=  0 ) 
					ile++;
					
            if(ile !=  M) 
				continue;
				
            int kolumna, rzad = 0;
            
            for(ll i = 0; i <= R*C; ++i)
            {
                kolumna = i%C+1;
                
                if(kolumna == 1) rzad++;
                
                if((S & (1 << i)) !=  0 ) 
				
				bartus[rzad][kolumna] = '*';
            }
            if(sprawdz() == true)
            {
                cout  << "Case #"  << lzd  << ":"  << endl;
                for(int i = 1; i <= R; ++i)
                {
                    for(int j = 1; j <= C; ++j)
                    {
                        if(bartus[i][j] == '+') 
							cout  << '.';
                        else cout  << 
							bartus[i][j];
                    }
                    cout  << endl;
                }
                
                udalosie = true;
                break;
            }
            for(int i = 1; i <= R; ++i)
                for(int j = 1; j <= C; ++j) {bartus[i][j] = '.'; ilosc[i][j] = 0;}

        }
        if(!udalosie) cout  << "Case #"  << lzd  << ":"  << endl  << "Impossible"  << endl;
    }
    return 0;
}
