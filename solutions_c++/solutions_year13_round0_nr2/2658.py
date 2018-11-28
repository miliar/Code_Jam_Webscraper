#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int r = 1; r <=t;r++){
        int n, m;
        cin>>n>>m;
        vector< vector<bool> > check(n, vector<bool>(m, false));
        vector< vector<int> > lawn(n, vector<int>(m, 0));
        for(int i=0;i < n;i++)
            for(int j=0;j < m; j++){
                cin>>lawn[i][j];
                if(lawn[i][j] == 2)
                    check[i][j] = true;
            }
        for(int i=0;i < n;i++){
            for(int j=0; j < m;j++){
                if(!check[i][j]){
                    bool temp = true;
                    for(int k=0;k < n; k++)
                        if(lawn[i][j] != lawn[k][j]){
                            temp = false;
                            break;
                        }
                    if(temp)
                        check[i][j] = true;
                    temp = true;
                    for(int k=0;k < m; k++)
                        if(lawn[i][j] != lawn[i][k]){
                            temp = false;
                            break;
                        }
                    if(temp)
                        check[i][j] = true;
                }
            }
        }

        bool test = true;
        for(int i=0;i < n;i++)
            for(int j=0; j < m;j++){
                test = test && check[i][j];
            }
        if(test)
            cout<<"Case #"<<r<<": "<<"YES"<<endl;
        else
            cout<<"Case #"<<r<<": "<<"NO"<<endl;
    }
}
