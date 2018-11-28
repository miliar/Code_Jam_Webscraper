#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
using namespace std;
string flip(string s,int n){
    string s1;
for(int k(0);k<n+1;k++){
    if(s[k]=='+'){
        s[k]='-';
    }else if(s[k]=='-'){
        s[k]='+';
    }

}
    s1=s;
    for(int k(0);k<n;k++){
        s[n-k]=s1[k];
    }

    return s;
}
bool v(int l){
}
int main()
{

int T,N,R;

    #define small
    //#define large
    #ifdef small
        freopen("B-small-attempt5.in","rt",stdin);
        freopen("B-small.txt","wt",stdout);
    #endif // small

    #ifdef large
        freopen("A-large.in","rt",stdin);
        freopen("A-large.out","wt",stdout);
    #endif // large
        cin >>T;
        string S;
        bool ish=false;
        getline(cin,S);
        for(int i(0);i<T;i++){
                int co=0;
                int c=0;
            getline(cin,S);
            int l=S.length();

            for(int j(0);j<l;j++){
                      if(S[j]=='+'){
                        co++;
                      }
                      if(co==l){ish=true;}else{ish=false;}
                    }
            if(ish==true){cout << "Case #" << i+1 <<": "<< 0 << endl;}
            else if( S=="-"){
                cout << "Case #" << i+1 <<": "<< 1 << endl;
            }
        else if(l>1){
            for(int k(0);k<pow(2,l);k++){

                    for(int j(0);j<l;j++){
                      if(S[j]=='+'){
                        co++;
                      }
                      if(co==l){ish=true; break;}else{ish=false;}
                    }
            if(S[0]=='-'){
            for(int j(0);j<l;j++){
                    if(S[l-j]=='-' ){
                       S=flip(S,(l-j));
                        c++;
                       break;
                    }
            }
            for(int j(0);j<l;j++){
                if(S[j]=='+' and S[j+1]=='-'){
                    S=flip(S,j);
                    c++;
                    break;
                }
            }
            for(int j(0);j<l;j++){
                if(S[j]=='-' and S[j+1]=='+'){
                   S=flip(S,j);
                   c++;
                   break;

                }
                }
            }else if(S[0]=='+'){
                for(int j(0);j<l;j++){
                if(S[j]=='+' and S[j+1]=='-'){
                    S=flip(S,j);
                    c++;
                    break;
                }
            }
                 for(int j(0);j<l;j++){
                    if(S[l-j]=='-' ){
                       S=flip(S,(l-j));
                        c++;
                       break;
                    }
            }
            for(int j(0);j<l;j++){
                if(S[j]=='+' and S[j+1]=='-'){
                    S=flip(S,j);
                    c++;
                    break;
                }
            }
            for(int j(0);j<l;j++){
                if(S[j]=='-' and S[j+1]=='+'){
                   S=flip(S,j);
                   c++;
                   break;

                }
                }

            }
            }
           cout << "Case #" << i+1 <<": "<< c << endl;

            }
        }




    return 0;

}
