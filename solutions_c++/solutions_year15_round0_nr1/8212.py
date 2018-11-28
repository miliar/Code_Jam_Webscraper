#include <iostream>
#include <stdio.h>

using namespace std;
const int zero='0';
int getNumber(){
    int n;
    scanf("%d ",&n);
    char s[n+2];
    gets(s);
    int start=s[0]-zero;
    int newadd=0;
    for(int i=1;i<=n;i++){
        int current=s[i]-zero;
        if(i>start && current!=0){
            int toAdd=i-start;
            start+=toAdd+current;
            newadd+=toAdd;
        }else{
            start+=current;
        }
    }
return newadd;
}
int main()
{
   freopen("data.in","r+",stdin);
   freopen("data.out","w+",stdout);
   int nrt;
   scanf("%d",&nrt);
   for(int i=1;i<=nrt;i++){
    printf("Case #%d: %d\n",i,getNumber());
   }
   fclose(stdin);
   fclose(stdout);
   return 0;
}
