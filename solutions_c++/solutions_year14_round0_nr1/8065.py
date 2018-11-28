#include <iostream>
#include <vector>
using namespace std;

void probA();

int
main(void){
    int nTest;
    
    cin >> nTest;
    
    for(int i = 1; i <= nTest; i++){
        cout << "Case #" << i << ": ";
        probA();
    }
}

void probA(){
    int cards1[4][4];
    int cards2[4][4];
    int row1, row2;
    
    // Read Row
    cin >> row1;
    
    // Read cards
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cin >> cards1[j][i];
        }
    }
    
    // Read Row
    cin >> row2; 
    
    // Read cards
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cin >> cards2[j][i];
        }
    }
    
    vector <int> poss1;
    for(int i = 0; i < 4; i++){
        poss1.push_back(cards1[i][row1-1]);
    }
    vector <int> poss2;
    for(int i = 0; i < 4; i++){
        poss2.push_back(cards2[i][row2-1]);
    }
    
    vector <int> intersect;
    for(int i = 0; i < 4; i++){
        if(find(poss2.begin(), poss2.end(), poss1[i]) != poss2.end()){
            intersect.push_back(poss1[i]);
        }
    }
    
    if(intersect.size() == 0){
        cout << "Volunteer Cheated!" << endl;
    }
    else if(intersect.size() == 1){
        cout << intersect[0] << endl;
    }
    else{
        cout << "Bad Magician!" << endl;
    }
}
