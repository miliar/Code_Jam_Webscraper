#include <iostream>
#include <set>
#include <stdlib.h>
#include <cstdlib>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output_file_name3.out","w",stdout);
    int T,pluscnt=0,plusmin=0,k=1,it;
    cin>>T;
    string s;
    while(T--){
        it=pluscnt=0;
        cin>>s;

        while(true){
            pluscnt=0;
            for(int i=0 ; i < s.size(); i++)if(s[i]=='+')pluscnt++;

            if(pluscnt==s.size()){
                break;
            }

            if(s[0]=='+'){
                for(int i=0; i<s.size() ; i++){
                    if(s[i]=='+')s[i]='-';
                    else break;
                }
            }else{
                for(int i=0 ; i<s.size(); i++){
                    if(s[i]=='-')s[i]='+';
                    else break;
                }
            }
            it++;
        }

        cout<<"Case #"<<k<<": "<<it<<endl;
        k++;
    }
    return 0;
}
