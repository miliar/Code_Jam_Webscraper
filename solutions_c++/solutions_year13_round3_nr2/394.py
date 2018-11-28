#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
#include<queue>

using namespace std;

typedef long long ent;
typedef pair<ent, ent> pe;

const int N=1000;

ent to_tab(ent x, ent y){
  return 2*N*(x+N)+(y+N);
}

pe from_tab(ent n){
  return pe(n/(2*N)-N,n%(2*N)-N);
}

struct triple{
  ent x, y, d;
  triple(ent a=0, ent b=0, ent di=0){
    x=a; y=b; d=di;
  }
};

void bfs(ent ex, ent ey, vector<ent> & pred){
  queue<triple> q;
  q.push(triple(0,0,1));
  while(!q.empty()){
    triple curr=q.front();
    //   cerr << curr.x << ' ' << curr.y << ' ' << curr.d << endl;
    q.pop();
    if(abs(curr.x)+curr.d>N/2 || abs(curr.y)+curr.d>N/2)
      continue;
    if(curr.x==ex && curr.y==ey)
      return;
    ent cc=to_tab(curr.x, curr.y);
    ent next;
    
    next=to_tab(curr.x+curr.d, curr.y);
    if(pred[next]==-1 && curr.x!=ex){
      q.push(triple(curr.x+curr.d, curr.y, curr.d+1));
      pred[next]=cc;
    }

    next=to_tab(curr.x-curr.d, curr.y);
    if(pred[next]==-1 && curr.x!=ex){
      q.push(triple(curr.x-curr.d, curr.y, curr.d+1));
      pred[next]=cc;
    }

    next=to_tab(curr.x, curr.y+curr.d);
    if(pred[next]==-1 && curr.y!=ey){
      q.push(triple(curr.x, curr.y+curr.d, curr.d+1));
      pred[next]=cc;
    }

    next=to_tab(curr.x, curr.y-curr.d);
    if(pred[next]==-1 && curr.y!=ey){
      q.push(triple(curr.x, curr.y-curr.d, curr.d+1));
      pred[next]=cc;
    }
  }
}

int main(){
  int nbcase;
  cin >> nbcase;
  for(int icase=1;icase<=nbcase;++icase){
    cout << "Case #" << icase << ": ";
    ent x, y;
    cin >> x >> y;
    vector<ent> pred(4*N*N,-1);

    bfs(x, y, pred);
    
    // cerr << "Ok" << endl;

    ent curr=to_tab(x,y);
    vector<pe> res;
    res.push_back(from_tab(curr));
    while(pred[curr]!=to_tab(0,0)){
      curr=pred[curr];
      res.push_back(from_tab(curr));
    }
    res.push_back(pe(0,0));

    reverse(res.begin(), res.end());

    /*
    for(int i=0;i<int(res.size());++i)
      cout << res[i].first << ' ' << res[i].second << endl;
    */

    for(int i=0;i<int(res.size())-1;++i){
      if(res[i].first<res[i+1].first) cout << 'E';
      if(res[i].first>res[i+1].first) cout << 'W';
      if(res[i].second<res[i+1].second) cout << 'N';
      if(res[i].second>res[i+1].second) cout << 'S';
    }
    cout << '\n';
  }
}
