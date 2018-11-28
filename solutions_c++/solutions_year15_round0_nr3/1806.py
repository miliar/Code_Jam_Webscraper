#include<bits/stdc++.h>
using namespace std;
string in,s;
//1 -1 i -i j -j k -k
int M[8][8]={
    {0,1,2,3,4,5,6,7},
    {1,0,3,2,5,4,7,6},
    {2,3,1,0,6,7,5,4},
    {3,2,0,1,7,6,4,5},
    {4,5,7,6,1,0,2,3},
    {5,4,6,7,0,1,3,2},
    {6,7,4,5,3,2,1,0},
    {7,6,5,4,2,3,0,1}
};
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int T,l,x,Case=0;
    scanf("%d",&T);
    while(T--){
        bool val=0;
        scanf("%d%d",&l,&x);
        cin>>in;
        s="";
        while(x--)s+=in;
        l=s.size();
        int tmp=0,i;
        for(i=0;i<l;i++){
            if(tmp==2)break;
            if(s[i]=='i')tmp=M[tmp][2];
            else if(s[i]=='j')tmp=M[tmp][4];
            else tmp=M[tmp][6];
        }
        tmp=0;
        for(;i<l;i++){
            if(tmp==4)break;
            if(s[i]=='i')tmp=M[tmp][2];
            else if(s[i]=='j')tmp=M[tmp][4];
            else tmp=M[tmp][6];
        }
        tmp=0;
        for(;i<l;i++){
            if(s[i]=='i')tmp=M[tmp][2];
            else if(s[i]=='j')tmp=M[tmp][4];
            else tmp=M[tmp][6];
        }
        if(tmp!=6)printf("Case #%d: NO\n",++Case);
        else printf("Case #%d: YES\n",++Case);
    }
    return 0;
}
