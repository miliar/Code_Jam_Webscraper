#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
string st;
int n,k;
long long int toTen(long long int b){
    long long int i,res=0,us=1;
    for(i=st.size()-1;i>=0;i--){
        if(st[i]=='1') res+=us;
        us*=b;
    }
    return res;
}
void doit(){
    long long int i,j,x;
    long long int arr[15];
    for(i=2;i<=10;i++){
        x=toTen(i);
        for(j=2;j*j<=x;j++){
            if((x%j)==0){
                arr[i]=j;
                break;
            }
        }
        if(j*j>x) return;
    }
    cout<<st<<" ";
    for(i=2;i<=10;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    k--;
}
void rec(int x){
    if(k==0) return;
    if(x==n-1){
        doit();
        return;
    }
    st[x]='1';
    rec(x+1);
    st[x]='0';
    rec(x+1);
}
int main(){
    freopen("coin.in","r",stdin);
    freopen("coin.out","w",stdout);
    int t,i;
    cin>>t>>n>>k;
    st="1";
    for(i=2;i<=n-1;i++)
        st+="0";
    st+="1";
    cout<<"Case #1:"<<endl;
    rec(1);
    return 0;
}
