#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> numbers =
{
"ZERO",
"ONE",
"TWO",
"THREE",
"FOUR",
"FIVE",
"SIX",
"SEVEN",
"EIGHT",
"NINE"
};

void erase(string& str, string number){
    int pos;
    for (int i = 0; i < number.size(); ++i){
        pos = str.find(number[i]);
        if (pos == string::npos){
            cout<<"stiring "<<number<<" not found! \n";
            return;
        }
        str.erase(pos,1);
    }
}

string solve(string str){
    vector<char> res;
    int pos;
    while(str.find('Z')!= string::npos ||
          str.find('W')!= string::npos ||
          str.find('U')!= string::npos ||
          str.find('X')!= string::npos ||
          str.find('G')!= string::npos)
    {
        pos = str.find('Z');
        if (pos != string::npos){
            res.push_back('0');
            erase(str,"ZERO");
            //cout<<"Z "<<str<<endl;
        }
        pos = str.find('W');
        if (pos != string::npos){
            res.push_back('2');
            erase(str,"TWO");
        }
        pos = str.find('U');
        if (pos != string::npos){
            res.push_back('4');
            erase(str,"FOUR");
        }
        pos = str.find('X');
        if (pos != string::npos){
            res.push_back('6');
            erase(str,"SIX");
        }
        pos = str.find('G');
        if (pos != string::npos){
            res.push_back('8');
            erase(str,"EIGHT");
        }
    }
    while(str.find('O')!= string::npos ||
          str.find('T')!= string::npos ||
          str.find('F')!= string::npos ||
          str.find('S')!= string::npos)
    {
        pos = str.find('O');
        if (pos != string::npos){
            res.push_back('1');
            erase(str,"ONE");
        }
        pos = str.find('T');
        if (pos != string::npos){
            res.push_back('3');
            erase(str,"THREE");
        }
        pos = str.find('F');
        if (pos != string::npos){
            res.push_back('5');
            erase(str,"FIVE");
        }
        pos = str.find('S');
        if (pos != string::npos){
            res.push_back('7');
            erase(str,"SEVEN");
        }
    }
    while(str.find('I')!= string::npos){
        pos = str.find('I');
        res.push_back('9');
        erase(str,"NINE");
    }
    if (str.size() != 0){
        cout<<"str not empty! "<<str<<endl;
    }
    sort(res.begin(), res.end());
    string ret;
    for (int i = 0; i < res.size(); ++i){
        ret += res[i];
    }
    return ret;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int T;
    string S;
    in >> T;
    for (int i = 1; i <= T; ++i){
        in >> S;
        out<<"Case #"<<i<<": "<<solve(S)<<endl;
    }
    return 0;
}

