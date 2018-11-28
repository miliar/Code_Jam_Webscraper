#include<bits/stdc++.h>
using namespace std;
int main(){
freopen("Input.txt","r",stdin);
freopen ("Output.txt","w",stdout);
int t,cnt,i;
scanf("%d",&t);
long long int num,tmp;
for(int te=0;te<t;te++){
   i=1;
   set<int>st;
   scanf("%lld",&num);
   printf("Case #%d: ",te+1);
   if(num==0){
    printf("INSOMNIA\n");
    continue;
   }
   do{
    tmp=num*i;
    while(tmp){
    st.insert(tmp%10);
   tmp/=10;
}
i++;
}while(st.size()!=10);
i--;
printf("%lld\n",i*num);
}
return 0;
}
