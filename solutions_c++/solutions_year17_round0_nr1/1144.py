#include<iostream>
#include<fstream>
using namespace std;
int main(){
    int t,k;
    ifstream in("A-large.in");
    ofstream out("out.txt");
    in>>t;
    string s;
    for(int it=0;it<t;it++){
        in>>s;
        in>>k;
        int count=0;
        for(int i=0;i<s.length();i++){
            if(s[i]=='-')
                if(i+k<=s.length()){
                    count++;
                    for(int j=0;j<k;j++){
                        s[i+j]=(s[i+j]=='-')?'+':'-';
                    }
                }else{
                    count=-1;
                    break;
                }
        }
        if(count==-1)
            out<<"Case #"<<it+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            out<<"Case #"<<it+1<<": "<<count<<endl;
    }
    return 0;
}
