#include <iostream>
#include <fstream>
long long  k =1;
using namespace std;
int main(){
        long long t,n,m,a[5][5],b[5][5],i,j,x;
        cin >> t;
        ofstream myfile;
        myfile.open ("abc.txt");
  //myfile << "Writing this to a file.\n";
 // myfile.close();
        while(t--){
            cin >> n;
            for(i=1; i<=4; i++){
                for(j=1; j<=4; j++){
                    cin >> a[i][j];
                }
            }
                cin >> m;
             for(i=1; i<=4; i++){
                for(j=1; j<=4; j++){
                    cin >> b[i][j];
                }
            }
            long long cnt = 0;
            for(i=1; i<=4; i++){
                    for (j=1;j<=4;j++){
                        if(a[n][i] == b[m][j]){
                        x = a[n][i];
                        cnt++;
                        }
                    }
            }
            myfile << "Case #" << k << ": ";
            k++;
            if(cnt < 1)
                myfile << "Volunteer cheated!\n";
            else if(cnt > 1)
                myfile  << "Bad magician!\n";
            else if(cnt == 1)
                myfile<< x << "\n";


        }
        myfile.close();
return 0;
}
