#include<bits/stdc++.h>
#define sd(x) scanf("%d",&x)
using namespace std;


void func(int test)
{
int xox,r,c,attpp,ply,add;


 for(int priyanka=1;priyanka<=test;priyanka++)
 {
     attpp=0,ply=0,add=0;
   sd(xox);
   sd(r);
   sd(c);






    if(r>c) {attpp=c; c=r; r=attpp;}

     if(xox==1)
     {
      cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;

     }


     else if(xox==2)
     {

       if(r==1 && c==1)
       cout<<"Case #"<<priyanka<<": "<<"RICHARD"<<endl;
       else if(r==1 && c==3)
        cout<<"Case #"<<priyanka<<": "<<"RICHARD"<<endl;
       else if(r==3 && c==3)
        cout<<"Case #"<<priyanka<<": "<<"RICHARD"<<endl;
       else
        cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;
     }

     else if(xox==3)
     {
        if(r==2 && c==3)
          cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;
         else if(r==3 && c==3)
         cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;
         else if(r==3 && c==4)
         cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;
         else
         cout<<"Case #"<<priyanka<<": "<<"RICHARD"<<endl;
     }

     else
      {
        if(r==4 && c==4)
        cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;
        else if(r==3 && c==4)
        cout<<"Case #"<<priyanka<<": "<<"GABRIEL"<<endl;
        else
        cout<<"Case #"<<priyanka<<": "<<"RICHARD"<<endl;
      }

}



}


int main()
{

     freopen("apk.in","r",stdin);
     freopen("apppk.out","w",stdout);
 int test;
 sd(test);


       func(test);

return 0;
}
