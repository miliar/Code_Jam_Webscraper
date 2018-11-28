#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main(){
    int t,j=1,i,count;
    char ch;
    string s;
    freopen("B-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    cin>>t;
    while(j<=t){
        cin>>s;
        ch='+';
        i=s.size()-1;
        count=0;
        while(i>=0){
            while(i>=0&&s[i]==ch){
                i--;
            }
            if(i>=0){
               ch= ch=='-'?'+':'-';
            i--;
            count++;
            }
        }
        cout<<"Case #"<<j<<": "<<count<<endl;
        j++;
    }

}
