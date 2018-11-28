#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <unordered_map>
#include <queue>
#include <bitset>
#define bs bitset <101>
using namespace std;

unordered_map < bs ,  int > o;
queue < bs > q;

void clear(){
    while(!q.empty()){
        q.pop();
    }
}


int solve (bs a, int l){
    q.push(a);
    o[a]=0;
    int i,j,num;
    while(!q.empty()){
        a=q.front();
        num=o[a];
        if(a.count()==l)
            return num;
        bs b = a;
        for(i=0;i<l;i++){
            for(j=0;j<=i/2;j++){
                b[j]=(!a[i-j]);
                b[i-j]=!(a[j]);
            }
            if(o[b])
                continue;   
            else{
                o[b]=num+1;
                q.push(b);
            }
        }
        q.pop();
    }
}


int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.out","w",stdout);
    
    
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++){
        o.clear();
        clear();
        string k;
        int i,l;
        bs y;
        cin>>k;
        l=k.length();
        for(i=0;i<l;i++){
            if(k[i]=='+')
                y[i]=1;
            else
                y[i]=0;
        }
        /*for(i=0;i<y.size();i++){
            cout<<y[i];
        }
        cout<<endl;*/
        cout<<"Case #"<<t<<": "<<solve(y,l)<<endl;
    }
    
}
