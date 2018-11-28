#include <fstream>
#include<iostream>
using namespace std;
int main(){

    int t,i,x=1,T,len,j;
    string s,a="";
    ofstream outputFile;
    outputFile.open("output.in");

    ifstream inputFile;
    inputFile.open("A-large (1).in");
    ifstream file("A-large (1).in");
    inputFile>>T;
    getline(file,s);
    while(T--){

        getline(file,s);
        len=s.size();
        a=s[0];
        j=0;
        for(i=1;i<len;i++)
        {
            if((int)(s[i]-48)>=(int)(a[0]-48))
                a=s[i]+a;
            else a=a+s[i];

        }
        outputFile<<"Case #"<<x<<": "<<a;
        outputFile<<"\n";
        x++;
    }
    inputFile.close();
    outputFile.close();
    return 0;
}
