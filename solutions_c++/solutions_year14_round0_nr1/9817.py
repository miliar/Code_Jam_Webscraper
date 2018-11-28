#include <iostream>
#include <vector>

using namespace std;

int* readCards(){
    int *possible = new int[4];
    int m;
    cin>>m;
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            int c;
            cin>>c;
            if(m-1 == i){
                possible[j] = c;
            }
        }
    }
    return possible;

}

void solve(int testNr){

    int *possibleFirst = readCards();
    int *possibleSecond = readCards();
    int same = 0;
    int magicNum;
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            if(possibleFirst[i] == possibleSecond[j]){
                same++;
                magicNum = possibleFirst[i];
            }
        }
    }
    cout<<"Case #"<<testNr<<": ";
    if(same == 0){
         cout<<"Volunteer cheated!"<<endl;
    } else if(same == 1){
        cout<<magicNum<<endl;
    }else if(same >= 2){
        cout<<"Bad magician!"<<endl;
    }
    delete possibleFirst;
    delete possibleSecond;
}

int main()
{
    int tests;
    cin>>tests;
    for(int i=0; i<tests; i++){
        solve(i+1);
    }
    return 0;
}
