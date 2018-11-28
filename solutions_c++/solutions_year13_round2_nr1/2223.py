#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<fstream>
#include<list>
#include<map>
#include<cstring>
#include<string>
#include<cassert>
#include<algorithm>

using namespace std;

#define FL(i,a,b) for(int i = a; i < b; i++)
#define RESET(a,t,s) memset(a, 0, sizeof(t)*s)
#define BIG 10000000

int *mote;
int dp[105][1000050];
int T, A, N;

void reset() {
  FL(j,0,105)
  FL(k,0,1000050)
    dp[j][k] = BIG;
}

int todo(int pos, int me) {
  if (pos >= N) {
    return 0;
  }
  if (dp[pos][me] < BIG) {
    return dp[pos][me];
  }

  int to_remove = todo(pos+1, me) + 1;

//printf("%d %d: remove - %d\n",pos,me,to_remove);

  int num = 0;
  int temp_size = me;
  while (temp_size <= mote[pos] && temp_size > 1) {
    temp_size += temp_size - 1;
    num++;
  }
  temp_size += mote[pos];
  
  int to_eat = BIG;
  if (me > 1) {
    to_eat = todo(pos+1, temp_size) + num;
  }

//printf("%d %d: eat - %d\n",pos,me,to_eat);

  dp[pos][me] = to_remove < to_eat ? to_remove : to_eat;
  return dp[pos][me];
}

int main(int argc, char *argv[]) {
  ifstream fin(argv[1]);
  ofstream fout(argv[2]);
  
  fin>>T;
  FL(i,0,T) {
    fin>>A>>N;

    mote = new int[N];
    FL(j,0,N)
      fin>>mote[j];
    sort(mote, mote+N);
    reset();

    int ans = todo(0, A);
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
    fout<<"Case #"<<i+1<<": "<<ans<<endl;

    delete []mote;
  }

}
