#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
int a[100010];
int b[100010];
int c[100010];
int fuc[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
int d[100010];
int e[100010];
int cao(int x,int y){
    int f=0;
    if(x<0)f++;
    if(y<0)f++;
    x=abs(x);
    y=abs(y);
    x--;
    y--;
    return fuc[x][y]*((f&1)==1?-1:1);
}
string str;
int main(){
    int t;
    int cas=1;
    //freopen("C-small-attempt2.in","r",stdin);
    //freopen("csmall.out","w",stdout);
    cin>>t;
    while(t--){
        int x,l;
        cin>>x>>l;
        cin>>str;
        int len=str.length();
        for(int i=0;i<len;i++){
            if(str[i]=='i')a[i]=2;
            else if(str[i]=='j')a[i]=3;
            else if(str[i]=='k')a[i]=4;
        }
        b[0]=1;
        int maxx=x*l;
        int f1=0,f2=0;
        for(int i=1;i<=maxx;i++){
            b[i]=cao(b[i-1],a[(i-1)%len]);
            if(b[i]==2)f1=1;
            if(f1&&b[i]==4){
                f2=1;
                break;
            }
        }
        //cout<<f1<<" "<<f2<<endl;
        b[0]=1;
        cout<<"Case #"<<cas++<<": ";
        if(!f2){
            cout<<"NO"<<endl;
            continue;
        }
        for(int i=1;i<=len;i++){
            b[i]=cao(b[i-1],a[i-1]);
        }
        //cout<<b[len]<<endl;
        //l=l%4;
        int tmp=1;
        int t=0;
        while(l){
            tmp=cao(tmp,b[len]);
            l--;
            t++;
        }
        //cout<<t<<endl;
        if(tmp==-1)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;

        /*b[0]=1;
        for(int i=1;i<=len;i++){
            b[i]=cao(b[i-1],a[i-1]);
        }
        c[0]=1;
        for(int i=1;i<=len;i++)
            c[i]=cao(a[len-i],c[i-1]);
        //for(int i=0;i<=len;i++)cout<<a[i]<<" "<<b[i]<<" "<<c[i]<<endl;
        d[0]=1;
        for(int i=1;i<=l;i++){
            d[i]=cao(d[i-1],b[len]);
        }
        int l1=min(4*len,x*l);
        bool flag=0;
        int pre=1;
        int suf=1;
        for(int i=1;i<=l1&&!flag;i++){
            pre=cao(pre,a[(i-1)%len]);
            if(pre!=2)continue;
            //cout<<pre<<endl;
            suf=1;
            for(int j=1;j<=l1&&!flag;j++){
                if(j+i>=x*l)break;
                suf=cao(a[(l1-j)%len],suf);
                //cout<<pre<<" "<<suf<<endl;
                if(suf!=4)continue;
                //cout<<len-j<<endl;
                if(cao(b[len-(l1-j)%len],d[l-(j+len-1)/len-1])==4)flag=1;


            }
        }
        cout<<"Case #"<<cas++<<": ";
        if(flag)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;*/

    }
}
