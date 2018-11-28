// Includes, standard.
#include <assert.h>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

enum board_symbol {
  sym_x = 'X',
  sym_o = 'O',
  sym_t = 'T',
  sym_d = '.'
};

enum game_state {
  x_won,
  o_won,
  draw,
  not_finished,
};

typedef board_symbol game_board[16];

void
print_board(game_board board) {
  for (size_t row = 0; row < 4; ++row) {
    for (size_t col = 0; col < 4; ++col) {
      printf("%c", board[row * 4 + col]);
    }
    printf("\n");
  }
}

void
read_board(game_board board) {
  for (size_t i = 0; i < 4; ++i) {
    std::string line;
    std::cin >> line;
    assert(line.size() == 4);

    for (size_t j = 0; j < 4; ++j) {
      board[i * 4 + j] = (board_symbol) line[j];
    }
  }
}

game_state
get_game_state(game_board board) {
  size_t nb_x = 0;
  size_t nb_d = 0;
  size_t nb_o = 0;
  size_t nb_t = 0;

  // Check lines.
  for (size_t row = 0; row < 4; ++row) {
    size_t nb_x = 0;
    size_t nb_d = 0;
    size_t nb_o = 0;
    size_t nb_t = 0;

    for (size_t col = 0; col < 4; ++col) {
      switch (board[row * 4 + col]) {
      case sym_d: nb_d++; break;
      case sym_x: nb_x++; break;
      case sym_t: nb_t++; break;
      case sym_o: nb_o++; break;
      }

      if ((nb_x + nb_t) == 4) return x_won;
      if ((nb_o + nb_t) == 4) return o_won;
    }
  }

  // Check colums.
  for (size_t col = 0; col < 4; ++col) {
    size_t nb_x = 0;
    size_t nb_d = 0;
    size_t nb_o = 0;
    size_t nb_t = 0;

    for (size_t row = 0; row < 4; ++row) {
      switch (board[row * 4 + col]) {
      case sym_d: nb_d++; break;
      case sym_x: nb_x++; break;
      case sym_t: nb_t++; break;
      case sym_o: nb_o++; break;
      }

      if ((nb_x + nb_t) == 4) return x_won;
      if ((nb_o + nb_t) == 4) return o_won;
    }
  }

  nb_x = 0;
  nb_d = 0;
  nb_o = 0;
  nb_t = 0;
  for (size_t i = 0; i < 4; ++i) {
    switch (board[5 * i]) {
    case sym_d: nb_d++; break;
    case sym_x: nb_x++; break;
    case sym_t: nb_t++; break;
    case sym_o: nb_o++; break;
    default:
      assert(false);
    }

    if ((nb_x + nb_t) == 4) return x_won;
    if ((nb_o + nb_t) == 4) return o_won;
  }

  nb_x = 0;
  nb_d = 0;
  nb_o = 0;
  nb_t = 0;
  for (size_t i = 0; i < 4; ++i) {
    switch (board[3 * (i + 1)]) {
    case sym_d: nb_d++; break;
    case sym_x: nb_x++; break;
    case sym_t: nb_t++; break;
    case sym_o: nb_o++; break;
    }

    if ((nb_x + nb_t) == 4) return x_won;
    if ((nb_o + nb_t) == 4) return o_won;
  }

  // Check if the game is complete.
  for (size_t i = 0; i < 4*4; ++i) {
    if (board[i] == sym_d) {
      return not_finished;
    }
  }

  return draw;
}

int
main(void) {
  game_board current_board = { sym_d };
  game_state current_state = { not_finished };

  size_t nb_tc = 0;
  std::cin >> nb_tc;

  for (size_t i = 0; i < nb_tc; ++i) {
    read_board(current_board);
    current_state = get_game_state(current_board);

    printf("Case #%d: ", (int) i + 1);
    switch (current_state) {
    case x_won: printf("X won\n"); break;
    case o_won: printf("O won\n"); break;
    case draw:  printf("Draw\n"); break;
    default:
      printf("Game has not completed\n");
    }
  }

  return EXIT_SUCCESS;
}

