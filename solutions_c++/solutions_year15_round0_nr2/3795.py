#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAX = 1005;

int table[MAX][MAX];

struct Node {
  int t;
  int count;
  int num;

  Node() {
    t = 0;
    count = 0;
    num = 0;
  }

  bool operator > (const Node& rhs) const {
    return num < rhs.num;
  }
};

int calc(priority_queue<Node, vector<Node>, greater<Node> >& pq){
  int count = 0;
  Node largest = pq.top();

  int mintime = largest.num;

  while (count < mintime) {
    largest = pq.top();
    pq.pop();

    largest.t += 1;
    largest.num = table[largest.count][largest.t];

    if (largest.count - 1 < largest.t) {
      break;
    }

    pq.push(largest);

    count++;
    if (count + pq.top().num < mintime) {
      mintime = count + pq.top().num;
    }
  }
  return mintime;
}

void init() {
  for (int i = 1; i < MAX; i++) {
    for (int j = 0; j < MAX && j < i; j++) {
      if (j == 0)
        table[i][j] = i;
      else {
        int d = i / (j+1);
        int b = i % (j+1);
        if (b == 0) {
          table[i][j] = d;
        }
        else {
          table[i][j] = table[b][b - 1] + d;
        }
      }
    }
  }
}

int main() {
  init();

  int T;
  cin >> T;
  for (int cases = 1; cases <= T; cases++) {
    priority_queue<Node, vector<Node>, greater<Node> > pq;

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
      int val;
      cin >> val;

      Node node;
      node.count = val;
      node.t = 0;
      node.num = table[val][0];

      pq.push(node);
    }
    cout << "Case #" << cases << ": " << calc(pq) << endl;
  }

  return 0;
}