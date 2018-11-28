#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;
struct Box{
  int x1,y1,x2,y2,idx;
  Box(int x0,int y0,int x1,int y1) {
    this->x1 = x0;
    this->y1 = y0;
    this->x2 = x1 + 1;    
    this->y2 = y1 + 1;    
    this->cost = 999999999;
  }
  bool operator<(const Box &a) const {
    return cost > a.cost;
  }
  int cost;
  int calc(const Box &s) {
    int a,b,c,d;
    a=s.x1;
    b=s.x2;
    c=x1;
    d=x2;
    int xmin = 0;
    if(b < c || d < a) {
      xmin = max(c - b, a - d);
    }
    a=s.y1;
    b=s.y2;
    c=y1;
    d=y2;
    int ymin = 0;
    if(b < c || d < a) {
      ymin = max(c - b, a - d);
    }
    return max(xmin,ymin);
  }
};
int main() {
  int T;
  cin>>T;
  for(int tc=1;tc<=T;tc++) {
    int W,H,N;
    cin>>W>>H>>N;
    vector<Box> box;
    for(int i = 0; i < N;i++){
      int x0,y0,x1,y1;
      cin>>x0>>y0>>x1>>y1;
      box.emplace_back(x0,y0,x1,y1);
      box.back().idx = box.size() - 1;
    }
    // 番兵
    Box start(-1,-1,-1,1000000000);
    Box exit(W,-1,W,1000000000);
    start.cost = 0;
    start.idx = box.size();
    int idx = box.size();
    box.push_back(start);
    exit.idx = box.size();
    box.push_back(exit);
    priority_queue<Box> que;
    que.push(start);
    while(!que.empty()) {
      Box now = que.top();que.pop();
      now = box[now.idx];
      // 移動先を決める
      for(int i = 0; i< box.size(); i++){
        int cost = now.calc(box[i]) + now.cost;
        if(box[i].cost > cost){
          box[i].cost = cost;
          que.push(box[i]);
        }
      }
    }
    cout << "Case #" << tc << ": " << box[box.size()-1].cost<<endl;


  }

}
