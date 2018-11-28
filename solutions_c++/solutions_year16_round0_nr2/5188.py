#include <iostream>
#include<cstring>
using namespace std;

int main()
{
    int t,p=0;
    cin>>t;
    while(t--){++p;
        string str;
        char s;
        cin>>str;
        s=str[0];
        int count=0,i;
        for(i=0;i<str.size();i++){
            if(s==str[i]){
                continue;
            }
            else{
                for(int j=0;j<=i-1;j++){
                    if(str[j]=='+')
                    str[j]='-';
                    else
                    str[j]='+';
                }
                count++;
                s=str[i];
            }
        }
        if(str[i-1]=='-')
        count++;
        cout<<"Case #"<<p<<": "<<count<<endl;
    }
    return 0;
}