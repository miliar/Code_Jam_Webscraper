# include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    
    for (int k = 0; k < t; k++){
        
             int n,m;
             cin >> n >> m;
             
             int a[n][m];
             int b[n][m];
             
             for (int i = 0; i < n; i++){
                 for (int j = 0; j < m; j++){
                     cin >> a[i][j];
                     b[i][j] = 100;
                 }
             }
             int max,max1;
             
             for (int i = 0; i < n; i++){
                 max = a[i][0];
                 max1 = b[i][0];
                 for (int j = 1; j < m; j++){
                     if(a[i][j] > max)
                                max = a[i][j];
                     if(b[i][j] > max1){
                                max1 = b[i][j];
                     }
                 }
                 if(max != max1){
                 for (int j = 0; j < m; j++){
                     b[i][j] = max;
                 }
                 }
             }
             
             for (int j = 0; j < m; j++){
                 max = a[0][j];
                 max1 = b[0][j];
                 for (int i =  0; i < n; i++){
                     if(a[i][j] > max)
                                 max = a[i][j];
                     if(b[i][j] > max1)
                                max1 = b[i][j];
                 }
                 
                 if(max != max1){
                 for (int i = 0; i < n; i++){
                     b[i][j] = max;
                 }
                 }
             }
             bool flag = false;
             cout << "Case #" <<k+1 <<": " ;
             for (int i = 0; i < n; i++){
                 for (int j = 0; j < m; j++){
                     if(a[i][j] != b[i][j]){
                               flag = true;
                     }
                     
                     if(flag) break;
                 }
                 if(flag) break;
             }
             
             if(flag) cout << "NO" << endl;
             else cout << "YES" << endl;             
        }
        
        return 0;
        }
