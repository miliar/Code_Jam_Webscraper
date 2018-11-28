#include<cstdio>

char board[6][6];

char is_complete(int x, int y) {
   char result = 'F';
   int count = 0;
   for (int i=0; i<4; i++) {
      if ((board[x][i] == board[x][y]) || (board[x][i] == 'T')) count++;
      if (board[x][i] != 'T') result = board[x][i];
   }
   if (count == 4) return result;
   count = 0;
   result = 'F';
   for (int i=0; i<4; i++) {
      if ((board[i][y] == board[x][y]) || (board[i][y] == 'T')) count++;
      if (board[i][y] != 'T') result = board[i][y];
   }
   if (count == 4) return result;
   if ((x == 0) && (y == 0)) {
      count = 0;
      result = 'F';
      for (int i=0; i<4; i++) {
         if ((board[x+i][y+i] == board[x][y]) || (board[x+i][y+i] == 'T')) count++;
         if (board[x+i][y+i] != 'T') result = board[x+i][y+i];
      }
      if (count == 4) return result;
   }
   if ((x == 0) && (y == 3)) {
      count = 0;
      result = 'F';
      for (int i=0; i<4; i++) {
         if ((board[x+i][y-i] == board[x][y]) || (board[x+i][y-i] == 'T')) count++;
         if (board[x+i][y-i] != 'T') result = board[x+i][y-i];
      }
      if (count == 4) return result;
   }
   
   return 'F';
}

int main() {
   int T;
   scanf("%d", &T);
   getchar();
   for (int cases=1; cases<=T; cases++) {
      bool not_complete = false;
      for (int i=0; i<4; i++) {
         for (int j=0; j<4; j++) {
            scanf("%c", &board[i][j]);
            if (board[i][j] == '.') not_complete = true;
         }
         getchar();
      }
      getchar();
     
      printf("Case #%d: ", cases);
      
      char flag = 'F';
      for (int i=0; (i<4) && (flag == 'F'); i++)
         for (int j=0; (j<4) && (flag == 'F'); j++)
            if ((board[i][j] != '.') && (board[i][j] != 'T'))
               flag = is_complete(i, j);
            
      if (flag == 'F') printf("%s\n", (not_complete) ? "Game has not completed" : "Draw");
      else printf("%c won\n", flag);
   }
   return 0;
}
