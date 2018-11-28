#include<bits/stdc++.h>
#define For(i,i1,i2) for(ll i=i1;i<i2;i++)
#define ll long long
#define pii pair<int,int>
#define F first
#define S second
#define V vector<int>
#define MP make_pair
#define PB push_back
#define MAX 1000000000000
#define CLR(x) memset(x,0,sizeof(x));
using namespace std;
struct dij{
    char c;
    bool sign;
};
dij pro(dij a,dij b){
    dij tmp;
    tmp.sign=a.sign^b.sign;
    if(a.c=='1'){
        if(b.c=='1'){
            tmp.c='1';
        }
        if(b.c=='i'){
            tmp.c='i';
        }
        if(b.c=='j'){
            tmp.c='j';
        }
        if(b.c=='k'){
            tmp.c='k';
        }
    }
    if(a.c=='i'){
        if(b.c=='1'){
            tmp.c='i';
        }
        if(b.c=='i'){
            tmp.c='1';
            tmp.sign=tmp.sign^1;
        }
        if(b.c=='j'){
            tmp.c='k';
        }
        if(b.c=='k'){
            tmp.sign=tmp.sign^1;
            tmp.c='j';
        }
    }
    if(a.c=='j'){
        if(b.c=='1'){
            tmp.c='j';
        }
        if(b.c=='i'){
            tmp.c='k';
            tmp.sign=tmp.sign^1;
        }
        if(b.c=='j'){
            tmp.c='1';
            tmp.sign=tmp.sign^1;
        }
        if(b.c=='k'){
            tmp.c='i';
        }
    }
    if(a.c=='k'){
        if(b.c=='1'){
            tmp.c='k';
        }
        if(b.c=='i'){
            tmp.c='j';
        }
        if(b.c=='j'){
            tmp.c='i';
            tmp.sign=tmp.sign^1;
        }
        if(b.c=='k'){
            tmp.c='1';
            tmp.sign=tmp.sign^1;
        }
    }
    return tmp;
}
dij pow(dij x,ll p){
    dij tmp;
    if(p%4==0){
        tmp.c='1';tmp.sign=0;
        return tmp;
    }
    if(p%4==1){
        return x;
    }
    if(p%4==2){
        tmp.c='1';tmp.sign=1;
        return tmp;
    }
    if(p%4==3){
        x.sign=x.sign^1;
        return x;
    }
}
ll len,x,l;
dij pre[10001],suf[10001],com;
string a;
int pos;
bool chk(){
    pos=-1;
    For(i,0,x*l){
        if(suf[i].c=='k'&&suf[i].sign==0){
            pos=x*l-i;
            break;
        }
    }
    //cout<<" pos "<<pos<<" ";
    if(pos<0)
        return 0;
    For(i,0,x*l){
        if(pre[i].c=='i'&&pre[i].sign==0){
            if(pos>i+2)
                return true;
        }
    }
    return false;
}
int main(){
    ios::sync_with_stdio(false);
    int t;
    /*For(i,0,10){
        dij tmp1,tmp2;
        cin>>tmp1.sign>>tmp1.c>>tmp2.sign>>tmp2.c;
        cout<<tmp1.sign<<tmp1.c<<tmp2.sign<<tmp2.c;
        cout<<"  "<<pro(tmp1,tmp2).sign<<pro(tmp1,tmp2).c<<endl;
    }*/
    cin>>t;
    For(z,1,t+1){
        CLR(pre);CLR(suf);
        cout<<"Case #"<<z<<": ";
        cin>>l>>x>>a;
        len=l*x;
        pre[0].c=a[0];pre[0].sign=0;
        suf[0].c=a[l-1];suf[0].sign=0;
        For(i,1,x*l){
            dij tmp;tmp.c=a[i%l];tmp.sign=0;
            pre[i]=pro(pre[i-1],tmp);
            tmp.c=a[(x*l-i-1)%l];
            suf[i]=pro(tmp,suf[i-1]);
            //cout<<pre[i].c<<" "<<pre[i].sign<<endl;
        }
        com=pre[l*x-1];
        if(com.c=='1'&&com.sign==1){
            if(chk())
            cout<<"YES\n";
            else
                cout<<"NO\n";
        }
        else{
            cout<<"NO\n";
        }
    }
}


