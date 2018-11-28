#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream in("b.in");
ofstream out("b.out");

int main()
{
    int t;
    in>>t;
    for(int i=1;i<=t;++i){
        string s;
        in>>s;
        for(int j=0;j<s.size()-1;){
            if(s[j]==s[j+1])s.erase(s.begin()+j);
            else ++j;
        }
        for(int j=s.size()-1;j>=0;){
            if(s[j]=='+'){
                s.erase(s.begin()+j);
                --j;
            }
            else break;
        }
        out<<"Case #"<<i<<": "<<s.size()<<endl;
    }
    return 0;
}
