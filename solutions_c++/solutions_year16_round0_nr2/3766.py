#include <iostream>
#include<fstream>
#include<stdio.h>
#include<string>
using namespace std;
bool b[105];char s[105];
int num;
void change(int index){
    int i;
    for(i=0;i*2<index;i++){
        bool temp=b[index-i];
        b[index-i]=!b[i];
        b[i]=!temp;
    }
    if(i*2==index)b[i]=!b[i];
}
void get(int index,bool bb){
    int k=index;
    while(b[k]==bb)k--;
    if(k<0)return;
    if(k==0){
        b[0]=!b[0];
        num++;
    }
    else{
        if(b[0]==b[k]){
            change(k);
            num++;
            get(k,bb);
        }
        else{
            while(b[k]==!bb)k--;
            get(k,!bb);
            num++;
        }
    }
}
int main()
{
    int t,i,len,k,times;
    ifstream inf;
    ofstream outf;
    inf.open("E:\\project\\B-large.in");
    outf.open("E:\\project\\b-large.txt");
    inf>>t;k=0;
    while(t--){
        inf>>s;k++;
        len=0;
        while(s[len]!='\0'){
            if(s[len]=='-')b[len]=false;
            else if(s[len]=='+')b[len]=true;
            else{
                len++;break;
            }
            len++;
        }
        len--;num=0;
        get(len,true);
        outf<<"Case #"<<k<<": "<<num<<endl;
    }
    inf.close();
    outf.close();
    return 0;
}
