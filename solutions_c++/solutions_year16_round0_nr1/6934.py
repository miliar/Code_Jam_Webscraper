#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
string GetLastNum(long int N);
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
    long int T,N;
    string str;
    fin>>T;

    for(long int i=0;i<T;i++){
        fin>>N;
        str=GetLastNum(N);
        fout<<"Case #"<<(i+1)<<": "<<str<<endl;
    }
//str="abcd";
//cout<<str<<endl;
//cout<<str.erase(0,1)<<endl;
    return 0;
}
string GetLastNum(long int N){
    ostringstream ss;
    if(N==0){
    ss<<"INSOMNIA";
    }
    else{
    long int i=1,x;
    string num="0123456789";
    string::size_type loc;
        do{
        x=i*N;
        ostringstream newNum;
        newNum<<x;
        string str=newNum.str();
        for(long int k=0;k<str.length();k++){
            loc = num.find( str[k],0);
            if(loc!=string::npos){
                num.erase(loc,1);
            }
        }
        i++;
        }while(num.length()!=0);
        ss<<x;
    }
    return ss.str();
}
