#include <bits/stdc++.h>
using namespace std;

int main(){
int T;scanf("%d",&T);
for(int Y=1;Y<=T;Y++){
int max;
scanf("%d",&max);
string s;
cin >>s;
int C=0;
int ans=0;
for(int i=0;i<s.size();i++){
int number=s[i]-'0';
if(C<i){ans+=i-C;C=i;}
C+=number;
}
printf("Case #%d: %d\n",Y,ans);
}

}
