#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    ifstream file_stream;
    file_stream.open(argv[1]);
    std::string line;
    getline(file_stream, line);
    char* str = new char[line.length() + 1];
    strcpy(str, line.c_str());
    int num = atoi(strtok(str, " "));
    delete[] str;
    for(int i = 0; i < num; ++i){
        getline(file_stream, line);
        char* st = new char[line.length() + 1];
        strcpy(st, line.c_str());
        int row1 = atoi(strtok(st, " "));
        vector<int> cards;
        delete[] st;
        for(int j = 0; j < 4; ++j){
            getline(file_stream, line);
            st = new char[line.length() + 1];
            strcpy(st, line.c_str());
            int x = atoi(strtok(st, " "));
            cards.push_back(x);
            for(int k = 0; k < 3; ++k){
                x = atoi(strtok(0, " "));
                cards.push_back(x);
            }
            delete[] st;
        }
        getline(file_stream, line);
        char* foo = new char[line.length() + 1];
        strcpy(foo, line.c_str());
        int row2 = atoi(strtok(foo, " "));
        delete[] foo;
        vector<int> cards2;
        for(int j = 0; j < 4; ++j){
            getline(file_stream, line);
            foo = new char[line.length() + 1];
            strcpy(foo, line.c_str());
            int x = atoi(strtok(foo, " "));
            cards2.push_back(x);
            for(int k = 0; k < 3; ++k){
                x = atoi(strtok(0, " "));
                cards2.push_back(x);
            }
        }
        vector<int> temp;
        vector<int> temp2;
        int index = (row1 - 1) * 4;
        int index2 = (row2 - 1) * 4;
        for(int j = 0; j < 4; ++j){
            temp.push_back(cards[index]);
            temp2.push_back(cards2[index2]);
           // cout << cards[index] << endl;
          //  cout << cards2[index2] << endl;
            index++;
            index2++;
        }
        vector<int> in_common;
        for(int j = 0; j < 4; ++j){
            int z = temp[j];
            for(int k = 0; k < 4; ++k){
                if(temp2[k] == z){
                    in_common.push_back(z);
                    break;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if(in_common.size() == 0){
            cout << "Volunteer cheated!" << endl;
        }
        else if(in_common.size() == 1){
            cout << in_common[0] << endl;
        }
        else{
            cout << "Bad magician!" << endl;
        }
    }
}
