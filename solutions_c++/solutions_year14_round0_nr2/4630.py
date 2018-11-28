#include<iostream>
#include<cstdio>
#define fr(i,n)    for(register int i=0;i<n;i++)
#define llu       long long unsigned
using namespace std;
main()
{int t;
 double a,y,c,f,x,ans;
 cin>>t;
 fr(h,t)
 {cin>>c>>f>>x;
  if(x<=c)
  {cout<<"Case #"<<h+1<<": "<<x/2<<endl;
  }
  else
  {y=x-c;
   a=2;
   ans=c/a;
   while((x/(a+f))<(y/a))
   {a+=f;
    ans+=c/a;
   }
   ans+=y/a;
   cout<<"Case #"<<h+1<<": ";
   printf("%.7f\n",ans);
  }
 }
 //system("pause");
}
