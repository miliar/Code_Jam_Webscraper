#include <iostream>
#include <fstream>

using namespace std;

void magic() {
    ifstream file("/Users/sborkar/input.in");
    int T, first, second, arr_1[4][4], arr_2[4][4], num;
    bool found,multiple;
    
    file >> T;
    for(int k =0 ; k<T ; k++) {
        file >> first;
        first-=1;
        for(int i=0; i<4; i++)for(int j=0; j<4; j++)file >> arr_1[i][j];
        file >> second;
        second-=1;
        for(int i=0; i<4; i++)for(int j=0; j<4; j++)file >> arr_2[i][j];

        found=false;
        multiple=false;
        for(int i=0; i<4; i++)for(int j=0; j<4; j++) {
            if(arr_1[first][i]==arr_2[second][j]) {
                if(found){multiple=true;break;}
                found=true;num=arr_1[first][i];
            }
        }
        cout<<"Case #" << k << ": ";
        if(!found)cout<<"Volunteer cheated!";
        else if(multiple)cout<<"Bad magician!";
        else cout<<num;
        cout<<endl;
    }
}

int main() {
    magic();
}