#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(){
    int T;
    ifstream din;
    ofstream dout;

    din.open("B-large.in", ifstream::in);
    dout.open("B-large.out", ofstream::out);

    din>>T;
    cout<<T<<endl;
    din.ignore();
    for(int t=0; t<T; t++){
        string s;
        string s2;
        getline(din, s);
        s2 = s[0];
        int j = 0;
        for(unsigned int i=1; i<s.length(); i++){
            if(s[i]!= s2[j]){
                s2 += s[i];
                j++;
            }
        }
        cout<<s2<<endl;
        /*bool allp = true;
        for(unsigned int i=0; i < s2.length(); i++){
            if(s2[i] == '-'){
                allp = false;
                break;
            }
        }*/
        if(s2.length()==1 && s2[0]=='+'){
            dout<<"Case #"<<(t+1)<<": 0"<<endl;
            continue;
        }

        int len;
        if(s2[s2.length()-1] == '-')
            len = s2.length();
        else
            len = s2.length() - 1;
        dout<<"Case #"<<(t+1)<<": "<<len<<endl;
    }

    din.close();
    dout.close();
    return 0;
}
