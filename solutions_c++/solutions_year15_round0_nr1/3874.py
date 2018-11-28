#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
const int N=1010;
char str[N];
int main(){
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int T,n;
   cin >> T;
   for(int t=1;t<=T;t++){
        cin >> n;
        cin >> str;
        int sum=0,ans=0;
        for(int i=0;i<n;i++){
            sum+=str[i]-'0';
            if(sum<i+1) {ans+=(i+1-sum);sum=i+1;}
        }
        printf("Case #%d: %d\n",t,ans);

   }
    return 0;
}
