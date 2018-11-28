#include<iostream>
#define f(i,n)    for(register int i=0;i<n;i++)
#define llu       long long unsigned
using namespace std;
main()
{int t,a,am[4][4],b,bm[4][4],ansl[4],ans;
 cin>>t;
 f(h,t)
 {cin>>a;
  f(i,4)
  f(j,4)
  cin>>am[i][j];
  f(i,4)
  ansl[i]=am[a-1][i];
  //f(i,4)
  //cout<<ansl[i]<<" ";
  //cout<<endl;
  cin>>b;
  f(i,4)
  f(j,4)
  cin>>bm[i][j];
  int ansn=0;
  f(i,4)
  {f(j,4)
   {if(bm[b-1][j]==ansl[i])
    {ansn++;
     ans=ansl[i];
     //cout<<"ndknd"<<ansn<<" "<<ans<<endl;
     break;
    }
   }     
  }
  cout<<"Case #"<<h+1<<": ";
  if(ansn==0)
  cout<<"Volunteer cheated!"<<endl;
  else if(ansn==1)
  cout<<ans<<endl;
  else cout<<"Bad magician!"<<endl;
 }
 //system("pause");
}
