#include <cstdio>
#include <cstring>

const int DRAW = 0;
const int O_WON = 1;
const int X_WON = 2;
const int NOT_COMPLETED = 3;

char game[4][6];

int status() {
   bool hasEmpty = false;
   /*
   for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
         printf("%c", game[i][j]);
      }

      printf("\n");
   }
   */

   // check rows
   for (int i = 0; i < 4; i++) {
      bool hasWinner = true;
      char first = game[i][0];
      if (first == 'T') first = game[i][1];

      for (int j = 0; j < 4; j++) {
         if (game[i][j] == '.') hasEmpty = true;

         if (game[i][j] != first && game[i][j] != 'T') {
            hasWinner = false;
            break;
         }
      }
      if (hasWinner && first != '.' ) {
         if (first == 'X') return X_WON;
         if (first == 'O') return O_WON;
      }
   }

   // check cols
   for (int j = 0; j < 4; j++) {
      bool hasWinner = true;
      char first = game[0][j];
      if (first == 'T') first = game[1][j];
      for (int i = 0; i < 4; i++) {
         if (game[i][j] != first && game[i][j] != 'T') {
            hasWinner = false;
            break;
         }
      }
      if (hasWinner && first != '.' ) {
         if (first == 'X') return X_WON;
         if (first == 'O') return O_WON;
      }
   }

   char first = game[0][0];
   if (first == 'T') first = game[1][1];
   if (first != '.') {
      if ((game[0][0] == 'T' || game[0][0] == first) &&
          (game[1][1] == 'T' || game[1][1] == first) &&
          (game[2][2] == 'T' || game[2][2] == first) &&
          (game[3][3] == 'T' || game[3][3] == first)) {
         if (first == 'X') return X_WON;
         if (first == 'O') return O_WON;
      }
   }

   first = game[0][3];
   if (first == 'T') first = game[1][2];
   if (first != '.') {
      if ((game[0][3] == 'T' || game[0][3] == first) &&
          (game[1][2] == 'T' || game[1][2] == first) &&
          (game[2][1] == 'T' || game[2][1] == first) &&
          (game[3][0] == 'T' || game[3][0] == first)) {
         if (first == 'X') return X_WON;
         if (first == 'O') return O_WON;
      }
   }

   if (hasEmpty) {
      return NOT_COMPLETED;
   } else {
      return DRAW;
   }

}

int main() {
   int t;
   scanf("%d", &t);

   for (int i = 1; i <= t; i++) {
      printf("Case #%d: ", i);
      for (int j = 0; j < 4; j++) {
         do {
            fgets(game[j], 5, stdin);
         } while (strlen(game[j]) < 4);
      }

      switch (status()) {
         case DRAW:
            printf("Draw\n");
            break;
         case O_WON:
            printf("O won\n");
            break;
         case X_WON:
            printf("X won\n");
            break;
         case NOT_COMPLETED:
            printf("Game has not completed\n");
            break;
         default:
            break;
      }
   }
   return 0;
}
