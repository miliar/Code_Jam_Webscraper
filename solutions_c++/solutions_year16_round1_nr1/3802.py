#include <iostream>
#include <string>

using namespace std;

void printS(string s, char first, string atStart, string atEnd){
   if (s.length() == 0){
         cout << atStart << atEnd; 
        return;
    }
    if (s[0] >= first){
        printS(s.substr(1), s[0], s.substr(0,1).append(atStart),  atEnd);
    }else{
    //    cout << endl << s << " " << atEnd << endl;
        printS(s.substr(1), first, atStart, atEnd.append(s.substr(0,1)));
    }

}

int main(){
int cases;
cin >> cases;
string S;

for (int j = 0; j < cases; j++){
    cin >> S;
    cout << "Case #" << j+1 << ": "; 
    printS(S, 'A', "", "");
    cout << endl;
}



}
