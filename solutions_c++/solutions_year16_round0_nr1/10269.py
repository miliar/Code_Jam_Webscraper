#include <bits/stdc++.h>
using namespace std;
int Map[10] = {0};
int renewmap() {
  for(int i=0;i<10;i++){
    Map[i] = 0;
  }
  return 1;
}
void mapall(int num) {
  while(num) {
    int rem = num % 10;
    num = num / 10;
    ++Map[rem];
  }
}

int check() {
  for (int i = 0; i < 10; ++i)
  {
    if(Map[i] == 0)
      return 0;
  }
  return 1;
}

void printmap() {
  cout<<endl<<"{ ";
  for (int i = 0; i < 10; ++i)
  {
    if(Map[i] == 0) cout<<i;
  }
  cout<<" }";
}
int main(int argc, char const *argv[])
{

  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  int t;cin>>t;
  for (int T = 1; T <= t; ++T)
  {
    if(renewmap() == 1)
    {int count = 0, N;
        cin>>N;
        if(N == 0){cout<<"Case #"<<T<<": INSOMNIA"<<endl;}
else {
        while(check() == 0) {
          //printmap();
          ++count;
          mapall(N * count);
          //cout<<"-"<<(N*count)<<"-"<<endl;
        }//end of while
        cout<<"Case #"<<T<<": "<<(N*count)<<endl;
      }//end of else
    }//end of if
  }//end of for
  return 0;
}//end of main