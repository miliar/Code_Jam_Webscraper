#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

int cards1[4][4];
int cards2[4][4];
int row1, row2;

void loadCards(int cards[][4], fstream& f){
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            f >> cards[i][j];
        }
    }
}

void print(int cards[][4]){
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            cout << cards[i][j] << " ";
        }
        cout <<endl;
    }
}

void test(int t, fstream& result){
    int count = 0;
    int index = 0;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++){
            if(cards1[row1][j] == cards2[row2][i]){
                count++;
                index = i;
            }
        }
    }
    result << "Case #" << t << ": ";
    if(count == 0){
        result << "Volunteer cheated!" << endl;
    }else if(count == 1){
        result << cards2[row2][index] << endl;
    }else{
        result << "Bad magician!" << endl;
    }
}

int main(int argc, char** argv)
{
    std::fstream f;
    std::fstream result;
    result.open("result.txt",std::fstream::out);
    f.open (argv[1], std::fstream::in);

    std::string l;
    int T; f >> T;

    for(int t = 1; t <= T; t++){

        f >> row1;row1--;
        loadCards(cards1,f);

        f >> row2;row2--;
        loadCards(cards2,f);

        test(t,result);
    }

    f.close();
    result.close();
    return 0;
}



