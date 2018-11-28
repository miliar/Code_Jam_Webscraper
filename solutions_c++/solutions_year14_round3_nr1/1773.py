#include<iostream>
#include<vector>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
using namespace std;
long long mcd(int a, int b){
    if(b==0)return a;
    return mcd(b, a%b);
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,gen,t,cases;
    string s;
    long long div,p,q,mult[50];
    bool b;
    mult[0]=1LL;
    for(i=1;i<=40;i++){
        mult[i]=mult[i-1]*2LL;
    }
    cin>>cases;
    for(t=1;t<=cases;t++){
        cin>>s;
        p=q=0;
        i=0;
        while(s[i]>='0'&&s[i]<='9'){
            p=p*10LL+(s[i]-'0');
            i++;
        }
        i++;
        while(i<s.length()){
            q=q*10LL+(s[i]-'0');
            i++;
        }
        cout<<"Case #"<<t<<": ";
        div=mcd(p,q);
        p=p/div;
        q=q/div;
        i=0;
        while(i<=40){
            if(q==mult[i])break;
            i++;
        }
        if(i==41){
            cout<<"impossible"<<endl;
            continue;
        }
        gen=1;
        while(i>0){
            if(p*2LL>=mult[i]){
                cout<<gen<<endl;
                break;
            }
            i--;
            gen++;
        }
    }
}
