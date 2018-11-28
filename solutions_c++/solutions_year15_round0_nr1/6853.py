#include <iostream>
using namespace std;

int main()
{
    int t=0;
    cin>>t;
    for(int i=0;i<t;i++){
        int S,number =0,acc=0;
        cin>>S;
        string str;
        cin>>str;
        int got=0;
        int get =0;
        for(int i=str.length()-1;i>=0;i--){
            if(str[i]!='0'){
                got=i;
                get = str[i]-'0';
                break;
            }
        }
        //cout<<got<<"\n"; 
        for(int i=0;i<=got;i++){
            if(str[i]!='0'){
                acc+=str[i]-'0';
            }
            if(str[i]=='0'){
                if(acc==0)
                number++;
            }
            if(acc!=0)
                acc--;
            
        }
        cout<<"Case #"<<i+1<<": "<<number<<"\n";
    }
    return 0;
}
