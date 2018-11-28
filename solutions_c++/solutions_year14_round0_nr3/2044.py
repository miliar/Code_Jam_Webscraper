#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cassert>

using namespace std;

/*
 * 2 = * (mine)
 * 1 = c
 * 0 = .
 */

int *transpose(int *board, int r, int c);
int *copy(int *board, int r, int c);
int index_of(int i, int j, int r, int c);
void fprint_board(int *board, int r, int c);
bool solve_other(int *board, int r, int c, int m);
bool is_1click(int *board, int r, int c, int m);
int click(int *board, int idx, int r, int c);
void coord_of(int idx, int r, int c, int *i, int *j);

int *transpose(int *board, int r, int c)
{
  int i, j;
  int *new_board = new int[r * c];
  for (i = 0; i < r; i++)
  {
    for (j = 0; j < c; j++)
    {
      new_board[index_of(j, i, c, r)] = board[index_of(i, j, r, c)];
    }
  }
  return new_board;
}

int *copy(int *board, int r, int c)
{
  int *new_board = new int[r * c];
  int i, j;
  for (i = 0; i < r; i++)
    for (j = 0; j < c; j++)
      new_board[index_of(i, j, r, c)] = board[index_of(i, j, r, c)];
  return new_board;
}

int index_of(int i, int j, int r, int c)
{
  if (i >= r || j >= c)
  {
    fprintf(stderr, "oops\n");
    exit(1);
  }
  return i * c + j;
}

// Returns the coordinates given idx. Writes coordinates to i, j.
void coord_of(int idx, int r, int c, int *i, int *j)
{
  *i = idx / c;
  *j = idx % c;
}

void fprint_board(FILE *fout, int *board, int r, int c)
{
  int i, j, tmp;
  for (i = 0; i < r; i++)
  {
    for (j = 0; j < c; j++)
    {
      tmp = board[index_of(i, j, r, c)];
      switch (tmp)
      {
        case 0:
          fprintf(fout, ".");
          break;
        case 1:
          fprintf(fout, "c");
          break;
        case 2:
          fprintf(fout, "*");
          break;
      }
    }
    fprintf(fout, "\n");
  }
}

void solve(int r, int c, int m, FILE *fout)
{
  int i, j, k;
  int *board = new int[r * c];
  int *trans;
  int tmp_r, tmp_c;

  if (m == 0)
  {
    // No mines.
    // c...
    // ....
    // ....
    board[0] = 1;
    for (k = 1; k < r * c; k++)
      board[k] = 0;
    fprint_board(fout, board, r, c);
  }
  else if (r == 1)
  {
    // 1 row.
    // ***..c
    for (k = 0; k < m; k++)
      board[k] = 2;
    for (; k < c - 1; k++)
      board[k] = 0;
    board[c - 1] = 1;
    fprint_board(fout, board, r, c);
  }
  else if (c == 1)
  {
    // 1 column.
    // *
    // *
    // .
    // .
    // c
    tmp_r = c;
    tmp_c = r;
    for (k = 0; k < m; k++)
      board[k] = 2;
    for (; k < tmp_c - 1; k++)
      board[k] = 0;
    board[tmp_c - 1] = 1;

    trans = transpose(board, tmp_r, tmp_c);
    fprint_board(fout, trans, r, c);
    //delete[] trans;
  }
  else if (m == r * c - 1)
  {
    // All but one square is a mine.
    // c***
    // ****
    // ****
    for (k = 1; k < r * c; k++)
      board[k] = 2;
    board[0] = 1;
    fprint_board(fout, board, r, c);
  }
  else if (m == r * c - 2)
  {
    // This is never possible (except in 1-column case, which was
    // already covered).
    // **
    // .c
    // doesn't work.
    fprintf(fout, "Impossible\n");
  }
  else if (m % c != c - 1 && r * c - m >= 2 * c)
  {
    // Something like this
    // *****
    // *****
    // ***..
    // .....
    // ....c
    for (k = 0; k < m; k++)
      board[k] = 2;
    for (; k < r * c - 1; k++)
      board[k] = 0;
    board[r * c - 1] = 1;
    fprint_board(fout, board, r, c);
  }
  else if (m % r != r - 1 && r * c - m >= 2 * r)
  {
    // ****..
    // ****..
    // ****..
    // ***...
    // ***..c
    tmp_r = c;
    tmp_c = r;
    for (k = 0; k < m; k++)
      board[k] = 2;
    for (; k < r * c - 1; k++)
      board[k] = 0;
    board[r * c - 1] = 1;
    trans = transpose(board, tmp_r, tmp_c);
    fprint_board(fout, trans, r, c);
    //delete[] trans;
  }
  else if (m > r * c - 2 * c && (m - (r * c - 2 * c)) % 2 == 0)
  {
    // *****
    // *****
    // **...
    // **...
    for (k = 0; k < r * c - 2 * c; k++)
      board[k] = 2;
    int m_left = m - (r * c - 2 * c);
    for (i = r - 2; i < r; i++)
    {
      for (j = 0; j < c; j++)
      {
        if (j < m_left / 2)
          board[index_of(i, j, r, c)] = 2;
        else
          board[index_of(i, j, r, c)] = 0;
      }
    }
    board[r * c - 1] = 1;
    fprint_board(fout, board, r, c);
  }
  else if (m > r * c - 2 * r && (m - (r * c - 2 * r)) % 2 == 0)
  {
    // *******
    // *******
    // *****..
    // *****..
    tmp_r = c;
    tmp_c = r;
    for (k = 0; k < tmp_r * tmp_c - 2 * tmp_c; k++)
      board[k] = 2;
    int m_left = m - (tmp_r * tmp_c - 2 * tmp_c);
    for (i = tmp_r - 2; i < tmp_r; i++)
    {
      for (j = 0; j < tmp_c; j++)
      {
        if (j < m_left / 2)
          board[index_of(i, j, tmp_r, tmp_c)] = 2;
        else
          board[index_of(i, j, tmp_r, tmp_c)] = 0;
      }
    }
    board[tmp_r * tmp_c - 1] = 1;
    trans = transpose(board, tmp_r, tmp_c);
    fprint_board(fout, trans, r, c);
    //delete[] trans;
  }
  else
  {
    if (solve_other(board, r, c, m))
      fprint_board(fout, board, r, c);
    else if (solve_other(board, c, r, m))
      fprint_board(fout, board, c, r);
    else
      fprintf(fout, "Impossible\n");
  }
  //delete[] board;
}

