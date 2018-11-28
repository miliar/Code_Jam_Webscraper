#include<bits/stdc++.h>
using namespace std;

int main()
{
freopen("k.in","r",stdin);
freopen("k.out","w",stdout);
int test = 0 ;
int t , smax , ans = 0 , current = 0  , i , j  ;
char in[1005] ;

cin >> t;

while(t--)
{
test ++ ;
cin >> smax ;
cin >> in ;
ans = 0 ; current = in[0]-'0' ;

for(i=1;in[i]!='\0';i++)
{
      if(in[i]=='0') continue ;

       if(current>=i){current += in[i]-'0';}
       else {ans += i - current ; current = in[i] - '0' + i ; }


}

cout<<"Case #"<<test<<": "<<ans<<endl;





}

return 0 ;
}
