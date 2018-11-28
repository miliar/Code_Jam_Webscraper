#include<bits/stdc++.h>
using namespace std;

int main()
{

     freopen("pk.in","r",stdin);
     freopen("pk.out","w",stdout);
 int t;
 cin>>t;

 for(int kk=1;kk<=t;kk++)
 {
   int x,r,c,tmp,mul,add;
   cin>>x>>r>>c;

    if(r>c) {tmp=c; c=r; r=tmp;}

     if(x==1)
     {
       cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
     }

     else if(x==2)
     {

       if(r==1 && c==1)
       cout<<"Case #"<<kk<<": "<<"RICHARD"<<endl;
       else if(r==1 && c==3)
        cout<<"Case #"<<kk<<": "<<"RICHARD"<<endl;
       else if(r==3 && c==3)
        cout<<"Case #"<<kk<<": "<<"RICHARD"<<endl;
       else
        cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
     }

     else if(x==3)
     {
       if(r==2 && c==3)
        cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
        else if(r==3 && c==3)
        cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
        else if(r==3 && c==4)
         cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
         else
         cout<<"Case #"<<kk<<": "<<"RICHARD"<<endl;
     }
     else
      {
        if(r==4 && c==4)
        cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
        else if(r==3 && c==4)
        cout<<"Case #"<<kk<<": "<<"GABRIEL"<<endl;
        else
        cout<<"Case #"<<kk<<": "<<"RICHARD"<<endl;
      }

 }

return 0;
}

