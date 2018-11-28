//gskhirtladze

#include <iostream>
#include <stdio.h>

using namespace std;

int t,t1,tmp;
double ans,c,f,x,now,get;

main()
 {
  freopen("out.out","w",stdout);
  cin>>t;
  for (t1=1;t1<=t;t1++)
   {
    cin>>c>>f>>x;
    now=0;
    get=2;
    tmp=10000020;
    ans=1000000000;
    while (tmp--)
     {
      ans=min(ans,now+(x/get));
      now+=(c/get);
      get+=f;
     }
    cout<<"Case #"<<t1<<": ";
    printf("%.7f\n",ans);
   }
 }
