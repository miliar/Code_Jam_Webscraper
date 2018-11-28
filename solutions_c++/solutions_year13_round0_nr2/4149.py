#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int main()
{
  int print, first, tcases, n, m, it, tot, low, lowtot, grass[10000];
  int begrow, finrow, begcol, fincol, mov, notgood, done;
  cin>>tcases;
  print = 1;
  while(tcases--)
  {
    cout<<"Case #"<<print<<": ";
    print++;
    first = 1;
    notgood = 0;
    cin>>n>>m;
    tot = n*m;
    for(it=0;it<tot;it++)
      cin>>grass[it];

    for(it=0;it<tot;it++)
    {
      notgood = 0;
      done = 0;
      if(it>=m)
      {
        begrow = it - it%m;
        finrow = begrow + m;
        begcol = it%m;
        fincol = tot;
      }
      else
      {
        begrow = 0;
        finrow = m;
        begcol = it;
        fincol = tot;
      }
      for(mov=begrow;mov<finrow;mov++)
        if(grass[mov] > grass[it])
        {
          notgood++;
          break;
        }
      for(mov=begcol;mov<fincol;mov+=m)
        if(grass[mov] > grass[it])
        {
          notgood++;
          break;
        }
      if(notgood == 2)
      {
        cout<<"NO"<<endl;
        done = 1;
        break;
      }
    }
    if(!done) cout<<"YES"<<endl;
  }
  return 0;
}
