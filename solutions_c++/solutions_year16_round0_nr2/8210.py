#include<iostream>
#include<string.h>
#include<algorithm>
#include<stack>
#include<deque>

using namespace std;

const int MAX=105;
char S[MAX];
int ans=0,top;
stack<char> st1,st2;

void convert(){
    char TMP;
    while(!st1.empty()){
        TMP=st1.top();
        st1.pop();
        if(TMP=='+'){
            st2.push('-');
        }
        else{
            st2.push('+');
        }
    }

    while(!st2.empty()){
        TMP=st2.top();
        st2.pop();
        st1.push(TMP);
    }
}

int main(){

    freopen("B-large.in","r",stdin);
    freopen("o1.out","w",stdout);

    int len,i,T,ans;
    char tmp;
    cin>>T;
    for(int z=1;z<=T;z++){
        scanf("%s",S);
        len=strlen(S);

        for(i=0;i<len;i++){
            st1.push(S[i]);
        }

        top=len-1;
        ans=0;

        while(top>=0){
            if(st1.top()=='+'){
                st1.pop();
                top-=1;
            }
            else{
              ans+=1;
              convert();
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }

    return 0;
}
