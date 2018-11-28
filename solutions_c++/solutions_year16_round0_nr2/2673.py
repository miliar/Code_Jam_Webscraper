#include<bits/stdc++.h>

using namespace std;

int T;
int n;
int cc=1;

string rev( string str,const int& pos){
    int upper=floor(pos*1.0/2 +0.5);

    for(int i=0;i<upper;i++){
        if( i==pos-1-i){
            str[i]=='-' ? str[i]='+' : str[i]='-';
            continue;
        }
        str[i]=='-' ? str[i]='+' : str[i]='-';
        str[pos-1-i]=='-'? str[pos-1-i]='+' : str[pos-1-i] ='-';
        swap( str[i],str[pos-1-i]);
    }
    return str;
}

int getHash(const string& str){
    unsigned int aux=0;
    for(int i=0;i<n;i++){
        if( str[i]=='+' ) aux^=(1<<(n-i-1) );
    }
    return aux;
}

bool checckp(const string& str){
    for(int i=0;i<n;i++)
        if(str[i]=='-') return false;
    return true;


}

bool checckm(const string& str){
    for(int i=0;i<n;i++)
        if(str[i]=='+') return false;
    return true;


}

int solve(string s){
    int ithmp,cnt=0,ithmm;
    bool checkp,checkm;
    while(true){
        if( checckp(s) || checckm(s) )break;
        checkp=checkm=false;
        for(int i=0;i<n;i++) {
            if(s[i]=='+' && !checkp) ithmp=i,checkp=true;
            if(s[i]=='-' && !checkm) ithmm=i, checkm=true;
        }
        //cout<<s<<" "<<ithmp<<" "<<ithmm<<endl;
        if( ithmp==0) s=rev(s,ithmm);
        else s=rev(s,ithmp);
        cnt++;
    }
    if( checckm(s)  ) return cnt+1;
    return cnt;
}



int main(){

    freopen("input.in","r",stdin);
    freopen("outhput.out","w",stdout);


    string org;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>org;
        n=org.length();
        printf("Case #%d: %d\n",cc++,solve(org) );

    }
    return 0;

}

