#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

char s[120010],str[10010];
int get(char c){
    if(c=='i') return 2;
    if(c=='j') return 3;
    return 4;
}
int mul(int x,int y){
    int sign=1;
    if(x<0){sign=-sign;x=-x;}
    if(y<0){sign=-sign;y=-y;}
    if(x==1) return sign*y;
    if(x==2){
        if(y==1) return sign*2;
        if(y==2) return -sign;
        if(y==3) return sign*4;
        return -sign*3;
    }
    if(x==3){
        if(y==1) return sign*3;
        if(y==2) return -sign*4;
        if(y==3) return -sign;
        return sign*2;
    }
    if(x==4){
        if(y==1) return sign*4;
        if(y==2) return sign*3;
        if(y==3) return -sign*2;
        return -sign;
    }
}
int main()
{
    //freopen("1.txt","r",stdin);
    //freopen("2.txt","w",stdout);
    int t,l,x,cas=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&l,&x);
        scanf("%s",str);
        int k=min(x/4,3);
        x=x%4+k*4;
        for(int i=0;i<x;i++)
            strcpy(s+i*l,str);
        int res=1;
        bool f1=false,f2=false;
        for(int i=0;s[i];i++){
            res=mul(res,get(s[i]));
            if(res==2) f1=true;
            if(res==4&&f1) f2=true;
        }
        printf("Case #%d: ",cas++);
        if(f1&&f2&&res==-1) puts("YES");
        else puts("NO");
    }
	return 0;
}
