#include<bits/stdc++.h>


using namespace std;

string cake,happyCake,unhappyCake;

void flipGroup(){
    for(int i=0;i<(signed)cake.length()-1;i++){
        if(cake[i]=='+')cake[i]='-';
        else cake[i]='+';
        if(cake[i+1]==cake[i])break;
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        cin>>cake;
        happyCake="";
        unhappyCake="";
        for(int i=0;i<cake.length();i++){
            happyCake+='+';
            unhappyCake+='-';
        }
        int flips = 0 ;
        //cout<<cake<<endl<<happyCake<<endl<<unhappyCake<<endl;
        while( cake != happyCake && cake != unhappyCake ){
            flipGroup();
            ++flips;
        }
        if(cake==happyCake){
            printf("Case #%d: %d\n",t,flips);
        }
        else printf("Case #%d: %d\n",t,flips+1);
    }
    return 0;
}
