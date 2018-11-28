# include <iostream>
# include <string>
# include <cstdio>
#include <fstream>
using namespace std;
int guests(string s){
int gue=0,present=0;

for(int i=0;i<s.length();i++){
    if(s[i]>48){
    if(i>present){gue+=i-present;present=i+s[i]-48;}
    else{present=present+s[i]-48;}
   // cout<<gue<<present<<endl;
    }
    else{}
}
return gue;
}





int main(){

ifstream fin("A-large.in");
ofstream fout("output.out");

if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
int cases,smax,t=1;
fin>>cases;
string input;
while(cases--){
    fin>>smax>>input;
    fout<<"Case #"<<t<<": "<<guests(input)<<endl;

t++;
}


}







