#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream inp("B-large.in");
    ofstream outp("output.txt");
    int tc;
    inp>>tc;
    string a;
    int cnt=0;

    for(int i=1;i<=tc;i++){
    inp>>a;
    cnt=0;
    for(int i=a.size()-1;i>=0;i--){
        if(a[i]=='-'){
            for(int j=i;j>=0;j--){
                if(a[j]=='-')
                a[j]='+';
                else if(a[j]=='+')
                    a[j]='-';}
            cnt++;
        }
    }
    outp<<"Case #"<<i<<": "<<cnt<<endl;}
    return 0;
}
