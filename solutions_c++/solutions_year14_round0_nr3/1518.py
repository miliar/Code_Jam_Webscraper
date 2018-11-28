#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++)

int N,i,j,T,M,mines;
char a[60][60];
void transpose();
bool imp = false;
void equalcase();
void notequalcase();

int main()
{
    scanf("%d",&T);
    //set<pair<pair<int,int>,int> > notp;
    for(int t = 1; t <= T; t++)
    {
        scanf("%d %d %d",&N,&M,&mines); 
        int om = mines;       
        memset(a,'.',sizeof a);            
        bool swapped = false;
        if(N > M)
        { 
            swap(N, M);
            swapped = true;
        }
        a[N-1][M-1] = 'c';      
        imp = false;                  
        if(mines != 0)
        {
            if(mines == N*M - 1)
            {
                memset(a,'*',sizeof a);
                a[N-1][M-1] = 'c';
            }
            else if(N == M) equalcase();
            else       notequalcase();
        }
        printf("Case #%d:\n",t);
        if(imp)
        {
            if(N > M) swap(N, M);
            //notp.insert(mp(mp(N,M),om));
            printf("Impossible\n");
            continue;
        }
        if(swapped)
        { 
            transpose();
            swap(N, M);
        }
        for(i = 0; i < N; i++)
        {
            a[i][M] = '\0';
            printf("%s\n",a[i]);            
        }       
        /* 
        for(i = 0; i < N; i++)
        for(j = 0; j < M; j++)
        if(a[i][j] != '*')
        {
            int dx[] = {+1,+1,+1,-1,-1,-1,0,0};
            int dy[] = {-1,+1,0,-1,+1,0,-1,+1};
            a[i][j] = '0';
            for(int k = 0; k < 8; k++)
            if(i + dx[k] < N && i + dx[k] >= 0 && j + dy[k] < M && j + dy[k] >= 0)
            if(a[i+dx[k]][j+dy[k]] == '*')
                a[i][j]++;
        }
        for(i = 0; i < N; i++)
        for(j = 0; j < M; j++)
        if(a[i][j] != '*')
        {
            int dx[] = {+1,+1,+1,-1,-1,-1,0,0};
            int dy[] = {-1,+1,0,-1,+1,0,-1,+1};
            bool yes = false;
            for(int k = 0; k < 8; k++)
            if(i + dx[k] < N && i + dx[k] >= 0 && j + dy[k] < M && j + dy[k] >= 0)
            if(a[i+dx[k]][j+dy[k]] == '0')
            {
                yes = true;
                break;
            }
            if(i == N-1 && j == M-1) yes = true;
            if(!yes) printf("GADBAD\n");
        }
        else om--;
        if(om != 0) printf("GADBAD %d\n",om);
        for(i = 0; i < M; i++)
            printf("=");
        printf("\n");
        for(i = 0; i < N; i++)
            printf("%s\n",a[i]);
        */
    }
    //tr(notp,it)
    //    cout << it->first.first << ", " << it->first.second << " = " << it->second << endl;
    
    return 0;
}

void transpose()
{
    char b[60][60];
    memset(b,'.',sizeof b);    
    for(i = 0; i < N; i++)
    for(j = 0; j < M; j++)
        b[j][i] = a[i][j];
    memcpy(a,b,sizeof(char)*60*60);
}
        
void equalcase()
{
    if(N*M - mines < 4)
    {
        imp = true;
        return;
    }
    int ii = 0, jj = 0;
    int row = 0;                
    i = ii;
    j = jj;
    int pi = -1, pj = -1;
    while(mines > 0)
    {
        a[i][j] = '*';                
        mines--;
        pi = i;
        pj = j;
        if(row) j++;
        else    i++;
        if(i == N)
        {
            row = 1 - row;
            i = ii;
            j = jj+1;
        }
        else if(j == M)
        {                        
            i = ++ii;
            j = ++jj;
            row = 0;
        }                     
    }                
    imp = false;
    if(pi == N-2)
    {
        a[pi][pj] = '.';
        if(jj+1 != M-2)
            a[ii][jj+1] = '*';
        else
            imp = true;
    }    
    else if(pj == M-2)
    {
        a[pi][pj] = '.';
        //cout << pi << " " << pj << " " << ii << " " << jj << " " << start << endl;
        if(ii+1 != N-2) 
            a[ii+1][jj+1] = '*';
        else
            imp = true;
    }    
}
                
void notequalcase()
{    
    if(N == 1)
    {
        if(mines > M-1)
        {
            imp = true;            
        }
        else
        {
            for(i = 0; i < mines; i++)
                a[0][i] = '*';
        }
        return;
    }
    else if(N == 2)
    {
        if(mines > 2*M-4 || mines%2 == 1)
        {
            imp = true;            
        }
        else
        {
            for(i = 0; i < mines/2; i++)
                a[0][i] = a[1][i] = '*';
        }
        return;
    }
    if(N*M - mines < 4)
    {
        imp = true;
        return;
    }        
    i = j = 0;       
    while(mines && j < M-3)
    {
        a[i][j] = '*';        
        i++;
        mines--;
        if(i == N)
        {
            i = 0;
            j++;
        }
    }
    if(i == N-1)
    {
        if(N > 2)
        {
            a[i-1][j] = '.';
            a[0][j+1] = '*';
        }
        else 
        {
            imp = true;
            return;
        }
    }
    int jstart = j;
    while(mines && i < N-3)
    {
        if(mines >= 3)
        {
            mines -= 3;
            a[i][jstart] = a[i][jstart + 1] = a[i][jstart + 2] = '*';
            i++;
        }
        else if(mines == 2)
        {
            mines = 0;
            a[i][jstart] = a[i+1][jstart] = '*';
        }
        else if(mines == 1)
        {
            mines = 0;
            a[i][jstart] = '*';
        }
    }
    if(mines == 2 || mines == 4)
    {
        imp = true;
        return;
    }
    else if(mines == 1)
    {        
        a[i][jstart] = '*';
    }
    else if(mines == 3)
    {
        a[i][jstart] = a[i+1][jstart] = a[i+2][jstart] = '*';
    }
    else if(mines == 5)
    {
        a[i][jstart] = a[i+1][jstart] = a[i+2][jstart] = a[i][jstart+1] = a[i][jstart+2] = '*';
    }   
}
