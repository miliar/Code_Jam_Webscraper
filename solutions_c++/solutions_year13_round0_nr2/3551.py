#include <cstdio>
#include <iostream>
using namespace std;

int final[101][101];
int a[101][101];
int n, m;
bool ok;

bool cal(){
    for(int i = 0; i < n; i++){
        int tmax = -1;
        for(int j = 0; j < m; j++){
            tmax = tmax > final[i][j] ? tmax : final[i][j];
        }
        for(int j = 0; j < m; j++){
            if(a[i][j] > tmax)
                a[i][j] = tmax;
        }
    }
    
    for(int i = 0; i < m; i++){
        int tmax = -1;
        for(int j = 0; j < n; j++){
            tmax = tmax > final[j][i] ? tmax : final[j][i];
        }
        for(int j = 0; j < n; j++){
            if(a[j][i] > tmax)
                a[j][i] = tmax;
        }
    }
    
    /*cout << endl;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }    
        cout << endl;
    }*/
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(a[i][j] != final[i][j])
                return false;
        }    
    }
    
    return true;

}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int cases = 1; cases <= t; cases++){
        cout << "Case #" << cases << ": ";
		cin >> n >> m;
		for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cin >> final[i][j];
                a[i][j] = 100;
            }
        }
        if(cal()){
            cout << "YES";
        }
        else
            cout << "NO";

        cout << endl;
	}
	return 0;
}
