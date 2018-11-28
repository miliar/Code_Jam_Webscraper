#include <cstring>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    int T,N;
    cin>>T;
    int digit[10];
    string str;
    int i;
    for(i=1;i<=T;i++)
    {
        cin>>N;
        if(N==0){
          cout<<"Case #"<<i<<": INSOMNIA"<<endl;
          continue;
        } 
        memset(digit,0,sizeof(digit));
        int count = 0;
        int time = 0;
        while(count!=10){
             time++;
            str = to_string(N*time);
            for(int j=0;j<str.length();j++){
                if(digit[str[j]-'0']==0){
                    digit[str[j]-'0']++;
                    count++;
                }
                cout<<count<<' ';
            }
           
        }
        cout<<"Case #"<<i<<": "<<N*time<<endl;
        
    }
    return 0;
}