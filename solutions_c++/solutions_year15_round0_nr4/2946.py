#include<iostream>
using namespace std;

bool func(int x,int r,int c){
    if(x<=1)
        return 0;
    if(x==2){
        if(r==1&&c==1)
            return 1;
        if(r==1&&c==3)
            return 1;
        if(r==3&&c==3)
            return 1;
        return 0;
    }
    if(x==3){
        if(r==1)
            return 1;
        if(r==2&&c==2)
            return 1;
        if(r==2&&c==4)
            return 1;
        if(r==4&&c==4)
            return 1;
        return 0;
    }
    if(x==4){
        if(r==1)
            return 1;
        if(r==2)
            return 1;
        if(r==3&&c==3)
            return 1;
        return 0;
    }
    return 0;
}
int main(){
    int t,x,r,c,r1;
    cin>>t;
    for(int w=1;w<=t;w++){
        cin>>x>>r>>c;
        r1=min(r,c);
        c=max(r,c);
        r=r1;
        if(func(x,r,c))
            cout<<"Case #"<<w<<": "<<"Richard"<<endl;
        else cout<<"Case #"<<w<<": "<<"Gabriel"<<endl;
        //r min c max
        //if((x==2&&max(r,c)<2)||(x==2&&min(r,c)==1&&max(r,c)==3)||(x==3&&max(r,c)<3)||(x==3&&r==4&&c==4)||(x==4&&max(r,c)<4)||(x==4&&min(r,c)==2&&max(r,c)==4)||(x==4&&min(r,c)==1&&max(r,c)==4))

    }
}
