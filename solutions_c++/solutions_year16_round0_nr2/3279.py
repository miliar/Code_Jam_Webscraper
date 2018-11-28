#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin ("B-large.in");
ofstream fout ("pancake.out");

int T;
string s;

long flip(string t){
//cout << t << endl;
if(t.length()==0)return 0;

//remove ++ at bottom
else if(t[t.length()-1]=='+'){
    long long i =t.length()-1;
    for(i=t.length()-1;i>=0;i--){
        if(t[i]=='-')break;
    }
    if(i==-1)return 0;
    string k;
    for(long long j=0;j<=i;j++){
        k+=t[j];
    }
    return flip(k);
}
//flip prefix +++ to ---
else if(t[0]=='+'){
    t[0]='-';
    long long i=1;
    for(i=1;i<t.length();i++){
        if(t[i]=='-')break;
        t[i]='-';
    }
    if(i==t.length())return 0;
    return 1+flip(t);
}

//flip longest -----
else{
    long long i=1;
    for(i=1;i<t.length();i++){
        if(t[i]=='+')break;
        }

    //all ----
    if(i==t.length())return 1;

    string k;
    for(long long l=t.length()-1;l>=i;l--){
        if(t[l]=='+')k+='-';
        else{ k+='+';}
    }
    return 1+flip(k);
}
}
int main(){
fin >> T;
for(int i=1;i<=T;i++){
    fin >> s;
    //cout << i << endl;
    fout << "Case #" << i << ": " << flip(s) << endl;
    }

}
