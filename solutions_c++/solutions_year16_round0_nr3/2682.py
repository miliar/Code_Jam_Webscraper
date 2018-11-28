#include<iostream>
#include<string>
#include<sstream>
using namespace std;
int j,n;
int nowJ;
int basePrime[6]={2,3,5,7,11,13};
long long GetTen(string data,long long baseR){
    long long ans=0;
    for(int i=0;i<data.length();i++){
        ans*=baseR;
        ans+=data[i]-'0';
    }
    return ans;
}
void checkStr(string str){
    long long cue=0;
    bool isAdd=true;
    for(int i=0;i<str.length();i++){
        if(isAdd){
            cue+=str[i]-'0';
        }
        else{
            cue-=str[i]-'0';
        }
        isAdd=!isAdd;
    }

    if(cue%3==0){
        //long long tenBase=GetTen(str,2);
        bool test=true;
        stringstream ss;
        ss<<str;
        //cout<<str<<" :"<<tenBase<<" ch "<<endl;
        for(int i=2;i<=10;i++){
            long long tenBase=GetTen(str,i);
            bool isPrime=false;
            for(int j=0;j<6;j++){
                if(tenBase%basePrime[j]==0){
                    ss<<" ";
                    ss<<basePrime[j];
                    isPrime=true;
                    break;
                }
            }
            if(!isPrime){
                return;
            }
            //cout<<" "<<tenBase/(i+1);
            //cout<<tenBase<<"/"<<i+1<<"="<<tenBase/(i+1)<<"."<<tenBase%(i+1)<<endl;
            //cout<<i+1<<" "<<tenBase%(i+1)<<endl;
        }
        //cout<<str;
        //for(int i=3;i<=11;i++)cout<<" "<<i;
        cout<<ss.str()<<endl;
        //cout<<str<<" :"<<tenBase<<" ch "<<test<<endl;
        nowJ++;
    }
}
void move(string current){
    if(j==nowJ){
        return;
    }
    if(current.length()+1==n){
        current+="1";
        checkStr(current);
        return;
    }
    move(current+"0");
    move(current+"1");
}

int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        cin>>n>>j;
        //cout<<gcd(n,j);
        cout<<"Case #"<<++cas<<":"<<endl;
        nowJ=0;
        string start="1";
        move(start);
        //cout<<"count;"<<nowJ<<endl;
    }
}

