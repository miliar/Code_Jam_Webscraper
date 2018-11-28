#include<iostream>
#include<fstream>
using namespace std;
    ifstream inn("B-large.in");
    ofstream out("out.txt");
int GG=0;
int f=0;
void flip(string &s,int i,char c){
    for(int k=0;k<=i;k++){
        s[k]=c;
    }
    GG++;
}
void chieck(string s, int x){
    for(int k=0;k<s.length()-1;k++){
        if(s[k]!=s[k+1]){
                return;
            }
    }
    if(s[0]=='-')
        GG++;
    out<<"Case #"<<x<<": "<<GG<<endl;
    GG=0;
    f=1;
}
void try2(string s,int x){
    if(s[0]==s[1]&& s[0]=='-'){
        out<<"Case #"<<x<<": 1\n";
    }else if(s[0]==s[1]&& s[0]=='+'){
        out<<"Case #"<<x<<": 0\n";
    }else if(s[0]=='+'&&s[1]=='-'){
        out<<"Case #"<<x<<": 2\n";
    }else if(s[0]=='-'&&s[1]=='+'){
        out<<"Case #"<<x<<": 1\n";
    }
}
int main(){
    int T;
    string s;

    inn>>T;
    for(int TS=1;TS<=T;TS++){
        inn>>s;
        f=0;
        while(f!=1){
                if(s.length()==1){
                    if(s[0]=='-')
                        out<<"Case #"<<TS<<": 1\n";
                    else
                        out<<"Case #"<<TS<<": 0\n";
                    f=1;
                     }else if(s.length()==2){
                        try2(s,TS);
                        f=1;
                    }else{
                        for(int i=0;i<s.length()-1;i++){
                            if(s[i]!=s[i+1]){
                                flip(s,i,s[i+1]);
                                chieck(s,TS);
                                if(f==1)
                                    break;
                            }
                        }
                        if(f==0){
                            chieck(s,TS);
                            f=1;
                        }
                    }
        }

    }

}
