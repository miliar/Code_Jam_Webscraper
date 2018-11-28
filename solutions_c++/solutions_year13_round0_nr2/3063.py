#include<iostream>
#include<fstream>
#include<map>
#include<string.h>
using namespace std;
bool find_possible(int lawn[][100], int row_max[], int col_max[], int n, int m)
{
    int possible_moves[100][100];
    for (int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            possible_moves[i][j] = 0;
            if(lawn[i][j] >= row_max[i]) possible_moves[i][j]++;
            if(lawn[i][j] >= col_max[j]) possible_moves[i][j]++;
            if(!possible_moves[i][j])   return false;
        }
    
    }
    return true;
}

int main()
{
    
    int num_cases;
    char c;
    int lawn[100][100];
    int row_max[100];
    int col_max[100];
    bool result = false;

    cin>>num_cases;
    int m, n;
    int count = 0;
    while (count < num_cases)
    {
        cin>>n>>m;
        for(int i=0; i<100; i++)
        {
            row_max[i] = 0;
            col_max[i] = 0;
        }
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                cin>>lawn[i][j];
                if(row_max[i] < lawn[i][j]) row_max[i] = lawn[i][j];
                if(col_max[j] < lawn[i][j]) col_max[j] = lawn[i][j];
            }
        }
        result = find_possible(lawn, row_max, col_max, n, m);
        cout<<"Case #"<<count+1<<": "<<(result?"YES":"NO")<<"\n";
        count++;
    }
}
