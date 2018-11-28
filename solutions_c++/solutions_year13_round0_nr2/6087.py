#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;
int main(){
    ifstream fin("B-small-attempt2.in");
    ofstream fout("output.out");
    
    int cases;
    fin>>cases;
    
    for(int i=0; i<cases; i++)
    {
        int m, n;
        fin>>m>>n;
        
        
        int lawn[m][n];
        for(int j=0; j<m; j++)
            for(int k=0; k<n; k++)
                lawn[j][k] = 2;
                
        int lawnideal[m][n];
        
        for(int j=0; j<m; j++)
            for(int k=0; k<n; k++)
                fin>>lawnideal[j][k];
    
        /*for(int j=0; j<m; j++){
            for(int k=0; k<n; k++)
                fout<<lawnideal[j][k]<<" ";
            fout<<endl;
        }
        fout<<endl;
        */
        for(int j=0; j<m; j++)
        {
            bool equal = true;
            for(int k=1; k<n; k++){
                if(lawnideal[j][0] != lawnideal[j][k]){
                    equal = false;
                    break;   
                } 
            }
            if(equal)
            {
                for(int k=0; k<n; k++)
                {
                    lawn[j][k] = lawnideal[j][0];   
                }   
            }
        }
        
        for(int j=0; j<n; j++)
        {
            bool equal = true;
            for(int k=1; k<m; k++){
                if(lawnideal[0][j] != lawnideal[k][j]){
                    equal = false;
                    break;   
                } 
            }
            if(equal)
            {
                for(int k=0; k<m; k++)
                {
                    lawn[k][j] = lawnideal[0][j];   
                }   
            }
        }
        string y= "YES";
        for(int j=0; j<m; j++){
            for(int k=0; k<n; k++){
                if(lawn[j][k] != lawnideal[j][k])
                {
                    y= "NO";
                }
            }  
        }
        
        /*for(int j=0; j<m; j++){
            for(int k=0; k<n; k++)
                fout<<lawn[j][k]<<" ";
            fout<<endl;
        }
        */
        fout<<"Case #"<<i+1<<": "<<y<<endl;
    }
    fin.close();
    fout.close();
    //system("pause");
    return 0;   
}
