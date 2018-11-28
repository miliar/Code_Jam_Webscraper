#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
using namespace std;
int mn,pl,sz;
long long ans;
char s[103];
int t;
int main()
{
  // freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
scanf("%d",&t);
for(int tt=1;tt<=t;tt++){
    printf("Case #%d: ",tt);
scanf(" %s",&s);
mn=pl=ans=0;
sz=strlen(s);
for(int i=0;i<sz;i++){
  if(s[i]=='-'){
        mn++;
    }if(s[i]=='+'){
     if(mn){
          ans++;
          mn=0;
    if(pl){ans++;}
pl+=mn;
}
        pl++;
}



        }

if(mn){
     mn=0;
    ans++;
    if(pl){ans++;}
    }
printf("%d\n",ans);
}
    return 0;
}
