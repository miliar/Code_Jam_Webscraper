#include<bits/stdc++.h>
using namespace std;

int i,t1,t,nr;
long long n,aux;
bool viz[10];

int main()
{
  ifstream cin("A-large.in");
  ofstream cout("output.txt");

  ios_base::sync_with_stdio(0); cin.tie(0);

  cin>>t1;
  for(t=1;t<=t1;++t)
  {
    cin>>n;
    cout<<"Case #"<<t<<": ";

    if(!n)
    {
      cout<<"INSOMNIA\n";
      continue;
    }

    memset(viz,0,sizeof(viz));

    for(i=1,nr=0;nr!=10;++i)
    {
      aux=n*i;
      while(aux)
      {
        if(!viz[aux%10]) ++nr,viz[aux%10]=1;
        aux/=10;
      }

      if(nr==10) cout<<n*i<<'\n';
    }
  }

 return 0;
}
