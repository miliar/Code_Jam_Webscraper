#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int power(int x, int y){
    int ans=1;
    for(int i=0;i<y;i++){
        ans=ans*x;
        }
    return ans;
    }

string b(int x){
    if(x==0) return "0";
    else{
        if(x/2==0){
            if(x%2==1) return "1";
            else return "0";
            }
        else{
            if(x%2==1) return b(x/2)+"1";
            else return b(x/2)+"0";
            }
        }
    }
int c2(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(2,i);
        }
        return ans;
    }
int c3(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(3,i);
        }
        return ans;
    }
int c4(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(4,i);
        }
        return ans;
    }
int c5(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(5,i);
        }
        return ans;
    }
int c6(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(6,i);
        }
        return ans;
    }
int c7(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(7,i);
        }
        return ans;
    }
int c8(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(8,i);
        }
        return ans;
    }
int c9(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(9,i);
        }
        return ans;
    }
int c10(string s){
    int ans=0;
    for(int i=0;i<=s.length()-1;i++){
        ans=ans+(s[s.length()-1-i]-'0')*power(10,i);
        }
        return ans;
    }

int main(){
    int t,n,j;
    int half;
    string current;
    string currentfull;
    string final;
    int bitpatch;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n>>j;
        half=n/2;
        cout<<"Case #"<<i<<":"<<endl;
        for(int m=0;m<j;m++){
            current=b(m);
            bitpatch=half-2-current.length();
            currentfull="1";
            for(int p=0;p<bitpatch;p++){
                currentfull=currentfull+"0";
                }
            currentfull=currentfull+current+"1";
            if(n%2==1){
                final=currentfull+"0"+currentfull;
                }
            else{
                final=currentfull+currentfull;
                }
            cout<<final<<" "<<c2(currentfull)<<" "<<c3(currentfull)<<" "<<c4(currentfull)<<" "<<c5(currentfull)<<" "<<c6(currentfull)<<" "<<c7(currentfull)<<" "<<c8(currentfull)<<" "<<c9(currentfull)<<" "<<currentfull;
            
            cout<<endl;
            }
        }
    }
