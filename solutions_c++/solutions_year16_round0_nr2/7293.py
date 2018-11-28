#include<iostream>
#include<string.h>
using namespace std;
void flip(int);
int count=0;
char ch[101];
int main(){
    int l; 
    int T,i,j,n;
    cin>>n;
    for(i=1;i<=n;i++){
        cin>>ch;
        l=strlen(ch);
        for(j=l;j>=0;j--){
            if(ch[j]=='-'){
                count++;
                flip(j);
                
            }        }
        cout<<"Case #"<<i<<": "<<count<<endl;
        count=0;
    }
    
}
void flip(int j){
    int i,flag=1,s,k;
    for(i=j;i>=0;i--){
        if(ch[i]=='+')ch[i]='-';
        else if(ch[i]=='-'&&ch[i-1]=='+'){
            ch[i-1]='-';
		ch[i]='+';
            i=i-1;
        }
        else if(ch[i]=='-')ch[i]='+';
    }
}