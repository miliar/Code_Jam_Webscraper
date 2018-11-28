#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

static const int N = 201;
bool connect[N][N];

class Treasure {
  public:
  Treasure() {
    for (int i = 0; i < N; ++i)
      fill_n(keys_[i], N, 0);
    fill_n(chests_, N, 0);
    fill_n(available_, N, 0);
  }
  Treasure(const Treasure &t) {
    for (int i=0; i<N; ++i)
      copy(t.keys_[i], t.keys_[i] + N, keys_[i]);
    copy(t.chests_, t.chests_ + N, chests_);
    copy(t.available_, t.available_ + N, available_);
  }
  virtual ~Treasure() {};
  virtual bool findOrder(int *) = 0;

  virtual void addAvailable(int k) {
    ++available_[k];
  }

  virtual void setChest(int c, int k) {
    chests_[c] = k;
  }

  virtual void addKey(int c, int k) {
    ++keys_[c][k];
  }

  protected:
  int available_[N];
  int keys_[N][N];
  int chests_[N];
};

class SmallTreasure : public Treasure {
  static const int M = 20;
  public:
  SmallTreasure() {
    fill_n(opened_, 1U << M, 0);
  }

  bool findOrder(int *order) {
    unsigned m = 0;
    if (!open(0)) return false;
    for (int i = 0; chests_[i]; ++i) {
      if (m & (1U << i)) continue;
      if (opened_[m | (1U << i)] > 0) {
        *(order++) = i;
        m |= 1U << i;
        i = -1; 
        continue;
      }
    }
    return true;
  }

  private:
  bool open(unsigned m) const {
    if (opened_[m]) return opened_[m] > 0;

    opened_[m] = -1;
    int available[N];
    copy(available_, available_ + N, available);
    int r = 0;
    for (int i = 0; chests_[i]; ++i) {
      if (!(m & (1U << i))) {
        ++r;
        continue;
      }
      for (int j = 0; j < N; ++j) {
        available[j] += keys_[i][j];
      }
      --available[chests_[i]];
    }
    if (!r) {
      opened_[m] = 1;
      return true;
    }
    for (int i = 0; chests_[i]; ++i) {
      if (m & (1U << i)) continue;
      if (available[chests_[i]] && open(m | (1U << i))) {
        opened_[m] = 1;
        return true;
      }
    }
    return false;
  }

  mutable int opened_[1U << M];
};

class BigTreasure : public Treasure{
  public:
  BigTreasure() {
  }

  BigTreasure(const BigTreasure &t) : Treasure(t) {
  }


  bool check() {
    if (!checkBalance()) return false;
    for (;;) {
      easyMoves();
      if (checkEnd()) return true;
      int c = findCycle();
      if (!c) return false;
      move(c);
    } 
  }

  bool findOrder(int *order) {
    if (checkEnd()) return true;
    BigTreasure t(*this);
    if (!t.check()) 
      return false;
    
    for (int i = 0; i < N; ++i) {
      if (!available_[chests_[i]]) continue;
      BigTreasure t2(*this);
      t2.move(i);
      if (!t2.check()) continue;
      move(i);
      *order = i;
      return findOrder(order + 1);
    }
    printf("XXXX\n");
    return false;
  }

  private:

  void move(int c) {
    --available_[chests_[c]];
    for (int i = 0; i < N; ++i) {
      available_[i] += keys_[c][i];
      keys_[c][i] = 0;
    }
    chests_[c] = 0;
  }

  void moveAll(int k) {
    for (int i = 0; i < N; ++i) {
      if (chests_[i] == k) {
        move(i);
      }
    }
    available_[k] = 0;
  }

  void easyMoves() {
    int balance[N];
    fill_n(balance, N, 0);
    for (int i = 0; i < N; ++i) {
      ++balance[chests_[i]];
    }
    bool again;
    do {
      again = false;
      for (int i = 0; i < N; ++i) {
        if (available_[i] > 0 && available_[i] >= balance[i]) {
          moveAll(i);
          again = true;
        }
      }
    } while (again);
  }

  bool checkBalance() const {
    int balance[N];
    copy(available_, available_ + N, balance);
    balance[0] += N;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        balance[j] += keys_[i][j];
      }
    }
    for (int i = 0; i < N; ++i) {
      if (--balance[chests_[i]] < 0) {
        return false;
      }
    }
    return true;
  }

  bool checkEnd() const {
    return *max_element(chests_, chests_ + N) == 0;
  }

  int findCycle() const {
    for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) {
      connect[i][j] =  keys_[i][chests_[j]];
    }
    for (int i = 0; i < N; ++i) {
      if (connect[i][i] && available_[chests_[i]])
         return i;
    }
    bool again;
    do {
      again = false;
      for (int i = 0; i < N; ++i) {
        if (!chests_[i]) continue;
        for (int j = 0; j < N; ++j) {
          if (!chests_[j]) continue;
          if (connect[i][j]) continue;
          for (int k = 0; k < N; ++k) {
            if (!chests_[k]) continue;
            if (!connect[i][k]) continue;
            if (!connect[k][j]) continue;
            connect[i][j] = true;
            if (i == j && available_[chests_[i]])
              return i;
            again = true;
            break;
          }
        }
      }
    } while (again);
    return 0;
  }

};

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    int k, n;
    scanf("%d%d", &k, &n);
    SmallTreasure treasure;
    while (k--) {
      int a;
      scanf("%d", &a);
      treasure.addAvailable(a);
    }
    for (int i = 0; i < n; ++i) {
      int ti, ki;
      scanf("%d%d", &ti, &ki);
      treasure.setChest(i, ti);
      while (ki--) {
        int a;
        scanf("%d", &a);
        treasure.addKey(i, a);
      }
    }
    int order[N];
    printf("Case #%d:", tc);
    if (treasure.findOrder(order)) {
      for (int i = 0; i < n; ++i)
        printf(" %d", order[i] + 1);
      printf("\n");
    } else {
      printf(" IMPOSSIBLE\n");
    }
  }
  return 0;
}
