#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int main()
{
    ifstream inp("A-large.in");
    ofstream outp("output.txt");
    int tc;
    inp>>tc;
    set <int> num;
    int n, temp,out;
    for(int j=1;j<=tc;j++){
    inp>>n;
    for(int i=1;i<=200000;i++){
        if(n==0||num.size()==10)
            break;
        temp=i*n;
        out=temp;
        while(temp!=0){
        num.insert(temp%10);
        temp=temp/10;
        }
    }
    if(n==0||num.size()!=10)
        outp<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
    else
    outp<<"Case #"<<j<<": "<<out<<endl;
    num.clear();
    }
    return 0;
}
