#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
using namespace std;
 
#define  rep(i,n)  for((i) = 0; (i) < (n); (i)++)
#define  rab(i,a,b)  for((i) = (a); (i) <= (b); (i)++)
#define all(v)    (v).begin(),(v).end()
#define  Fi(n)    rep(i,n)
#define  Fj(n)    rep(j,n)
#define  Fk(n)    rep(k,n)
#define  sz(v)    (v).size()

#define ROCK 1
#define SCISSOR 2
#define PAPER 3

struct Tree {
  int winner;
  Tree* left;
  Tree* right;
  string s;
  int level;
};

void delete_tree(Tree* t) {
  if (t->left != NULL) delete_tree(t->left);
  if (t->right != NULL) delete_tree(t->right);
  t->left = t->right = NULL;
  delete t;
}

char to_char(int piece) {
  switch(piece) {
    case ROCK: return 'R';
    case SCISSOR: return 'S';
    case PAPER: return 'P';
    default: return 0;
  }
}

void sort_tree(Tree* t) {
  if (t == NULL) return;

  sort_tree(t->left);
  sort_tree(t->right);

  string s1, s2;

  if (t->left == NULL && t->right == NULL) {
    t->s = "";
    t->s += to_char(t->winner);
  } else {
    if (t->left != NULL) s1 = t->left->s;
    else s1 = "";

    if (t->right != NULL) s2 = t->right->s;
    else s2 = "";

    string p1, p2;

    p1 = s1 + s2;
    p2 = s2 + s1;

    if (p1 < p2) {
      t->s = p1;
    } else {
      Tree* temp = t->left;
      t->left = t->right;
      t->right = temp;
      t->s = p2;
    }
  }
}

Tree* get_tree(int R, int P, int S, int win) {
  Tree* root = new Tree();
  root->left = root->right = NULL;
  root->winner = win;
  root->level = 0;

  if (win == ROCK) R--;
  if (win == SCISSOR) S--;
  if (win == PAPER) P--;

  vector <int> level;
  
  queue <Tree*> Q;

  Q.push(root);

  while (sz(Q) > 0) {
    //if (R == 0 && P == 0 && S == 0) break;
    Tree* t = Q.front();
    Q.pop();

    int next;

    if (t->winner == ROCK && S > 0) {
      next = SCISSOR;
      S--;
    } else if (t->winner == SCISSOR && P > 0) {
      next = PAPER;
      P--;
    } else if (t->winner == PAPER && R > 0) {
      next = ROCK;
      R--;
    } else {
      level.push_back(t->level);
      continue;
    }

    t->left = new Tree();
    t->right = new Tree();

    t->left->left = t->left->right = t->right->left = t->right->right = NULL;
    t->left->winner = t->winner;
    t->right->winner = next;
    t->left->level = t->right->level = t->level + 1;
    Q.push(t->left);
    Q.push(t->right);
  }
  if (R != 0 || S != 0 || P != 0) {
    delete_tree(root);
    return NULL;
  }
  sort(all(level));

  for (int i = 1; i < sz(level); i++) {
    if (level[i] != level[1]) {
      delete_tree(root);
      return NULL;
    }
  }

  if (level[sz(level) - 1] - level[0] > 1) {
    delete_tree(root);
    return NULL;
  }

  sort_tree(root);

  return root;
}

int main() {
	int T,cs;
  int N, R,P,S;

	scanf("%d",&T);

	rab(cs,1,T) {
    scanf("%d %d %d %d",&N, &R, &P, &S);
    vector <string> sol;
    Tree* t;

    if (R > 0) {
      t = get_tree(R, P, S, ROCK);
      if (t != NULL) {
        sol.push_back(t->s);
        delete_tree(t);
      }
    }

    if (S > 0) {
      t = get_tree(R, P, S, SCISSOR);
      if (t != NULL) {
        sol.push_back(t->s);
        delete_tree(t);
      }
    }

    if (P > 0) {
      t = get_tree(R, P, S, PAPER);
      if (t != NULL) {
        sol.push_back(t->s);
        delete_tree(t);
      }
    }

    sort(all(sol));
    
    if (sz(sol) > 0) {
      cout << "Case #" << cs << ": " << sol[0] << endl;
    } else {
      cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
    }
	}
} 
