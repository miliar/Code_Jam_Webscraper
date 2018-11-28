#include <iostream>
#include <set>
using namespace std;

int bff[2000], N, loop[2000], res[2000];
set<int> gset[2000];

int path_to(int dest, set<int>& myset) {
  int ret = 0, kptst = 0;

  for (int st=1; st<=N; ++st) {
    if (myset.find(st)!=myset.end()) continue;
    set<int> inset;
    int now=st, count=1;
    inset.insert(now);

    while (1) {
      if (bff[now]==dest) {
        if (count>ret) {ret=count; kptst=st;}
        break;
      }
      if (myset.find(bff[now])!=myset.end()) break;
      if (inset.find(bff[now])!=inset.end()) break;

      now = bff[now];
      inset.insert(now);
      ++count;
    }
  }

  if (kptst) {
    int st = kptst;
    int now=st, count=1;
    myset.insert(now);

    while (1) {
      if (bff[now]==dest) {
        break;
      }
      if (myset.find(bff[now])!=myset.end()) break;

      now = bff[now];
      myset.insert(now);
      ++count;
    }
  }

  return ret;
}

int sol(int startid) {
  int link[2000]={0};
  int pos=0, now, work=0;

  now = startid;
  gset[startid].insert(now);
  link[pos++] = now;

  while (1) {
    if (bff[now]==link[0]) break;
    else if (pos>=2 && bff[now]==link[pos-2]) {work=1; break;}
    else if (gset[startid].find(bff[now])==gset[startid].end()) {
      now = bff[now];
      gset[startid].insert(now);
      link[pos++] = now;
    }
    else return -1;
  }
  if (!work) {
    loop[startid] = (pos>=3);
    return pos;
  }

  loop[startid] = 0;
  return pos + path_to(link[pos-1], gset[startid]);
} 

int ans() {
  int maxlop = 0;
  int ans2=0, tmpmax=0, tmpmaxid=0;
  set<int> fset;

  for (int i=1; i<=N; ++i) {
    if (loop[i] && res[i]>maxlop) maxlop=res[i];
  }

  while (1) {
    tmpmax=0;
    tmpmaxid=0;

    for (int i=1; i<=N; ++i) {
      if (loop[i]) continue;
      if (fset.find(i)!=fset.end()) continue;
      
      if (res[i]>tmpmax) {
        tmpmax = res[i];
        tmpmaxid = i;
      }
    }
    if (tmpmaxid==0) break;
    //cout<<"tmpmax"<<tmpmax<<"id "<<tmpmaxid<<endl;

    int add=1;
    for (set<int>::iterator iter = gset[tmpmaxid].begin(); iter!=gset[tmpmaxid].end(); ++iter) {
      if (fset.find(*iter)!=fset.end()) add=0;
      fset.insert(*iter);
      //cout<<*iter<<endl;
    }
    if (add) ans2 += tmpmax;

  }
  return ans2>maxlop? ans2:maxlop;
}

int main() {
  int cas, T;

  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cin>>N;
    for (int i=1; i<=N; ++i) {
      cin>>bff[i];
      gset[i].clear();
    }

    for (int i=1; i<=N; ++i) {
      res[i] = sol(i);
    }


    cout<<"Case #"<<cas<<": "<<ans()<<endl;
  }
  return 0;
}
