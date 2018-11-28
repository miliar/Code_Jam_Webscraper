#include<iostream>
using namespace std;
bool f(int x){
    if(x<=9)
        return true;
    int a[10],c=0;
    while(x!=0){
        a[c++]=x%10;
        x/=10;
    }
    for(int i=0;i<c/2;i++)
        if(a[i]!=a[c-i-1])
            return false;
    return true;
}
int t,a,b,x[10001];
int main(){
	int i,j;
	freopen("src.txt","r",stdin);
	freopen("out.txt","w",stdout);
    for(i=0;i<=100;i++)
        x[i*i]=i;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>a>>b;
        int c=0;
        for(j=a;j<=b;j++)
            if(x[j]&&f(j)&&f(x[j]))
                c++;
        cout<<"Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}