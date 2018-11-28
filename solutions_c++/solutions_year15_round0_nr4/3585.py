#include<iostream>
using namespace std;

int main()
 {
  int x,r,y,c,i;
  cin>>c;
  for(i=0;i<c;i++)
   {
    cin>>x>>r>>y;
    switch(x)
     {
      case 1:cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
      case 2:if((r==y&&(r==1||r==3))||(r==1&&y==3)||(r==3&&y==1))     
              cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
             else cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
      case 3:if((r==y&&r!=3)||r==1||y==1||(r==2&&y==4)||(r==4&&y==2))
              cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
             else cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
      case 4:if(r==1||y==1||r==2||y==2||(r==3&&y==3))
              cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
             else cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
             break;
     }
   }
  return 1;
 }