#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int ncases;
    cin>>ncases;
    for( int t = 0; t < ncases; t++){
        int n, m;
        cin>>n>>m;
        vector<vector<int>> lawn(n, vector<int>(m));
        for( int i = 0; i < n; i++){
            for( int j = 0; j < m; j++){
                cin>>lawn[i][j];
            }
        }
        int success = 1;
        for( int i = 0; i < n; i++){
            for( int j = 0; j < m; j++){
                int success1 = 1;
                for( int k = 0; k < m; k++){
                    if( lawn[i][j] < lawn[i][k]){
                        success1 = 0;
                        break;
                    }
                }
                if (success1)
                    continue;
                for( int k = 0; k < n; k++){
                    if( lawn[i][j] < lawn[k][j]){
                        success = 0;
                        break;
                    }
                }    
                if( success)
                    continue;
                else
                    break;
            }
            if( success)
                continue;
            else
                break;     
        }
        if( success)
            cout<<"Case #"<<t+1<<": YES"<<endl;
        else
            cout<<"Case #"<<t+1<<": NO"<<endl;
    }
}