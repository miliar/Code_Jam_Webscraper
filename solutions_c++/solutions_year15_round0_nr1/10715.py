#include <iostream>
//#include <fstream>
#include <string.h>

using namespace std;

int main()
{
  int T,i,j;

//  ifstream *fin("inp.txt",ios::in);
//  ofstream *fout("out.txt",ios::out);

  cin>>T;

  for(i=1;i<=T;++i)
  {
    int Sm,val[8],len,ctr=0,max;
    char S[8];

    cin>>Sm;
    cin>>S;

    len=strlen(S);

    for(j=0;j<len;++j)
      val[j]=S[j]-48;

    max=val[0];
    for(j=1;j<len;++j)
    {
      while(val[j]>0&&max<j)
      {
        ++ctr;
        ++max;
      }
      max+=val[j];
    }

    cout<<"Case #"<<i<<": "<<ctr<<endl;
  }
  return 0;
}
