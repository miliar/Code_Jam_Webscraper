#include<iostream>
using namespace std;
int main()
{
  int t,x,r,c,cs=1;
  cin>>t;
  while(cs<=t)
  {
    int ans =0;
    cin>>x>>r>>c;
    int p = r*c;
    if(x == 1) ans =1;
    if(x == 2 &&  p%2==0)  ans = 1;
    if(x == 3 && (p==6 || p == 9 || p == 12)) ans =1;
    if(x == 4 && (p==12 || p== 16)) ans =1;
    
    if(ans)
    cout<<"Case #" <<cs<<": "<<"GABRIEL\n";
    else
    cout<<"Case #" <<cs<<": "<<"RICHARD\n";
    cs++;

  }
} 
