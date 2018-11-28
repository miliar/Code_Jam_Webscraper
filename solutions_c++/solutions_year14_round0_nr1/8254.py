#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
  int r1, r2, a[4][4], b[4][4], f[17], n, r;
  int tc;

  cin >> tc;
  for(int p=1;p<=tc;p++)
  { 
    n = 0; r=0;
    for(int i=0;i<17;i++)f[i]=0;
    cin >> r1;
    r1--;
    for(int i=0;i<16;i++)
    {
      cin >> a[i/4][i%4];
      if(r1 == i/4){
        f[a[i/4][i%4]]++;
      }
    }
    cin >> r2;
    r2--;
    for(int i=0;i<16;i++)
    {
      cin >> b[i/4][i%4];
      if(r2 == i/4){
        f[b[i/4][i%4]]++;
      }
    }

    for(int i=1;i<17;i++)
    { 
      //cout << i << ": " << f[i] <<endl;
      if(f[i] == 2)
      {
	n = i;
        r++;
      }
    }

    cout << "Case #" << p << ": ";
    if(r==0){
      cout << "Volunteer cheated!" <<endl;
    }else if(r==1){
      cout << n << endl;
    }else{
      cout << "Bad magician!" << endl;
    }
  }
}
