#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
    int T, pos;
    string str;
    vector<int> number;

    cin >> T;
    for(int caso=1;caso<=T;caso++){
        cin >> str;
        number.clear();

        while( (pos=str.find_first_of('Z')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('E'), 1);
            str.erase(str.find_first_of('R'), 1);
            str.erase(str.find_first_of('O'), 1);
            number.push_back(0);
        }
        while( (pos=str.find_first_of('W')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('T'), 1);
            str.erase(str.find_first_of('O'), 1);
            number.push_back(2);
        }
        while( (pos=str.find_first_of('X')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('S'), 1);
            str.erase(str.find_first_of('I'), 1);
            number.push_back(6);
        }
        while( (pos=str.find_first_of('G')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('E'), 1);
            str.erase(str.find_first_of('I'), 1);
            str.erase(str.find_first_of('H'), 1);
            str.erase(str.find_first_of('T'), 1);
            number.push_back(8);
        }
        while( (pos=str.find_first_of('H')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('T'), 1);
            str.erase(str.find_first_of('R'), 1);
            str.erase(str.find_first_of('E'), 1);
            str.erase(str.find_first_of('E'), 1);
            number.push_back(3);
        }
        while( (pos=str.find_first_of('S')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('E'), 1);
            str.erase(str.find_first_of('V'), 1);
            str.erase(str.find_first_of('E'), 1);
            str.erase(str.find_first_of('N'), 1);
            number.push_back(7);
        }
        while( (pos=str.find_first_of('R')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('F'), 1);
            str.erase(str.find_first_of('O'), 1);
            str.erase(str.find_first_of('U'), 1);
            number.push_back(4);
        }
        while( (pos=str.find_first_of('V')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('F'), 1);
            str.erase(str.find_first_of('I'), 1);
            str.erase(str.find_first_of('E'), 1);
            number.push_back(5);
        }
        while( (pos=str.find_first_of('O')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('N'), 1);
            str.erase(str.find_first_of('E'), 1);
            number.push_back(1);
        }
        while( (pos=str.find_first_of('I')) != string::npos ){
            str.erase(pos, 1);
            str.erase(str.find_first_of('N'), 1);
            str.erase(str.find_first_of('N'), 1);
            str.erase(str.find_first_of('E'), 1);
            number.push_back(9);
        }

        cout << "Case #" << caso << ": ";
        sort(number.begin(), number.end());
        for(int i=0;i<number.size();i++)
            cout << number[i];
        if( caso < T )
            cout << endl;
    }

    return 0;
}
