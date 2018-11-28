/**
 * Sort naomi's blocks smallest to largest
 * Sort ken's blocks largest to smallest
 * Deceitful war:
 *   going in order
 *   if naomi's first block is smaller than ken's first block,
 *   say it is smaller than ken's first but larger than next
 *   ken wins
 *   if naomi's first block is larger than ken's first block,
 *   naomi wins
 */

#include <iostream>
#include <queue>
#include <deque>
#include <list>
#include <functional>

using namespace std;

struct Naomi{
  priority_queue<double, vector<double>, greater<double> > blocks;

  Naomi(int N) {
    double value;
    for (int i = 0; i < N; ++i) {
      cin >> value;
      blocks.push(value);
    }
  }
};

struct Ken {
  list<double>* blocks_l2g;
  deque<double>* blocks_g2l;

  Ken(int N) {
    blocks_g2l = new deque<double>(N);
    for (int i = 0; i < N; ++i) {
      cin >> (*blocks_g2l)[i];
    }
    sort(blocks_g2l->begin(), blocks_g2l->end());
    blocks_l2g = new list<double>(blocks_g2l->begin(), blocks_g2l->end());
  }

  ~Ken() {
    delete blocks_l2g;
    delete blocks_g2l;
  }
};

int
fair_count(int N, Naomi& naomi, Ken& ken) {
  int wins = 0;
  priority_queue<double, vector<double>, greater<double> > naomi_blocks(naomi.blocks);
  double naomi_block, ken_block;

  for (int i = 0; i < N; ++i) {
    bool ken_wins = false;

    naomi_block = naomi_blocks.top();
    for (list<double>::const_iterator j = ken.blocks_l2g->begin(); j != ken.blocks_l2g->end(); ++j) {
      if (*j > naomi_block) {
	ken_wins = true;
	ken.blocks_l2g->erase(j);
	break;
      }
    }
    if (!ken_wins) {
      wins++;
    }
    naomi_blocks.pop();
  }
  return wins;
}

int
deceitful_count(int N, Naomi& naomi, Ken& ken) {
  int wins = 0;
  priority_queue<double, vector<double>, greater<double> > naomi_blocks(naomi.blocks);

  double naomi_block, ken_block;

  for (int i = 0; i < N; ++i) {
    naomi_block = naomi_blocks.top();
    ken_block = ken.blocks_g2l->back();
    if (naomi_block > ken_block) {
      wins++;
      ken.blocks_g2l->pop_back();
    } else if (naomi_block > ken.blocks_g2l->front()) {
      wins++;
      ken.blocks_g2l->pop_front();
    }
    naomi_blocks.pop();
  }
  return wins;
}

int
main(int argc, char** argv) {
  int T;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    cout << "Case #" << i << ": ";
    Naomi naomi(N);
    Ken ken(N);

    /*
    cout << endl;
    for (int j = 0; j < N; ++j) {
      cout << naomi.blocks.top() << ", " << ken.blocks.top() << endl;
      naomi.blocks.pop();
      ken.blocks.pop();
    }
    */
    cout << deceitful_count(N, naomi, ken) << " " << fair_count(N, naomi, ken) << endl;
  }
  return 0;
}
