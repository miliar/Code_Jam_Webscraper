#include<iostream>
#include<vector>
#include<set>
#include<queue>
#include<algorithm>
#include<map>
#include<string>

using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
using namespace std;
struct Hrana {
    int x,y,c,t;
    Hrana(int xx,int yy,int cc):  x(xx),y(yy),c(cc),t(0)  {}
    void pripocitaj(int a,int cc);
    int res(int a);
    int sused(int a);

};
void Hrana::pripocitaj(int a,int cc) {
    if(a==x) t+=cc;else t-=cc;
}
int Hrana::sused(int a) {
    if(a==x) return y;
    else return x;
}
int Hrana::res(int a) {
    if(a==x) return c-t;
    return t;
}
/*int rec_block(int x) {
    REP(i,graf[x].size()) if(graf[x][i]->res(x)  &&
            dst[graf[x][i]->sused(x)]-dst[x]=1) {
    if(rec_block(graf[x][i]->sused[x]))  {
        graf[x][i]->prirataj(x,1);
        return 1;
    }
    }
    return 0;
}*/
vector<vector< Hrana*> > graf;
int n;
int max_flow(int source,int target) {
    int res=0;
    while(1) {
        queue<int> q;
        vector<int> dst(n,-1);
        dst[source]=0;
        q.push(source);
        //construct layered graph
        while(!q.empty()) {
            int k=q.front();
            q.pop();
            REP(i,graf[k].size()) if(graf[k][i]->res(k)>0) {
                int x=graf[k][i]->sused(k);
                if(dst[x]==-1) {
                    dst[x]=dst[k]+1;
                    q.push(x);
                }
            }
        }
        if(dst[target]==-1) break;
        //find blocking flow


        vector<int> path(1,source);  // current path, 
        vector<int> next(n,0); // Next edge in graph
        while(!path.empty()) {
        
            int t=path.back();
            if(next[t]==(int)graf[t].size()) {  // if there are no more edges for d, pop it from path
                path.resize(path.size()-1);
                if(path.empty()) break;
                next[path.back()]++;
                    continue;
            }
            if(graf[t][next[t]]->res(t)>0) {
                int s=graf[t][next[t]]->sused(t);
                if(s==target) {  // Found target
                    res++;
                    REP(i,path.size()) {
                        graf[path[i]][next[path[i]]]->pripocitaj(path[i],1);
                        if(graf[path[i]][next[path[i]]]->res(path[i])==0) next[path[i]]++;
                    }
                    path.resize(1);
                } else if(dst[s]-dst[t]==1 && next[s]!=(int)graf[s].size())path.push_back(s); //next level and node has some unclosed edges
                else next[t]++;  // next edge
            } else next[t]++; // next edge
        }
    }
    return res;

}
void addedge(int x,int y) {
  Hrana *a;
 // printf("adding edge %d %d\n",x,y);
  a= new Hrana(x,y,1);
  graf[x].push_back(a);
  graf[y].push_back(a);
}

vector<vector<int> > getGrid() {
  int w,h,n;
  cin >>w>>h>>n;
  vector<vector<int > >  rval=vector<vector<int> >(h, vector<int>(w));
  REP(i,n)  {
    int x0,y0,x1,y1;
    cin>>x0>>y0>>x1>>y1;
    for(int x=x0;x<=x1;++x) for(int y=y0;y<=y1;++y) rval[y][x]=1;
  }
  return rval;
}
int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};
void solve() {
  vector<vector<int> > grid=getGrid();
  int h=grid.size();
  int w=grid[0].size();
  n=2+2*h*w;
  graf = vector<vector< Hrana*> >(n);
  int dest=n-1;
  int src=n-2;
  REP(i,w) if(grid[0][i]==0)addedge(src, i*2);
  REP(i,w) REP(j,h) {
    int x=(w*j+i)*2;
    addedge(x,x+1);
    REP(s,4) {
      int ni=i+dx[s];
      int nj=j+dy[s];
      if(ni>=0 && ni<w && nj>=0 && nj<h && !grid[nj][ni]) {
        int nx=(w*nj+ni)*2;
        addedge(x+1, nx);
      }
    }
  }

  REP(i,w) if(grid[h-1][i]==0)addedge( ((h-1)*w+i)*2+1, dest);
  cout<<max_flow(src, dest);

}
int main() {
int T;cin>>T;
REP(i,T) {
  cout<<"Case #"<<(i+1)<<": ";
  solve();
  cout<<endl;
}
}
