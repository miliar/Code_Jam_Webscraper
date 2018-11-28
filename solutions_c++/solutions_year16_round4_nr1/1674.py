#include<bits/stdc++.h>
using namespace std;

int main(){
freopen("1.txt","r",stdin);
freopen("out1.txt","w",stdout);
    int t;
    cin>>t;
    int j=1;
    while(t--){
        int n,r,p,s;
        cin>>n>>r>>p>>s;
        if(n==1){
            if(r==2||p==2||s==2){
                cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
            }
            else if(p==1 && r==1){
                cout<<"Case #"<<j<<": PR"<<endl;
            }
            else if(p==1 && s==1){
                cout<<"Case #"<<j<<": PS"<<endl;
            }
            else if(s==1 && r==1){
                cout<<"Case #"<<j<<": RS"<<endl;
            }
        }
        else if(n==2){
            if(r*p*s==0){
                cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
            }

            else if(r==(p+s)){
                cout<<"Case #"<<j<<": PRRS"<<endl;
            }
            else if(p==(r+s)){
                cout<<"Case #"<<j<<": PRPS"<<endl;
            }
            else if(s==(r+p)){
                cout<<"Case #"<<j<<": PSRS"<<endl;
            }
        }
        else{
            int f=0;
            if(n%2==1){
                f=2;
            }
            else{
                f=4;
            }
            int t=pow(2,n);
            if(abs(r-p)<=1 && abs(p-s)<=1 && abs(r-s)<=1){
                string s1="";
                for(int i=0;i<(t-f-6);i+=6){
                    s1+="PRPSRS";
                }
                if(f==2){
                    s1+="PR";
                    if(r<p){
                        s1+="PSPSRS";
                    }
                    else if(p<r){
                        s1+="RSPSRS";
                    }
                    else{
                        s1+="PSPRRS";
                    }
                }
                else{
                    s1+="";
                    if(p>r){
                        s1+="PRPRPSPSRS";
                    }
                    else if(r>s){
                        s1+="PRPRRSPSRS";
                    }
                    else{
                        s1+="PSPRRSPSRS";
                    }
                }
                cout<<"Case #"<<j<<": "<<s1<<endl;
            }
            else{
                cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
            }
        }
        j++;
    }
}
