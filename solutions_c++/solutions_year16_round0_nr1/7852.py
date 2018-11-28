#include <iostream>
#include <set>
#include <string>
#include <sstream>


using namespace std;
string ConToS(int x);


int main() {
set<char > Numbers;
int N,Num,Num2,j=2;
string Nu;
cin >> N;
for (int i = 0 ; i < N ; i++){
cin>>Num;
Num2=Num;
start:
Nu=ConToS(Num2);
for (int k = 0 ; k < Nu.length();k++){
Numbers.insert(Nu[k]);
}
if (Numbers.size()==10){cout<<"Case #"<<i+1<<": "<<Num2<<endl;}
else if (Num==0){cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;}
else{Num2=Num*j;j++;goto start;}
Numbers.clear();
j=2;
}
}//main

string ConToS(int x){
stringstream SS;
string Out;
SS << x;
Out=SS.str();
return Out;
}