// Solve other cases. Writes result to board.
bool solve_other(int *board, int r, int c, int m)
{
  int k;
  int *start, *end;
  for (k = 0; k < m; k++)
    board[k] = 2;
  for (; k < r * c; k++)
    board[k] = 0;
  if (m <= r * c - 2 * c)
  {
    // *****
    // ****.
    // .....
    // .....
    // doesn't work
    start = board + m - 1;
    end = board + r * c;
  }
  else
  {
    start = board + r * c - 3 * c - 1;
    end = board + r * c;
  }
  start = board;
  end = board + r * c;
  sort(start, end);
  do {
    if (is_1click(board, r, c, m))
      return true;
  } while (next_permutation(start, end));
  return false;
}

bool is_1click(int *board, int r, int c, int m)
{
  int i, j;
  int tmp_i, tmp_j;
  int idx, idx2;
  int *tmp_board = new int[r * c];
  assert(tmp_board);
  // Reset the board. Mines are -1.
  for (idx = 0; idx < r * c; idx++)
  {
    if (board[idx] == 2)
      tmp_board[idx] = -1;
    else
      tmp_board[idx] = 0;
  }
  for (idx = 0; idx < r * c; idx++)
  {
    if (tmp_board[idx] == -1)
      continue;
    coord_of(idx, r, c, &i, &j);
    for (tmp_i = i - 1; tmp_i <= i + 1; tmp_i++)
    {
      for (tmp_j = j - 1; tmp_j <= j + 1; tmp_j++)
      {
        if (tmp_i < 0 || tmp_i >= r || tmp_j < 0 || tmp_j >= c)
          continue;
        idx2 = index_of(tmp_i, tmp_j, r, c);
        // Count mines.
        if (tmp_board[idx2] == -1)
          tmp_board[idx]++;
      }
    }
  }
  for (idx = 0; idx < r * c; idx++)
  {
    if (tmp_board[idx] == -1)
      continue;
    // Try clicking here.
    int result = click(tmp_board, idx, r, c);
    if (result == r * c - m)
    {
      // Remake the board properly.
      for (idx2 = 0; idx2 < r * c; idx2++)
      {
        if (tmp_board[idx2] == -1)
          board[idx2] = 2;
        else if (idx2 == idx)
          // Click here
          board[idx2] = 1;
        else
          board[idx2] = 0;
      }
      //delete[] tmp_board;
      return true;
    }
  }
  //delete[] tmp_board;
  return false;
}

struct node
{
  node *next;
  int data;
};

node *create_node(int data)
{
  node *n = (node *) malloc(sizeof(node));
  n->next = NULL;
  n->data = data;
  return n;
}

node *push(node *list, int data)
{
  node *n = create_node(data);
  n->next = list;
  return n;
}

node *pop(node *list)
{
  node *n = list->next;
  return n;
}

// Returns number of squares revealed when mine is clicked. -1 = mine
int click(int *board, int idx, int r, int c)
{
  int i, j, tmp, tmp_i, tmp_j, idx2;
  int found = 0;
  int *visited = (int *)malloc(r * c * sizeof(int));
  node *to_visit = NULL;

  for (i = 0; i < r * c; i++)
    visited[i] = 0;

  to_visit = push(to_visit, idx);
  while (to_visit != NULL)
  {
    tmp = to_visit->data;
    to_visit = pop(to_visit);
    if (board[tmp] == -1)
      continue;
    if (visited[tmp])
      continue;
    visited[tmp] = 1;
    found++;
    if (board[tmp] == 0)
    {
      coord_of(tmp, r, c, &i, &j);
      for (tmp_i = i - 1; tmp_i <= i + 1; tmp_i++)
      {
        for (tmp_j = j - 1; tmp_j <= j + 1; tmp_j++)
        {
          if (tmp_i < 0 || tmp_i >= r || tmp_j < 0 || tmp_j >= c)
            continue;
          idx2 = index_of(tmp_i, tmp_j, r, c);
          if (idx2 == tmp)
            continue;
          to_visit = push(to_visit, idx2);
        }
      }
    }
  }
  return found;
}

int main()
{
  FILE *fin, *fout;
  fin = fopen("input.txt", "r");
  fout = fopen("output.txt", "w");

  int T, n;
  int r, c, m;

  fscanf(fin, "%d\n", &T);
  for (n = 1; n <= T; n++)
  {
    fscanf(fin, "%d %d %d\n", &r, &c, &m);
    fprintf(fout, "Case #%d:\n", n);
    solve(r, c, m, fout);
  }
  fclose(fin);
  fclose(fout);
  return 0;
}
