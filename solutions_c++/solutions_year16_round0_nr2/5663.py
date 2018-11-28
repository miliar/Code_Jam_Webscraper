#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main(){
    int t,j=1,i,crnt1;
    char chr;
    string s;
    freopen("B-large (1).in","r",stdin);
    freopen("output1.txt","w",stdout);
    cin>>t;
    while(j<=t){
        cin>>s;
        chr='+';
        i=s.size()-1;
        crnt1=0;
        while(i>=0){
            while(i>=0&&s[i]==chr){
                i--;
            }
            if(i>=0){
               if(chr=='-')
                chr='+';
               else
                chr='-';
            i--;
            crnt1++;
            }
        }
        cout<<"Case #"<<j<<": "<<crnt1<<endl;
        j++;
    }

}
