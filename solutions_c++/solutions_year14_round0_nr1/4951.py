#include <iostream>
#include <cstdio>
using namespace std;

int card1[4][4];
int card2[4][4];
int cRow[4];
int main(){
    int n;
    int sc1;
    int sc2;
    int sCardRow1;
    int sCardRow2;
    int sCard;
    bool found;
    bool badMagic;
    
    cin >> n;
    for(int curr=1;curr<=n;curr++){
        sCard = -1;
        found = false;
        badMagic = false;
        cin >> sCardRow1;
        
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                
                cin >> card1[i][j];
                
            }
        }
        cin >> sCardRow2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin >> card2[i][j];
            
            }
        }
        
        sCardRow1--;
        sCardRow2--;
        
        for(int i=0;i<4;i++){
            cRow[i] = card1[sCardRow1][i];
        }
        
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(card2[sCardRow2][i] == cRow[j]){
                    if(found){
                        badMagic = true;
                        break;
                    }
                    else{
                        found = true;
                        sCard = card2[sCardRow2][i];
                    
                        //
                        //cout << sCard << endl;
                    }
                }
            }
        }
        
        /*cout << "sCardRow1: " << sCardRow1 << endl;
        cout << "sCardRow2: " << sCardRow2 << endl;
        cout << "sCard: " << sCard << endl;*/
        
        
        if(badMagic){
            printf("Case #%d: Bad magician!\n",curr);
        }
        else if(found){
            printf("Case #%d: %d\n",curr,sCard);
        }
        else{
            printf("Case #%d: Volunteer cheated!\n",curr);
            
        }
        // cout << "Case #" << i << ": " << result << endl;
        
    }
}