#include <iostream>
#include <string>

using namespace std;

string decode(string code);

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

        string result = decode(line);
        cout << "Case #" << ++count << ": " << result << endl;
    }
    return 0;
}

string decode(string code){
    int table[26] = {0,};
    int count[10] = {0,};
    int length = code.size();
    int temp;

    for(int i = 0; i < length; i++){
        table[code[i]-'A']++;
    }

    temp = table['Z'-'A'];
    count[0] = temp;
    table['R'-'A'] -= temp;
    table['O'-'A'] -= temp;

    
    temp = table['G'-'A'];
    count[8] = temp;
    table['I'-'A'] -= temp;

    
    temp = table['W'-'A'];
    count[2] = temp;
    table['O'-'A'] -= temp;


    temp = table['X'-'A'];
    count[6] = temp;
    table['S'-'A'] -= temp;
    table['I'-'A'] -= temp;


    temp = table['S'-'A'];
    count[7] = temp;
    table['V'-'A'] -= temp;
    table['E'-'A'] -= temp;
    table['N'-'A'] -= temp;


    temp = table['V'-'A'];
    count[5] = temp;
    table['F'-'A'] -= temp;
    table['I'-'A'] -= temp;


    temp = table['F'-'A'];
    count[4] = temp;
    table['O'-'A'] -= temp;
    table['R'-'A'] -= temp;


    temp = table['R'-'A'];
    count[3] = temp;

    
    temp = table['I'-'A'];
    count[9] = temp;
    
    
    temp = table['O'-'A'];
    count[1] = temp;

    string result = "";
    for(int i = 0; i < 10; i++)
        for(int j = 0; j < count[i]; j++)
            result += ('0' + i);

    return result;

}
