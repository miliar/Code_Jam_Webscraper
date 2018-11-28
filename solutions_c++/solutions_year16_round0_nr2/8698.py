#include <iostream>
#include <stack>
#include <queue>
#include <string.h>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        //cout<<i<<endl;
        char S[101];
        int p=0;
        cin>>S;
        stack <char> a;
        int l=strlen(S);
        for(int j=l-1;j>=0;j--){
            //cout<<S[j];
            a.push(S[j]);
        }

        int count=0;
        int turn=0;
        while(count<l){
            char t = a.top();
            if(t=='+'){
                p=1;
            }else{
                p=0;
            }
            a.pop();
            count=1;
            if(l==1){
                if(p==1){
                    turn=0;
                }else{
                    turn=1;
                }
            }else{
                while(a.size()>=1&&count<l){
                    if(t==a.top()){
                        a.pop();
                        count++;
                    }else{
                        break;
                    }
                }
                if(count==l){
                    if(p!=1){
                        turn++;
                    }
                }else{
                    if(p==1){
                        for(int b=0;b<count;b++){
                            a.push('-');
                        }
                    }else{
                        for(int b=0;b<count;b++){
                            a.push('+');
                        }
                    }
                    turn++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<turn<<endl;
    }
    return 0;
}
