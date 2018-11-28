#include<iostream.h>
#include<conio.h>
#include<math.h>
void main()
{int ntc;cin>>ntc;
for(int c=1;c<=ntc;c++)
{cout<<"Case #"<<c<<": ";
int x,y; cin>>x>>y;
int x1=0,y1=0,curr=1;
 while(x!=x1) { if(x>0)   {if((x-x1)>=curr) {cout<<"E";x1=x1+curr;curr++;} else {cout<<"WE";curr=curr+2;x1++;      }    }   else {    if((x1-x)>=curr) {cout<<"W";x1=x1-curr;curr++;} else {cout<<"EW";curr=curr+2;x1--;      }               }}
 while(y!=y1) { if(y>0)   {if((y-y1)>=curr) {cout<<"N";y1=y1+curr;curr++;} else {cout<<"SN";curr=curr+2;y1++;      }    }   else {    if((y1-y)>=curr) {cout<<"S";y1=y1-curr;curr++;} else {cout<<"NS";curr=curr+2;y1--;      }       }}

cout<<endl;

}}