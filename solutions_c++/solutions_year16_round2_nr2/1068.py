#include<bits/stdc++.h>
using namespace std;
vector<int> x,y;
int con(string a){
    int ans=0;
    for(int i=0;i<a.size();i++){
        ans=(ans*10+(a[i]-'0'));
    }
    return ans;
}
void fun(string a,int i,int n,bool b){
    //cout<<a<<" "<<i<<endl;
    if(i==n){
        if(b){
            x.push_back(con(a));
        }
        else{
            y.push_back(con(a));
        }
        return ;
    }
    if(a[i]!='?'){
        fun(a,i+1,n,b);
    }
    else{
        string tmp[10];
        for(int j=0;j<10;j++){
            tmp[j]=a;
            tmp[j][i]=char('0'+j);
            fun(tmp[j],i+1,n,b);
      //      return ;
        }
    }
}
string con1(int a,int n){
    string tmp;
    if(a==0){
        for(int i=0;i<n;i++){
            tmp.push_back('0');
        }
        return tmp;
    }
    while(a!=0){
        char c='0'+a%10;
        tmp.push_back(c);
        a/=10;
    }
    for(int i=tmp.size();i<n;i++){
        tmp.push_back('0');
    }
    string tmp1;
    for(int i=0;i<n;i++){
        tmp1.push_back(tmp[n-i-1]);
    }
    return tmp1;
}
int main(){
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        int n;
        string a,b;
        cin>>a>>b;
        x.clear();y.clear();
        n=a.size();
        fun(a,0,n,1);
        fun(b,0,n,0);
        int a1=INT_MAX,a2=INT_MAX,mn=INT_MAX;
        for(int i=0;i<x.size();i++){
            for(int j=0;j<y.size();j++){
                if(abs(x[i]-y[j])<=mn){
                    if(abs(x[i]-y[j])<mn){
                        mn=abs(x[i]-y[j]);
                        a1=x[i];a2=y[j];
                    }
                    else{
                        if(x[i]==a1){
                            if(y[j]<a2){
                                a2=y[j];
                            }
                        }
                        else{
                            if(x[i]<a1){
                                a1=x[i];
                                a2=y[j];
                            }
                        }
                    }
                }
            }
        }
        cout<<con1(a1,n)<<" "<<con1(a2,n)<<endl;
    }
}
