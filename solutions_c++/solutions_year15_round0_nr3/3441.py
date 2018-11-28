#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int D[9][5]={{0,0,0,0,0},
             {0,1,2,3,4},
             {0,2,5,4,7},
             {0,3,8,5,2},
             {0,4,3,6,5},
             {0,5,6,7,8},
             {0,6,1,8,3},
             {0,7,4,1,6},
             {0,8,7,2,1}},
    R[3]={2,4,5};           

int main(int argc, char *argv[])
{int L,M,i,d,k,T,t,n; string x;
 freopen("C-small.in","r",stdin);
 freopen("C.out","w",stdout);
 cin>>T;
 for(t=1;t<=T;t++)
 {cin>>L>>M>>x;
  //x=string(M,x);
  M*=L;
  for(i=n=0,d=1;i<M;i++,d=D[d][k])
  {if(n<2 && d==R[n])n++;
   k=x[i%L]-'i'+2;
  }
  cout<<"Case #"<<t<<": ";
  if(n<2 || R[n]!=d)cout<<"No";
  else cout<<"Yes";
  cout<<endl;
 }
 //   system("PAUSE");
    return EXIT_SUCCESS;
}
