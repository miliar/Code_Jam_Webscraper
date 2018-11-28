#include<iostream>
#include<fstream>
#include<string>
using namespace std;

string  reverseit(string s,int n){
    string temp(s.begin(),s.begin()+n);
    for(int i=0;i<n;i++){
        if(temp[n-i-1]=='-') s[i]='+';
        else s[i]='-';
    }
    return s;
}
bool check(string s){
    for(int i=0;i<s.length();i++) if(s[i]=='-') return 0;
    return 1;
}

int main(){
 int t;
 long long int ans=0,i=1;
 cin>>t;

 string s,temp;
 while(t--){
    cin>>s;
    ans=0;
    bool flag =0;
    int last =s.length();
    flag = check(s);
    if(flag){
            cout<<"Case #"<<i++<<": "<<ans<<endl;
            continue;
    }
    while(last>=1){
        if(s[0]=='+'){
                int i;
            for( i=0;i<last;i++) {
                if(s[i]=='-') break;
            }
           s= reverseit(s,i);
            ans++;
        }
       // cout<<s<<" ";
        if(s[last-1]=='-') {
            s= reverseit(s,last);
                ans++;
                }
              //  cout<<s<<" ";
              int i =last;
            while(i>0&&s[i-01]=='+'){
                i--;
            }
            last=i;
            flag=check(s);
    }
    cout<<"Case #"<<i++<<": "<<ans<<endl;
 }
return 0;
}
