#include<iostream>
#include<fstream>
#include<string>
using namespace std;

string  Reverse(string s1,int n){
    string temp(s1.begin(),s1.begin()+n);
    for(int k=0;k<n;k++){
        if(temp[n-k-1]=='-') s1[k]='+';
        else s1[k]='-';
    }
    return s1;
}

bool Check(string s1){
    for(int i=0;i<s1.length();i++) if(s1[i]=='-') return 0;
    return 1;
}

int main(){
 int t;
 long long int cnt=0,j=1, l=1;
 cin>>t;

 string str,temp;
 while(t--){
    cin>>str;
    cnt=0;
    bool f =0;
    int last =str.length();
    f= Check(str);
    if(f){
            cout<<"Case #"<<l++<<": "<<cnt<<endl;
            continue;
    }
    while(last>=1){
        if(str[0]=='+'){
                int j;
            for( j=0;j<last;j++) {
                if(str[j]=='-') break;
            }
           str= Reverse(str,j);
        cnt++;
        }
           if(str[last-1]=='-') {
            str= Reverse(str,last);
                cnt++;
                }
              
              int j=last;
            while(j>0&&str[j-01]=='+'){
                j--;
            }
            last=j;
            f=Check(str);
    }
    cout<<"Case #"<<l++<<": "<<cnt<<endl;
 }
return 0;
}
