#include <algorithm>
#include <iostream>
#include <queue>
#include <map>
#include <vector>
using namespace std;

typedef long long int64;

const int64 mod = 1000002013;

struct vertex;
struct edge
{
   vertex *from, *to;
   int64 used, mi, ma; // min may be -max
   int64 unitCost; // Cost using one unit of this edge

   int64 cost(vertex* p) { return (p==from?unitCost:-unitCost);}

   vertex* opposite(vertex* p)
   { return (p == from ? to : from); }
   int64 left(vertex* p) // Source vertex, capacity left from p
   { return (p == from ? ma - used : used - mi); }
   void add(vertex* p, int64 flow) // Source vertex, add from p
   { used += (p == from ? flow : -flow); }
};
struct vertex
{
   vector<edge*> e; // Edge index
   edge* in; // Incoming edge, used in the breath first search
   int64 cost; // Cost used in Dijkstra’s algorithm
};

vertex v[2013];
edge e[2013*2013];
int numv = 0;
const int eSpecialIdx = 2013*2000;
int numNormalE;


typedef pair<int64, vertex*> elem; // pri_q element [-cost, v]

bool AugPath(vertex* source, vertex* dest)
{
   // Dijkstra’s algorithm
   for(int i = 0; i < numv; ++i)
      v[i].cost = 0x3FFFFFFFFFFFFFFFLL;
   source->cost = 0;
   source->in = (edge*)-1; // reinterpret_cast<edge*>(-1)

   priority_queue<elem, vector<elem>, greater<elem> > pq;
   pq.push(elem(0, source));
   while(!pq.empty()) {
      elem curElem = pq.top();
      vertex* cur = curElem.second;
      if(cur == dest)
         return true; // Finished!
      pq.pop();
      if(cur->cost != curElem.first) // Was this the best?
         continue;
      // Check edges
      for(vector<edge*>::iterator it = cur->e.begin();
         it != cur->e.end(); ++it)
      {
         if((*it)->left(cur) > 0) {
            vertex* recv = (*it)->opposite(cur);
            int64 newCost = curElem.first +(*it)->cost(cur);
            if(newCost < recv->cost) {
               recv->cost = newCost;
               recv->in = *it;
               pq.push(elem(newCost, recv));
            }
         }
      }
   }
   return false;
}

int64 MaxFlow(vertex* source, vertex* dest)
{
   int64 maxflow = 0;
   while(AugPath(source, dest))
   {
      // Find flow to add
      int64 flow = 0x7FFFFFFFFFFFFFFFLL;
      edge* e;
      vertex* sender = dest; // The sender (in the loop)
      while((e = sender->in) != (edge*)-1)
         flow=min(flow,e->left(sender=e->opposite(sender)));
      // Add the flow
      sender = dest;
      while((e = sender->in) != (edge*)-1)
         e->add(sender = e->opposite(sender), flow);
      maxflow += flow;
   }
   return maxflow;
}


struct input_data
{
   int o, e, p;
};

int main()
{
   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
   {
      int64 n;
      int m;
      cin >> n >> m;
      std::map<int, int> stations;
      std::vector<input_data> inputData(m);
      int64 oldCost = 0;
      for (int i = 0; i < m; ++i)
      {
         input_data &id = inputData[i];
         cin >> id.o >> id.e >> id.p;
         stations.insert(make_pair(id.o, (int)stations.size()));
         stations.insert(make_pair(id.e, (int)stations.size()));
         int64 k = id.e - id.o;
         int64 unitCost = (k*(n+n+1-k)/2) % mod;
         oldCost += (id.p*unitCost) % mod;
         oldCost = oldCost % mod;
      }
      numv = stations.size();
      const int inVIdx = numv++;
      const int outVIdx = numv++;
      v[inVIdx].e.clear();
      v[outVIdx].e.clear();
      for (int i = 0; i < (int)stations.size(); ++i)
      {
         v[i].e.clear();

         int ei = eSpecialIdx+2*i;
         e[ei].from = &v[inVIdx];
         e[ei].to = &v[i];
         e[ei].used = 0;
         e[ei].mi = 0;
         e[ei].ma = 0;
         e[ei].unitCost = 0;
         v[i].e.push_back(&e[ei]);
         v[inVIdx].e.push_back(&e[ei]);

         ei = eSpecialIdx+2*i+1;
         e[ei].from = &v[i];
         e[ei].to = &v[outVIdx];
         e[ei].used = 0;
         e[ei].mi = 0;
         e[ei].ma = 0;
         e[ei].unitCost = 0;
         v[i].e.push_back(&e[ei]);
         v[outVIdx].e.push_back(&e[ei]);
      }
      for (int i = 0; i < m; ++i)
      {
         const input_data &id = inputData[i];
         // Input edge.
         int ine = eSpecialIdx+2*stations[id.o];
         e[ine].ma += id.p;

         // Output edge
         int oute = eSpecialIdx+2*stations[id.e]+1;
         e[oute].ma += id.p;
      }
      // Set paths between stations
      numNormalE = 0;
      for (auto it = stations.begin(); it != stations.end(); ++it)
      {
         for (auto jt = stations.begin(); jt != stations.end(); ++jt)
         {
            if (jt->first <= it->first)
               continue;
            int is = it->second;
            int js = jt->second;
            edge &mye = e[numNormalE++];
            mye.from = &v[is];
            mye.to = &v[js];
            mye.used = 0;
            mye.mi = 0;
            mye.ma = 0x3FFFFFFFFFFFFFFFLL;
            int64 k = jt->first - it->first;
            mye.unitCost = k*(int64)(n+n+1-k)/2;
            v[is].e.push_back(&mye);
            v[js].e.push_back(&mye);
         }
      }

      int64 maFl = MaxFlow(&v[inVIdx], &v[outVIdx]);
      cerr << "Flow: " << maFl << endl;
      int64 newCost = 0;
      for (int i = 0; i < numNormalE; ++i)
      {
         newCost += (e[i].used * e[i].unitCost) % mod;
         newCost %= mod;
      }
      int64 ret = (oldCost - newCost + mod) % mod;
      cout << "Case #" << (t+1) << ": " << ret << endl;
   }
   return 0;
}
