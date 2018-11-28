//gskhirtladze

#include <iostream>
#include <stdio.h>

using namespace std;

int t,t1,n,i,tot,a,pos[50000],ind,j;

main()
 {
  freopen("out.out","w",stdout);
  cin>>t;
  for (t1=1;t1<=t;t1++)
   {
    cin>>n;
    for (i=0;i<=1000;i++)
     pos[i]=2;
    for (i=1;i<=4;i++)
     for (j=1;j<=4;j++)
      {
       cin>>a;
       if (i == n) pos[a]--;
      }
    cin>>n;
    for (i=1;i<=4;i++)
     for (j=1;j<=4;j++)
      {
       cin>>a;
       if (i == n) pos[a]--;
      }
     tot=0;
     ind=0;
    for (i=1;i<=1000;i++)
     if (pos[i] == 0)
      { tot++; ind=i; }
     cout<<"Case #"<<t1<<": ";
     if (tot >= 2)
      { cout<<"Bad magician!"<<endl; continue; }
     if (tot == 1) cout<<ind<<endl; else
      cout<<"Volunteer cheated!"<<endl;
   }
 }
