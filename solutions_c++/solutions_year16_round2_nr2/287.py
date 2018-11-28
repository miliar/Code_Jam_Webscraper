#include<cstdio>
#include<string.h>
char str1[21];
char str2[21];
int ans1,ans2;
int n;

bool candoit(int x,int y){
    int gop=1;
    for(int i=n-1;i>=0;i--){
        if(str1[i]=='?'||str1[i]==48+((x/gop)%10)){
            i=i;
        }else{
            return false;
        }
        if(str2[i]=='?'||str2[i]==48+((y/gop)%10)){
            i=i;
        }else{
            return false;
        }
        gop*=10;
    }
    return true;
}

int main(){
    int t;
    int cmp;
    int diff,lim;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        cmp=0;
        diff=1000000;
        lim=1;
        for(int i=0;i<=19;i++) str1[i]='\0';
        for(int i=0;i<=19;i++) str2[i]='\0';
        scanf("%s %s",str1,str2);
        n=(int)strlen(str1);
        for(int i=0;i<n;i++) lim*=10;lim--;
        for(int i=0;i<=lim;i++){
            for(int j=0;j<=lim;j++){
                if(candoit(i,j)){
                    if(i<=j){
                        if(diff>j-i){
                            diff=j-i;ans1=i;ans2=j;
                        }
                    }else{
                        if(diff>i-j){
                            diff=i-j;ans1=i;ans2=j;
                        }
                    }
                }
            }
        }
        if(n==1) printf("Case #%d: %01d %01d\n",turn,ans1,ans2);
        if(n==2) printf("Case #%d: %02d %02d\n",turn,ans1,ans2);
        if(n==3) printf("Case #%d: %03d %03d\n",turn,ans1,ans2);
    }
}
