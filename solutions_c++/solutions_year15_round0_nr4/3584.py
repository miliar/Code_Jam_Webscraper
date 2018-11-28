#include<iostream>

using namespace std;

int main()
 {
  int x,r,c,t,i;
  cin>>t;
  for(i=0;i<t;i++)
   {
    cin>>x>>r>>c;
    switch(x)
     {
      case 1:cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
      case 2:if((r==c&&(r==1||r==3))||(r==1&&c==3)||(r==3&&c==1))     
              cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
             else cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
      case 3:if((r==c&&r!=3)||r==1||c==1||(r==2&&c==4)||(r==4&&c==2))
              cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
             else cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
      case 4:if(r==1||c==1||r==2||c==2||(r==3&&c==3))
              cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
             else cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
     }
   }
  return 0;
 }