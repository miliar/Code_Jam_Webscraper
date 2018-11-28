#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int T;
    in >> T;

    string str;
//    for(int i = 0; i < T; i++) {
//        cin >> str;

//        int count = 0;
//        size_t found = str.find_last_of("-");

//        while(found != string::npos) {

//            for(size_t i = 0; i <= found; i++) {
//                str[i] = (str[i] == '-' ? '+' : '-');
//            }
//            count++;

//            found = str.find_last_of("-");
//        }

//        cout << "Case #" << i+1 << ": " << count << "\n";
//    }

    for(int i = 0; i < T; i++) {
        in >> str;

        int countP = 0;

        if(str[0] == '-') {
            countP = -1;
        }

        int countMinus = 0;

        for(int i = 0; i < str.size(); i++) {
            if(str[i] == '-' && str[i+1] == '+') {
                countMinus++;
            }
        }

        if(str[str.size() - 1] == '-') {
            countMinus++;
        }

        countP += countMinus * 2;

        out << "Case #" << i+1 << ": " << countP << "\n";
    }

    return 0;
}
