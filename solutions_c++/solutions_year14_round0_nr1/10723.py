#include<iostream>
using namespace std;
void trick(int [4][4],int [4][4],int,int,int);

int main()
 {
     int test,c1,c2,a[4][4],b[4][4],i,j,cno=1;
     cin>>test;
     while(cno<=test)
     {
        cin>>c1;
         for(i=0;i<4;++i)
           for(j=0;j<4;++j)
             cin>>a[i][j];
        cin>>c2;
        for(i=0;i<4;++i)
         for(j=0;j<4;++j)
            cin>>b[i][j];
        trick(a,b,c1,c2,cno);
        ++cno;
     }
    return 0;
 }

 void trick(int a[4][4],int b[4][4],int c1,int c2,int cno)
  {
      int match=0,x,y,card;
      --c1;
      --c2;
      for(x=0;x<4;++x)
      {
        for(y=0;y<4;++y)
         {
          if(a[c1][x]==b[c2][y])
           {
             ++match;
             card=a[c1][x];
           }
         }
     }
     if(match==0)
        cout<<"Case #"<<cno<<":"<<" "<<"Volunteer cheated!\n";
     else
      if(match==1)
       cout<<"Case #"<<cno<<":"<<" "<<card<<"\n";
      else
       if(match>1)
        cout<<"Case #"<<cno<<":"<<" "<<"Bad magician!\n";
   }
