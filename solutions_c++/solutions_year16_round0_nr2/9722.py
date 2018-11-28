#include <iostream>
#include <cstring>
using namespace std;
int HowMany(char* str){
    int negseg=0,start,len=strlen(str);
    if(str[0]=='+')start=1;
    else start=0;
    for(int i=1;i<len;i++){
        if(str[i-1]=='+' && str[i]=='-')
            negseg++;
    }
    if(!start)return (2*negseg+1);
    else return (2*negseg);
}
main(){
    int T,retrn;
    char str[101];
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>str;
        retrn=HowMany(str);
        cout<<"Case #"<<i<<": "<<retrn<<endl;
    }
}
