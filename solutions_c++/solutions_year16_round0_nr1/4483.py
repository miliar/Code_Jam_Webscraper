#include<bits/stdc++.h>
using namespace std;
int allset(int a[]){
for(int i=0;i<10;++i){
    if(a[i]==0){
        return 0;
    }
}
return 1;
}
string toString(int k){
string x="";
while(k>0){
    x=char((k%10)+48)+x;
    k=k/10;
}
return x;
}
int main(){
    int t;
    cin>>t;
    int je=1;
    while(t>0){
        int a[10];
        for(int i=0;i<10;++i){
            a[i]=0;
        }
        int k;
        scanf("%d",&k);
        if(k==0){
            cout<<"Case #"<<je<<": INSOMNIA"<<endl;
        }else{
            int i=1;
        while(!allset(a)){
         string x=toString(k*i);
         int c=0;
         while(c<x.length()){
            a[int(x[c]-48)]=1;
            if(allset(a)){
                cout<<"Case #"<<je<<": "<<x<<endl;
                break;
            }
            ++c;
         }
         ++i;
        }
        }
        ++je;
        --t;
    }
return 0;
}
