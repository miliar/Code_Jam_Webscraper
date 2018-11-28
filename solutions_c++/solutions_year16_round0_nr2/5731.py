#include<iostream>
#include<cstdio>
#include<stack>
#include<cstring>

using namespace std;

int main(){
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);

int t,len,c,ans;
char str[1000];
scanf("%d",&t);
c=0;
while(t--){
++c;
scanf("%s",&str);
len = strlen(str);

int f = 0,ans=0;
while(1){
  char ch = str[0];
  int l=0;

  for(int i=1;i<len;i++){
    if(ch != str[i]) {
        break;
    }
    l = i;
  }

  if(l != len-1 || ch != '+'){
     for(int i=0;i<=l;i++){
        if(str[i]=='+') str[i] = '-';
        else str[i] = '+';
     }
     ++ans;
  }

  ch = str[0];
  //printf("%d -> %s\n",ans,str);
  if(l==len-1 && ch=='+'){
    printf("Case #%d: %d\n",c,ans);
    break;
  }
}

}

return 0;
}
