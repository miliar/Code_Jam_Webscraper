#include<iostream>
#define f(i,n)    for(register int i=0;i<n;i++)
#define llu       long long unsigned
using namespace std;
main()
{int t,r,c,m,n,min,max;
 cin>>t;
 f(h,t)
 {cin>>r>>c>>m;
  min=r<c?r:c;
  max=r>c?r:c;
  n=min*max;
  cout<<"Case #"<<h+1<<":\n";
  if(min==1)
  {if(min==r)
   {cout<<"c";
    f(i,n-m-1)
    cout<<".";
    f(i,m)
    cout<<"*";
   }
   else if(min==c)
   {cout<<"c";
    f(i,n-m-1)
    cout<<"\n.";
    f(i,m)
    cout<<"\n*";
   }
   cout<<endl;
  }
  else if(min==2)
  {if(n-m==2||((n-m)!=1&&(n-m)%2!=0))
   cout<<"Impossible";
   else
   {if(min==r)
    {cout<<"c";
     f(i,((n-m)/2)-1)
     cout<<".";
     f(i,m/2)
     cout<<"*";
     cout<<endl;
     f(i,((n-m)/2))
     cout<<".";
     f(i,m/2)
     cout<<"*";
     if((n-m)==1)
     cout<<"*";
    }
    else if(min==c)
    {if(n-m==1)cout<<"c*";
     else cout<<"c.";
     f(i,(n-m)/2-1)
     cout<<"\n..";
     f(i,m/2)
     cout<<"\n**";
    }
   }
   cout<<endl;
  }
  else
  {if(n-m==2||n-m==3||n-m==5||n-m==7)
   cout<<"Impossible"<<endl;
   else if(n-m==1)
   {f(i,r)
    {f(j,c)
     {if(i==0&&j==0)
      cout<<"c";
      else cout<<"*";
     }
     cout<<endl;
    }
   }
   else if(n-m==4||n-m==6)
   {f(i,r)
    {f(j,c)
     {if(i==0&&j==0)
      cout<<"c";
      else if((i==0||i==1)&&(j<(n-m)/2))
      cout<<".";
      else cout<<"*";
     }
     cout<<endl;
    }
   }
   else if(n-m>2*c+1&&(n-m)%c!=1)
   {f(i,r)
    {f(j,c)
     {if(i==0&&j==0)
      cout<<"c";
      else if(i*c+j<n-m)
      cout<<".";
      else cout<<"*";
     }
     cout<<endl;
    }
   }
   else if(n-m>2*c+1&&(n-m)%c==1)
   {f(i,r)
    {f(j,c)
     {if(i==0&&j==0)
      cout<<"c";
      else if(i*c+j<n-m-2)
      cout<<".";
      else if(i*c+j==n-m-2)
      cout<<"*";
      else if(i*c+j<n-m+1)
      cout<<".";
      else cout<<"*";
     }
     cout<<endl;
    }
   }
   else
   {int d2=(n-m)/2,r2=(n-m)%2;
    if(r2==1)
    {r2=3;
     d2--;
    }
    f(i,r)
    {f(j,c)
     {if(i==0&&j==0)
      cout<<"c";
      else if(i<2&&j<d2)
      cout<<".";
      else if(i==2&&j<r2)
      cout<<".";
      else cout<<"*";
     }
     cout<<endl;
    }
   }
  }
 }
 //system("pause");
}
