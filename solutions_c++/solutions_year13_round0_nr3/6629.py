#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include<map>
#include <list>
#include <queue>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <sstream>
#include <cmath>
using namespace std;
int main(){
    int x,y,tot,k,l,a,b,v,m;
    //freopen("C:\\Users\\LAPTOPS\\Desktop\\aa.txt","r",stdin);
    //freopen("C:\\Users\\LAPTOPS\\Desktop\\out.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++){
    cin>>a>>b;
    tot=0;x=sqrt(a);y=sqrt(b);
    if(sqrt(a)-x) x+=1;
    
    for(int i=x;i<=y;i++){
            //cout<<i;
           m=i; 
         k=(i*i); int l=v=0;
         
         while(k){
              l=l*10+(k%10);
              if(m){
              v=v*10+(m%10);}
              k=k/10;
              m=m/10;
              }   
            
    if(l==(i*i)&& v==i)   tot++;
}
    //printf("%d\n",tot);
    printf("Case #%d: %d\n",j,tot);
    

}

return 0;
//system("pause");
}
