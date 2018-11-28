#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;

int main(){

ifstream in ("input.txt");
ofstream out("output.txt");
int x;
in>>x;

string s;
getline (in,s);
for(int i=0;i<x;i++)
{
    string word;
    getline(in,s);
    stringstream ss;
    ss<<s;
    string ch;
    while(ss>>ch)
    {
        word.insert(0,ch);
        word.insert(0," ");
    }
    cout<<"Case #"<<i+1<<":";
    for(int k=0;k<word.size();k++)
        cout<<word[k];
    cout<<endl;
}


return 0;
}
