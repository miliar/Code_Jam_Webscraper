#include <iostream>
#include <fstream>
#include <String>

using namespace std;

int T;


ifstream fin("wordLarge.in");
ofstream fout("wordLarge.out");

void calc(string s){
    string newS = "";
    char firstLetter = s[0];
    newS += firstLetter;
    for(int i = 1; i < s.length(); i++){
        if(s[i] >= firstLetter){
            newS.insert(0, 1, s[i]);
            firstLetter = s[i];
        }else{
            newS += s[i];
        }
    }
    fout<<newS<<"\n";
}

int main(){
    fin>>T;
    string S;
    for(int t = 1; t <= T; t++){
        fout<<"Case #"<<t<<": ";
        fin>>S;
        calc(S);
    }
    fin.close();
    fout.close();
}
