#include <iostream>
#include <vector>
#include <stdio.h>
#include <assert.h>

using namespace std;

typedef vector<vector<int> > lown_t;

bool cut_row(lown_t* lown, int row, int h, const lown_t& target_pattern);

bool cut_col(lown_t* lown, int col, int h, const lown_t& target_pattern);

void print_lown(const lown_t& lown)
{
  for(int i = 0; i < lown.size(); i++) {
    for(int j = 0; j < lown.size(); j++)
      printf("%d ",lown[i][j]);
    printf("\n");
  }
}

bool cut(lown_t* lown, const lown_t& target_pattern) {
  int nrow = target_pattern.size();
  assert(nrow > 0);
  int ncol = target_pattern[0].size();

  for(int i = 0; i < nrow; i++) {
    for(int j = 0; j < ncol; j++) {
      int h = (*lown)[i][j];
      int th = target_pattern[i][j];
      if (h > th) {
        if (!cut_row(lown,i,th,target_pattern) &&
            !cut_col(lown,j,th,target_pattern)) {
          return false;
        }
        assert(target_pattern[i][j] == (*lown)[i][j]);
      } else if (h < target_pattern[i][j]) {
        return false;
      }
    }
  }
  return true;
}

bool cut_row(lown_t* lown, int row, int h, const lown_t& target_pattern)
{
  assert(target_pattern.size() > 0);
  int ncol = target_pattern[0].size();
  
  // is it safe to cut ?
  for(int j = 0; j < ncol; j++)
    if (h < target_pattern[row][j])
      return false;
  
  for(int j = 0; j < ncol; j++) {
    if ((*lown)[row][j] > h) {
      (*lown)[row][j] = h;
    }
  }
  return true;
}

bool cut_col(lown_t* lown, int col, int h, const lown_t& target_pattern)
{
  int nrow = target_pattern.size();
  
  // is it safe to cut ?
  for(int i = 0; i < nrow; i++)
    if (h < target_pattern[i][col])
      return false;
  
  for(int i = 0; i < nrow; i++)
    if ((*lown)[i][col] > h)
      (*lown)[i][col] = h;
  return true;
}

int main()
{
  int n;

  cin >> n;
  for(int k = 1; k <= n; k++) {
    int nrow,ncol;
    cin >> nrow >> ncol;

    lown_t lown(nrow,vector<int>(ncol,100));

    lown_t target(nrow,vector<int>(ncol));
    for(int i = 0; i < nrow; i++) {
      for(int j = 0; j < ncol; j++) {
        int h;
        cin >> h;
        target[i][j] = h;
      }
    }

    printf("Case #%d: ",k);
    if (cut(&lown,target))
      printf("YES");
    else
      printf("NO");
    printf("\n");

  }
  return 0;
}
