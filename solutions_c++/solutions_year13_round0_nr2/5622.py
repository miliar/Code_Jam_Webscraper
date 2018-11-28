#include <iostream>
#include <fstream>

using namespace std;

int main() {

  ofstream file;
  file.open ("Output.txt");

  int t, n, m;

  cin >> t;

  for(int k=1; k<=t; k++){

    cin >> n >> m;
    bool arr1[n][m];
    int cont1=0;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            int aux;
            cin >> aux;
            if(aux==1){
                arr1[i][j]=true;
                cont1++;
            } else {
                arr1[i][j]=false;
            }
        }
    }

    if(cont1==n*m||cont1==0){
        file << "Case #" << k << ": " << "YES" << endl;
    } else {

        bool arr2[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr2[i][j]=false;
            }
        }
        bool crash=false;

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(arr1[i][j]==true && arr2[i][j]==false){

                    bool filaOK=true;
                    for(int r=0; r<m; r++){
                        if(arr1[i][r]==false){
                            filaOK=false;
                            break;
                        }
                    }

                    bool colOK=true;
                    for(int r=0; r<n; r++){
                        if(arr1[r][j]==false){
                            colOK=false;
                            break;
                        }
                    }

                    if(filaOK){
                        for(int x=0; x<m; x++){
                            arr2[i][x]=true;
                        }
                    }

                    if(colOK){
                        for(int x=0; x<n; x++){
                            arr2[x][j]=true;
                        }
                    }

                    if(!filaOK&&!colOK){
                        crash=true;
                    }

                }

                if(crash) break;
            }
            if(crash) break;
        }
        if(crash){
            file << "Case #" << k << ": " << "NO" << endl;
        } else {
            file << "Case #" << k << ": " << "YES" << endl;
        }
    }

  }

  file.close();

  return 0;
}
