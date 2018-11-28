#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t;
    ifstream fin("a.in");
    ofstream fout("ab.out");
    fin>>t;
    
    for(int qq=0; qq<t;qq++){
        string s;
        fin>>s;


        int a = 0,b=0;
        int count = 0;
        int i;
        for(i=0; i<s.length(); i++){
            if(s[i] == '+'){
                break;
            }
        }
        if(i==s.length()){
            fout<<"Case #"<<qq+1<<": "<<1<<endl;
            continue;
        }
        
        for(int i=0;i<s.length()-1;i++){
            if(s[i] == s[i+1]){
                continue;
            }else if(s[i+1] == '-'){
                count+=2;
                while(i<s.length()-2&&s[i+2]=='-'){
                    i++;
                }
                s[i+1] = '+'; 
            }else{
                count++;
            }
        }
        
         fout<<"Case #"<<qq+1<<": "<<count<<endl;
    }
    return 0;
}




