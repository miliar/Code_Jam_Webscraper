#include<iostream>
using namespace std;
int main()
{int T;
cin>>T;
for(int i=1;i<=T;i++)
{int X,R,C;
cin>>X>>R>>C;
if(X%2!=0)
{if(((R>=X&&C>=(X/2)+1)||((R>=(X/2)+1)&&C>=X))&&((R*C)%X)==0)
{cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;}
else{cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;}
}
else if(X==4&&((R==2&&C>=3)||(C==2&&R>=3))){cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;}
else if(X%2==0)
{if(((R>=X&&C>=(X/2))||((R>=(X/2))&&C>=X))&&((R*C)%X)==0)
{cout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;}
else{cout<<"Case #"<<i<<": "<<"RICHARD"<<endl;}
}
}
return 0;
}
