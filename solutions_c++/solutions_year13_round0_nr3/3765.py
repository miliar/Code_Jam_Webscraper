#include<iostream>
#include<string>
using namespace std;
int T,il_cyfr;
long long A,B;
long long res;
string s;
bool palindrom(long long a){
     s="";
     while(a>0){
                s+=char(a%10+48);
                a/=10;
                //it++;
                }
     //cout<<s<<endl;
     for(int i=0;i<(s.size()/2);i++){
             if(s[i]!=s[s.size()-i-1])return 0;
             }
     return 1;
     }
int main(){
    cin>>T;
    for(int q=1;q<=T;q++){
            cin>>A>>B;
            res=0;
            for(long long i=1;i*i<=B;i++){
                    if((i*i>=A)&&(palindrom(i))&&(palindrom(i*i)))res++;
                    }
            cout<<"Case #"<<q<<": "<<res<<endl;
            }
    
    
    return 0;
}
