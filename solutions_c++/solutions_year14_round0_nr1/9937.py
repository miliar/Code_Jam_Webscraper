#include <iostream>
using namespace std;
int main()
{
  int t,a1, a2, v1[5][5],v2[5][5], i, j, c=0, v[20], k, r;
  cin>>t;
  while (t--)
  {
    cin>>a1;
    for (i=0; ++i<=4; )
      for (j=0; ++j<=4;)
        cin>>v1[i][j];
    cin>>a2;
    for (i=0; ++i<=4; )
      for (j=0; ++j<=4;)
        cin>>v2[i][j];
    k=0;
    for (i=0; ++i<=16; v[i]=0  );
    for (i=0; ++i<=4; )
      v[ v1[a1][i]  ]=1;
    for (i=0; ++i<=4; )
      if ( v[ v2[a2][i]  ]==1 ) ++k, r=v2[a2][i];
    if (k==1)
      cout<<"Case #"<<++c<<": "<<r<<endl;
    else if (k>1) cout<<"Case #"<<++c<<": Bad magician!"<<endl;
    else cout<<"Case #"<<++c<<": Volunteer cheated!"<<endl;
  }
  return 0;
}