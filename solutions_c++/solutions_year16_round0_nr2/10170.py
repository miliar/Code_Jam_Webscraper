#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
   fstream in("B-large.in");
   ofstream outp("sayed.txt");
    int n,counter=0;
    string s;
    in>>n;
    for(int i=0;i<n;i++){
        in>>s;
        reverse(s.begin(),s.end());
        for(int c=0;c<s.size();c++){
            if(s[c]=='-'){
                counter++;
                for(int j=c;j<s.size();j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }
        outp<<"Case #"<<i+1<<": "<<counter<<endl;
        counter=0;
    }
    return 0;
}
