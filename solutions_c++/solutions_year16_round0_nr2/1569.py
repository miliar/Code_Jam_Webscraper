#include <iostream>
#include <string>

using namespace std;

int flipTime(string pattern);

int main(){

    int numOfTest = 0;
    int count = 0;
    string line;

    if(getline(cin, line)){
        numOfTest = stoi(line);
    }
    else{
        cout << "No testcase is specified.\n";
        return 1;
    }

    while(getline(cin, line)) {
        int result = flipTime(line);
        cout << "Case #" << ++count << ": " << result << endl;
    }

    return 0;
}

int flipTime(string pattern){

    string converted = "";
    int length = pattern.size();
    int idx = 0;
    char last = '*';

    if(length == 0)
        return 0;

    while(idx < length){
        if(last != pattern[idx]){
            converted += pattern[idx];
        }
        last = pattern[idx];
        idx++;
    }

    int newLength = converted.size();
    if(last == '-')
        return newLength;
    else
        return newLength - 1;
}

