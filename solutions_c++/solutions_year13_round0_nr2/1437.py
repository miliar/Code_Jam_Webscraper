#include <iostream>
#include <cstdio>
using namespace std;

const int MAXSIZE = 100;

int N, M;
int desiredHeight[MAXSIZE][MAXSIZE];
int resultHeight[MAXSIZE][MAXSIZE];

void readInput()
{
    cin >> N >> M; 
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> desiredHeight[i][j];
}

string solve()
{   
    for (int i = 0; i < N; i++)   
    {
        int maxRowHeight = desiredHeight[i][0];
        for (int j = 1; j < M; j++)
            if (desiredHeight[i][j] > maxRowHeight)
               maxRowHeight = desiredHeight[i][j];
               
        for (int j = 0; j < M; j++)
            resultHeight[i][j] = maxRowHeight; 
    }
    
    for (int j = 0; j < M; j++)
    {
        int maxColHeight = desiredHeight[0][j];
        for (int i = 1; i < N; i++)
            if (desiredHeight[i][j] > maxColHeight)
               maxColHeight = desiredHeight[i][j];
               
        for (int i = 0; i < N; i++)
            if (resultHeight[i][j] > maxColHeight)
                resultHeight[i][j] = maxColHeight;
    }    
       
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (resultHeight[i][j] != desiredHeight[i][j])
               return "NO";  
       
    return "YES";   
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        readInput();
        
        string result = solve();
        printf("Case #%d: %s\n", t, result.c_str());        
    }
    
    return 0;
}
