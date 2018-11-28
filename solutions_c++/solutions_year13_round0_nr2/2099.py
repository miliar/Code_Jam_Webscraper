#include <iostream>
#include <vector>
#include <string>
#include <sstream>


using namespace std;

bool check(int N, int M);
int max1(int col, int M);
int max2(int wier, int N);

int game[101][101];
bool game1[101][101];

int main()
{   
    int T, N, M;
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        ostringstream ss;
        ss << i+1;
        cout<<"Case #"<<ss.str()<<": ";
        
        cin>>N>>M;
        
        for(int j = 0; j < N; ++j)
            for(int k = 0; k < M; ++k)
                cin>>game[j][k];
        
        if(check(N,M))
            cout<<"YES";
        else cout<<"NO";
        cout<<'\n';
    }
    
    
    return 0;   
}

bool check(int N, int M)
{
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j)
           game1[i][j] = false;
           
    for(int i = 0; i < N; ++i)
    {
        int pom = max1(i, M);
        for(int j = 0; j < M; ++j)
            game1[i][j] = (game[i][j] == pom);
    }
    
    for(int i = 0; i < M; ++i)
    {
        int pom = max2(i, N);
        for(int j = 0; j < N; ++j)
            if(game[j][i] == pom)
                game1[j][i] = true;
    }
    
    for(int i = 0; i < N; ++i)
        for(int j = 0; j < M; ++j)
           if(!game1[i][j])
               return false; 
               
    return true;   
}

int max1(int col, int M)
{
    int ret = game[col][0];
    for(int j = 1; j < M ; ++j)
        ret = max(ret, game[col][j]);
    
    return ret;
}

int max2(int wier, int N)
{
    int ret = game[0][wier];
    for(int j = 1; j < N ; ++j)
        ret = max(ret, game[j][wier]);
    
    return ret;
}
