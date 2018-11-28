#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
int GetMinFlips(string input);
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
    int T;
    string input;
    fin>>T;
    for(int i=0;i<T;i++){
        fin>>input;
        int output=GetMinFlips(input);
        fout<<"Case #"<<(i+1)<<": "<<output<<endl;
    }



    return 0;
}
int GetMinFlips(string data){

    string::size_type loc;
    string input=data;
    int count=0;
    loc=input.find_last_of('-');
    while(loc!=string::npos){
    ostringstream ss;
    for(int i=0;i<=loc;i++){
        if(input[i]=='+'){
            ss<<"-";
        }
        else{
            ss<<"+";
        }
    }
    input=ss.str();
    count++;
    loc=input.find_last_of('-');
    }
    return count;
}
