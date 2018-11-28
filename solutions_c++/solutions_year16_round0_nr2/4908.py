#include <iostream>
#include <string>

using namespace std;

int main(){
    int T;
    int m = 1;
    cin >> T;
    while(m<=T){
        string str;
        cin >> str;
        int step = 0;
        while(str.find('-')!=-1){
            for(int i = 1; i <= str.length(); i++){
                if(str[i-1]=='-' && (str[i]=='+' || str[i]=='\0')){
                    for(int j = 0; j < i; j++){
                        str[j]='+';
                    }
                    step+=1;
                }
                if(str[i]=='-' && str[i-1]=='+'){// case +++-..
                    for(int j = 0; j < i; j++){
                        str[j]='-';
                    }
                    step+=1;
                }
            }
        }
        cout <<"Case #"<<m<<": "<<step<<endl;
        m++;
    }
    
}