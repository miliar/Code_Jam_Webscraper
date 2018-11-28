#include <iostream>
#include <cstdlib>
#include <map>
#include <cstring>
#include <climits>
#include <queue>

using namespace std;

class Sdata {
  public:
    Sdata(char *s, int w) : s_(strdup(s)), weight_(w) {
    }
    virtual ~Sdata() {
      free(s_);
    }
    Sdata *flip(int len, int weight) {
      char *new_s = strdup(s_);
      for (int i = 0; i < (len+1)/2; ++i) {
        char t = new_s[i];
        new_s[i] = new_s[len - i - 1];
        new_s[len - i - 1] = t;
      }
      for (int i = 0; i < len; ++i) {
        new_s[i] = (new_s[i] == '+') ? '-' : '+';
      }

      Sdata *new_d = new Sdata(new_s, weight);
      free(new_s);
      return new_d;
    }

    const char *data() { return s_; }
    void set_weight(int w) {
      weight_ = w;
    }
    int weight() const { return weight_; }

  private:
    char *s_;
    int weight_;
};

struct cmp_sdata {
  bool operator()(Sdata *a, Sdata *b) {
    return strcmp(a->data(), b->data()) < 0;
  }
};

struct cmp_sdata_weight {
  bool operator()(Sdata *a, Sdata *b) {
    return (a->weight() > b->weight());
  }
};

typedef map<Sdata*, int, cmp_sdata> data_map_t;

void solve(char *s) {
  data_map_t visited;
  priority_queue<Sdata*, vector<Sdata*>, cmp_sdata_weight> order_q;

  int len = strlen(s);
  char *goal_str = strdup(s);
  for (int i = 0; i < len; ++i) {
    goal_str[i] = '+';
  }

  Sdata *goal = new Sdata(goal_str, INT_MAX);
  order_q.push(goal);

  Sdata *root = new Sdata(s, 0);
  order_q.push(root);
  
  while (!order_q.empty()) {
    Sdata *d = order_q.top();
    order_q.pop();
    data_map_t::iterator item = visited.find(d);
    if (item != visited.end()) {
      // Found a visited node. Update table with lesser value.
      item->second = min(item->second, d->weight());
      if (item->second != item->first->weight()) {
        item->first->set_weight(item->second);
      }
      //delete d;
      continue;
    }

    visited[d] = d->weight();

    if (!strcmp(goal_str, d->data())) {
      continue;
    }

    for (int i = 1; i <= len; ++i) {
      Sdata *new_d = d->flip(i, d->weight() + 1);
      order_q.push(new_d);
    }
  }

  cout << visited[goal];
}

int main(int argc, char **argv) {
  int T;
  char S[101];

  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> S;
    cout << "Case #" << i+1 << ": ";
    solve(S);
    cout << endl;
  }
  return 0;
}

