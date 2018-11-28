#include <iostream>
#include <string>

using namespace std;

int main() {

bool IsSmile=true;
int T,Result=0,C=0;
string S1,S2;

cin >> T;
cin.ignore();
for (int i = 0 ; i < T ; i++){//For#1

getline(cin,S1);

for (int j = 0 ; j < S1.length() ; j++){
if (S1[j]!='-'){C++;}
}//For#2

start:
if (C==S1.length()){}
else if (S1[0] == '+'){
for (int j = 0 ; j < S1.length() ; j++){
if (S1[j]=='-' && IsSmile==true){for (int k=0;k <j;k++){S1[k]='-';}IsSmile=false;}
if (IsSmile==false){IsSmile=true;break;}
}//For#2
Result++;
}//If#1

else if (S1[0] == '-' && S1[S1.length()-1]=='-'){S2=S1;
for (int k=0;k <S1.length();k++){if (S1[k]=='-'){
S2[S1.length()-1-k]='+';}
else {S2[S1.length()-1-k]='-';}}
S1=S2;
Result++;
}//If#2

else if (S1[0] == '-' && S1[S1.length()-1]=='+'){
for (int j = 0 ; j < S1.length() ; j++){
if (S1[j]=='+'){for (int k=0;k <j;k++){S1[k]='+';}IsSmile=false;}
if (IsSmile==false){IsSmile=true;break;}
}//For#2
Result++;
}//If#3

for (int j = 0 ; j < S1.length() ; j++){
if (S1[j]=='-'){IsSmile=false; break;}
}//For#2

if (IsSmile == true){cout << "Case #"<<i+1<<": "<<Result<<endl;}
else {IsSmile=true;goto start;}

Result=0;
IsSmile=true;
C=0;
}//For#1

}//main

