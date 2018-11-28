#include<bits/stdc++.h>

using namespace std;


int T;
string org;
int hs[1024];
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




int bfs(string s){
    queue<string> q;
    q.push(s);
    hs[ getHash(s ) ]=0;
    string rec,mrev;
    int mhash,orghash;
    while(!q.empty()){
        rec=q.front(); q.pop();
        orghash=getHash(rec);

        if( orghash==(1<<n)-1) break;

        for(int j=0;j<n;j++){
            mrev=rev(rec,j+1);
            mhash=getHash(mrev);
            if( hs[ mhash]==-1 ){

                q.push(mrev);
                hs[ mhash]=hs[ orghash]+1;

            }
        }

    }
    return hs[orghash];

}




int main(){

    freopen("input.in","r",stdin);
    freopen("outhput.out","w",stdout);
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>org;
        memset(hs,-1,sizeof(hs) );
        n=org.length();
        cout<<"Case #"<<cc++<<": "<<bfs(org)<<endl;




    }

}
