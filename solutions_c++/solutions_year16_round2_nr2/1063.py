#include "stdio.h"
#include "math.h"
#include "iostream"
#include "algorithm"
using namespace std;
int a[3],b[3];
bool possible(int i,int j);
string to_string(int len,int x);
int main(){
    freopen("B-small-attempt0(1).in","r",stdin);
    freopen("b-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int l=1;l<=t;l++){
        int n,ans=100000;
        string x,y,ans1,ans2;
        cin>>x>>y;
        int r=3-x.length(),ll=x.length();
        string temp;
        for(int i=0;i<r;i++) temp+="0";
        x=temp+x;
        y=temp+y;
        for(int i=0;i<3;i++){
            if(x[i]=='?') a[i]=-1;
            else a[i]=x[i]-'0';
        }
        for(int i=0;i<3;i++){
            if(y[i]=='?') b[i]=-1;
            else b[i]=y[i]-'0';
        }
        for(int i=0;i<1000;i++){
            for(int j=0;j<1000;j++){
                if(possible(i,j)){
                    if(fabs(i-j)<ans){
                        ans=(int)fabs(i-j);
                        ans1=to_string(ll,i);
                        ans2=to_string(ll,j);
                    }
                }
            }
        }
        printf("Case #%d: ",l);
        cout<<ans1<<" "<<ans2<<endl;

    }
}
string to_string(int len,int x){
    string ans="";
    if(x==0) ans.insert(ans.end(),'0');
    else{
        while(x!=0){
            ans.insert(ans.end(),x%10+'0');
            x/=10;
        }
    }
    int t=ans.length();
    for(int i=t;i<len;i++) ans.insert(ans.end(),'0');
    reverse(ans.begin(),ans.end());
    return ans;
}
bool possible(int i,int j){
    for(int k=2;k>=0;k--){
        if(a[k]==-1);
        else if(i%10!=a[k]) return false;
        i/=10;
    }
    for(int k=2;k>=0;k--){
        if(b[k]==-1);
        else if(j%10!=b[k]) return false;
        j/=10;
    }
    return true;
}
