#include <iostream>
#include <fstream>

#include <conio.h>

using namespace std;

int main ()
{
    ifstream fin;
    fin.open ("A-in.txt");
    ofstream fout;
    fout.open ("A-out.txt");
    
    
    int t, r1, r2, arr1[4][4], arr2[4][4], ans;
    
    fin>>t;
    for (int i=1;i<=t;i++){
        fin>>r1;
        for (int j=0;j<4;j++)
            for (int k=0;k<4;k++)
                fin>>arr1[j][k];
                
        fin>>r2;
        for (int j=0;j<4;j++)
            for (int k=0;k<4;k++)
                fin>>arr2[j][k];
                
        int match=0;        
        for (int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                //cout<<arr2[r2-1][k]<<" ";
                if (arr1[r1-1][j]==arr2[r2-1][k]){
                   ans=arr1[r1-1][j];
                   match++;
                }
            }     
        }            
        fout<<"Case #"<<i<<": ";    
        if (match==0)
           fout<<"Volunteer cheated!"<<endl;
        else if (match==1)
             fout<<ans<<endl;
        else fout<<"Bad magician!"<<endl;
        
    }         
    
    getch ();
}
