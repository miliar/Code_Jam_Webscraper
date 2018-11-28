#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    while(T--){
        int firstRow, secondRow;
        int firstLine[4], secondLine[4];
        int emptyNum;
        cin >> firstRow;
        for(int i = 1; i < firstRow; i++){
            for(int j = 0; j < 4; j++)
                cin >> emptyNum;
        }
        for(int i = 0; i < 4; i++)
            cin >> firstLine[i];
        for(int i = firstRow; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> emptyNum;

        cin >> secondRow;
        for(int i = 1; i < secondRow; i++){
            for(int j = 0; j < 4; j++)
                cin >> emptyNum;
        }
        for(int i = 0; i < 4; i++)
            cin >> secondLine[i];
        for(int i = secondRow; i < 4; i++)
            for(int j = 0; j < 4; j++)
                cin >> emptyNum;

        int flag = 0; // 1,2,3 for three cases
        int sameNum = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++)
            {
                if(firstLine[i] == secondLine[j]){
                    if(sameNum != 0){
                        flag = 2;
                        break;
                    }
                    sameNum = firstLine[i];
                }
            }
            if(flag == 2)
                break;
        }

        if(flag == 2)
            cout << "Case #"<< 100 - T<<": Bad magician!" << endl;
        else if(sameNum != 0)
            cout << "Case #"<< 100 - T<<": " << sameNum << endl;
        else
            cout << "Case #"<< 100 - T<<": Volunteer cheated!" << endl;


    }
    return 0;
}
