#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

vector<int> pierwszy;
vector<int> drugi;
bool duplicates[17];
int pokrywa_sie=-1;
int znalezione=0;

void clear(){
    pierwszy.clear();
    drugi.clear();
    pokrywa_sie=-1;
    znalezione=0;
    memset(duplicates, 0, sizeof(duplicates) );
}


int main(){
    ios_base::sync_with_stdio(0);
    
    int testy;
    cin>>testy;
    
    for(int t=1; t<=testy; t++){
        clear();
        int rzad;
        
        for(int k=0; k<=1; k++){
            cin>>rzad;
        
            for(int i=1; i<=4; i++){
                for(int j=1; j<=4; j++){
                    int number;
                    cin>>number;
                
                    if(i==rzad){
                        if(duplicates[number]==true){
                            pokrywa_sie=number;
                            znalezione++;
                        }
                        duplicates[number]=true;
                    }
                }
            }
        }
        
        cout<<"Case #"<<t<<": ";
        if(znalezione==0){
            cout<<"Volunteer cheated!\n";
        }
        else if (znalezione==1){
            cout<<pokrywa_sie<<"\n";
        }
        else if (znalezione>=2){
            cout<<"Bad magician!\n";
        }
    }
    
    
    return 0;
}