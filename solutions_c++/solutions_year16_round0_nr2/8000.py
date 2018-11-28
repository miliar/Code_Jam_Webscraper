#include<iostream>
#include<fstream>
#include<string>
using namespace std;
bool checkString(string& str){

    for(int i = 0; i < str.size(); ++i){
        if(str[i] == '-'){
            return false;
        }
    }
    return true;

}

void change(string& str, char ch, int endr){

    for(int i = 0; i <= endr; ++i)
        str[i] = ch;

}
bool allAreNeg(string& str){

    for(int i = 0; i < str.size(); ++i)
        if(str[i] == '+')
            return false;
    return true;
}
int main(){

    int T, counter = 0, endr;
    string str;
    bool check = false;
    ifstream cinf("B-large.in");
    ofstream coutf("output.txt");
    cinf>>T;

    for(int i = 1; i <= T; ++i){
        counter = 0;

        cinf>>str;

        for(int j = 0; j < str.size(); ++j){
            if(checkString(str))
                break;
            else{
                ++counter;

                for(int k = 0; k < str.size(); ++k){

                    if((str[k] != str[0]) || (k == str.size() - 1)){
                        endr = k;
                        break;
                    }
                }
                if(allAreNeg(str)){
                    break;
                }
                change(str, str[endr], endr);
            }
        }

        coutf<<"Case #"<<i<<": "<<counter<<endl;
    }

}
