#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
    string inStr;
    ifstream in("B-large.in");
    ofstream out("writeOut2.txt");
    int tcase;
    in>>tcase;
    int k=1;
    while(k<=tcase){
        in>>inStr;
        int len=inStr.length();
        int Count=0;

        for(int i=1;i<len;i++){
            if(inStr[i-1]!=inStr[i])
                Count++;
        }
        if(inStr[len-1]=='-')
            Count++;
        out<<"Case #"<<k<<": "<<Count<<endl;

        k++;
    }
    return 0;
}
