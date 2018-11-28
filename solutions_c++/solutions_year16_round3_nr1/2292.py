#include "mylib.h"


// "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
// Z-0 X-6 

void fix(vla<int> &a, vla<int> &v, char c, int val, charp s) {
  int count=v[c];
  if (0==count) return;
  a[val]=count;
  charp t=s;
  while (*t) {
    char i=*t++;
    v[i]=v[i]-count;
  }
}

class n_room {
public:
  char c;
  int count;
  void dump(std::ostream &out) { out<<"c="<<c<<" count="<<count; }
};

bool roomSort(n_room i, n_room j) { return i.count>j.count; }


void solve(int no, mifstream &fi, mofstream &fo) {
  fo<<"Case #"<<no<<":";
  int n_count=fi.nextInt();
  vla<n_room> v(n_count);
  int tot_count=0;
  for (int i=0; i<n_count; i++) {
    n_room r;
    r.c=(char)('A'+i);
    r.count=fi.nextInt();
    tot_count+=r.count;
    v.push_back(r);
  }
  for (;;) {
    sort(v.begin(), v.end(), roomSort);
    // cout<<"--"<<endl;  v.dumpx();
    n_room r1=v[0];
    n_room r2=v[1];
    if (r1.count>(tot_count/2)) {
      cout<<"error"<<endl;
    }

    if (r1.count==0) {
      break;
    }
    if (r1.count>=r2.count+2) {
      // take two from r1
      v[0].count-=2;
      tot_count-=2;
      fo<<' '<<r1.c<<r1.c;
      continue;
    }
    if (r1.count>r2.count) {
      // take one from r1
      v[0].count-=1;
      tot_count-=1;
      fo<<' '<<r1.c;
      continue;
    }
    if (2<n_count && v[2].count>0) {
      // take one from r1
      v[0].count-=1;
      tot_count-=1;
      fo<<' '<<r1.c;
      continue;
    }
    else {
      // take one from r1
      v[0].count-=1;
      v[1].count-=1;
      tot_count-=2;
      fo<<' '<<r1.c<<r2.c;
      continue;
    }
  }
  fo<<endl;
}

int solve_all(mifstream &fi, mofstream &fo) {
  int count=fi.nextInt();
  for (int i=1; i<=count; i++) {
    solve(i, fi, fo);
  }
  return 0;
}

