#include<iostream>
#include<string>
using namespace std;
//ProblemA.StandingOvation
int main(){
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        int s;
        cin>>s;
        string str;
        cin>>str;
        int ans=0;
        int people=0;
        for(int i=0;i<str.length();i++){
            if(str[i]=='0')continue;
            if(i<=people){
                people+=str[i]-'0';
            }
            else{
                ans+=(i-people);
                people=i;
                people+=str[i]-'0';
            }
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
}
