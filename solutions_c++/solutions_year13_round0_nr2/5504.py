#include <iostream>
int Ggrid[100][100];
void print (int grid[100][100], int N, int M) {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        std::cout << grid[i][j] << " ";
      }
      std::cout << "\n";
    }
    std::cout << "\n";
}
bool solve(int grid[100][100], int cutlist[200], bool *hlist, int k, int N, int M) {
  while( k >=1 && !hlist[k])
    k--;
  if (k < 1)
    return true;
  bool found = false;
  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      if(grid[i][j] == k) {
        found = true;
        bool rowok = true;
        bool colok = true;
        for(int x=0; x<M; x++) {
          if (grid[i][x] == 0 && k != Ggrid[i][x] )
            rowok = false;
        }
        for (int x=0; x<N; x++) {
          if(grid[x][j] == 0 && k != Ggrid[x][j])
            colok = false;
        }
        int tgrid[100][100];
        int tcutlist[200];
        for (int x=0; x < N; x++)
          for(int y=0; y < M; y++)
            tgrid[x][y] = grid[x][y];
        //std::cout << k << "\n";
        //print(tgrid, N, M);

        for (int x=0; x < N; x++)
          tcutlist[x] = cutlist[x];
        for(int x=0; x < M; x++)
          tcutlist[100+x] = cutlist[100+x];

        if(cutlist[i] == 1 && rowok) { //row cut
          for(int x=0; x<M; x++) {
            if(tgrid[i][x] == k)
              tgrid[i][x] = 0;
          }
          tcutlist[i] = 0;
          //print(tgrid, N, M);
          rowok = solve(tgrid, tcutlist, hlist, k, N, M);
        } 

        for (int x=0; x < N; x++)
          for(int y=0; y < M; y++)
            tgrid[x][y] = grid[x][y];
        for (int x=0; x < N; x++)
          tcutlist[x] = cutlist[x];
        for(int x=0; x < M; x++)
          tcutlist[100+x] = cutlist[100+x];
        if (cutlist[100+j] == 1 && colok) {//col cut
          for (int x=0; x<N; x++) {
            if(tgrid[x][j] == k)
              tgrid[x][j] = 0;
          }
          cutlist[100+j] = 0;
          //print(tgrid, N, M);
          colok = solve(tgrid, tcutlist, hlist, k, N, M);
        } 
        return colok | rowok; //can not cut
      }
    }
  }
  if (found == false) {
    k--;
    return solve(grid, cutlist, hlist, k, N, M);
  }
}
int main () {
  int num, iCase, N, M;
  int tgrid[100][100];
  bool hlist[101];
  int hcount;
  int cutlist[200];
  std::cin >> num;
  std::cout << num << "\n";
  for (iCase = 1; iCase <= num; iCase ++) {
    std::cin >> N >> M;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        std::cin >> Ggrid[i][j];
        hlist[Ggrid[i][j]] = true;
      }
    }
    hcount = 0;
    for (int i=0; i<100; i++)
      if (hlist[i])
        hcount += 1;
    if (hcount > N + M) {
      std::cout << "Case #" << iCase << ": " << "NO" << "count\n";
      continue;
    }
    for(int i=0; i<N; i++)
      cutlist[i] = 1;
    for(int i=0; i<M; i++)
      cutlist[100+i] = 1;
    //print(Ggrid, N, M);
    if (solve(Ggrid, cutlist, hlist, 100, N, M))
      std::cout << "Case #" << iCase << ": YES" << "\n";
    else
      std::cout << "Case #" << iCase << ": NO" << "\n";
    /*
    */

  }
  return 0;
}
