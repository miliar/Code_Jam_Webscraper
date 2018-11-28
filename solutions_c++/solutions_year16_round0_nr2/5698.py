#include<iostream>

using namespace std;

string inp;
char temp;

inline void reverse(int b){
  if(b==0){
    inp[0]='+';
  }
  else
  for(int i=0;i<=b/2;i++){
    if(inp[i]=='-')
      inp[i]='+';
    else
      inp[i]='-';
    if(i!=b-i){
      if(inp[b-i]=='+')
        inp[b-i]='-';
      else
        inp[b-i]='+';
    }
    temp=inp[i];
    inp[i]=inp[b-i];
    inp[b-i]=temp;
    //cout<<b<<" "<<inp<<endl;
  }
}

int main(){
  int tt,t,i,j,k,ans,flag,flag2;
  scanf("%d",&t);
  tt=t;
  while(t--){
    ans=0;
    cin>>inp;
    while(1){
      flag=1;
      for(i=0;i<inp.length();i++)
        if(inp[i]=='-'){
          flag=0;
          break;
        }
      if(flag)
        break;
      for(j=0;j<i;j++){
        if(inp[j]=='+'){
          inp[j]='-';
          flag2=1;
        }
      }
      if(flag2)
        ans++;
      flag2=0;
      //cout<<inp<<endl;
      for(i=0;i<inp.length();i++)
        if(inp[i]=='-')
          j=i;
      reverse(j);ans++;
      //cout<<inp<<endl;
    }
    cout<<"Case #"<<tt-t<<": "<<ans<<endl;
  }
  return 0;
}
