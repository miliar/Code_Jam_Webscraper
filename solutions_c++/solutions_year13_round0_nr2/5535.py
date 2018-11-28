#include <fstream>
#include <iostream>

using namespace std;

int main(){
   
    int t;
    ifstream input("input.txt");
    ofstream output("output.txt");
    input>> t;
    
    int l = 1;
    
    while(l<=t){
        int n,m;
        
        input>>n>>m;
        int** arr = new int*[n];
        
        for(int i=0; i<n; i++){
            arr[i] = new int[m];
            for(int j=0; j<m; j++){
                input >> arr[i][j];
            }         
        }
        
        
        int flag = false;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
               
               int r= arr[i][j];
               bool hasColumnBigger = false;
               for(int k=0; k<n; k++){
                   if(arr[k][j] > r){
                      hasColumnBigger = true;
                   }
               }
               
               bool hasRowBigger = false;
               for(int k=0; k<m; k++){
                   if(arr[i][k] > r){
                      hasRowBigger = true;
                   }
               }
               
               if(hasColumnBigger && hasRowBigger){
                   flag = true;
                   break;
               }
                  
            }
            if(flag){
               break;
            }
        }
        if(flag)
           output<<"Case #"<< l<< ": NO"<<endl;
        else
           output<<"Case #"<< l<< ": YES"<<endl;
           
        l++;
    }
    system("pause");
}
