#include<iostream>
using namespace std;
int main(){
int T;
cin>>T;
for(int i=0;i<T;i++){
int X,R,C;
cin>>X>>R>>C;
switch(X){
case 1:
cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
break;
case 2:
if((R*C)%2!=0)
cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
else
cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
break;
case 3:
if((R*C)%3!=0)
cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
else if((R>1&&C>2)||(R>2&&C>1))
cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
else
cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
break;
case 4:
if((R*C)%4!=0)
cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
else if((R>2&&C>3)||(R>3&&C>2))
cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
else
cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
break;
}
}
return 0;
}
