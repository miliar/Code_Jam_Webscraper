#include <fstream>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;
int main(){
       ifstream cin("in.txt");
       ofstream cout("out.txt");
       int n;
       cin >> n ;
       for(int i = 0 ; i < n; i++){
               int m, n;
               cin >> m >> n;
               int mat[m][n];
               int mayorfila[m];
               int mayorcolumna[n];
               for(int j= 0; j <n ; j++){
                       mayorcolumna[j]=0;
               }
               for(int i= 0; i <m ; i++){
                       mayorfila[i]=0;
                       for(int j= 0; j <n ; j++){
                               cin >> mat[i][j];
                               if(mat[i][j]>mayorfila[i]){
                                       mayorfila[i] = mat[i][j];
                               }
                               if(mat[i][j]>mayorcolumna[j]){
                                       mayorcolumna[j] = mat[i][j];
                               }
                       }
               }
               bool b = false; 
               cout << "Case #" << i+1 << ": ";
               for(int i= 0; i <m ; i++){
                   for(int j= 0; j <n ; j++){
                           if(mat[i][j] < mayorfila[i] && mat[i][j] < mayorcolumna[j]){
                                        cout <<  "NO" << endl;
                                        b = true;
                                        break;
                           }              
                   }
                   if(b){
                          break;
                   }
               }
               if(!b){
                      cout << "YES" << endl;
               }
               
       }
}
