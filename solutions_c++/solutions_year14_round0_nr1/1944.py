#include <iostream>
#include <fstream>

using namespace std;
ifstream inp;
ofstream oup;
int main(){
    int T;
    int array[4][4];
    inp.open("input.in");
    oup.open("output.txt");
    inp>>T;
    int choice;
    int pos[4];
    int sop[4];
    for (int t=0; t<T; t++){
        inp>>choice;
        for (int j=0; j<4; j++){
            for (int k=0; k<4; k++){
                inp>>array[j][k];
                if (j==choice-1){
                   pos[k]=array[j][k];             
                }    
            }    
        }
        inp>>choice;
        for (int j=0; j<4; j++){
            for (int k=0; k<4; k++){
                inp>>array[j][k];
                if (j==choice-1){
                   sop[k]=array[j][k];             
                }    
            }    
        }
        
        
        int cnt=0;
        int urray[4][4];
        for (int i=0; i<4; i++){
            for (int j=0; j<4; j++){
                urray[i][j]=0;        
            }
        }
        int blah=-1;
        for (int i=0; i<4; i++){
            for (int j=0; j<4; j++){
                if (sop[i]==pos[j]){
                   urray[i][j]=1;
                   blah=pos[j];                   
                }
            }    
        }
        for (int i=0; i<4; i++){
            for (int j=0; j<4; j++){
                cnt+= urray[i][j];        
            }
        }
        if (cnt==1) oup<<"Case #"<<t+1<<": "<<blah<<endl;
        else if (cnt==0) oup<<"Case #"<<t+1<<": Volunteer Cheated!"<<endl;
        else oup<<"Case #"<<t+1<<": Bad Magician!"<<endl;
          
    }
    
    
}
