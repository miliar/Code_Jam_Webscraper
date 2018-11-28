/**
 * @file    p1.cc
 * @desc    Google Code Jam Problem A. Magic Trick
 * @vers    v1.0.0.140412
 * @date    Sat Apr 12 12:19:06 HKT 2014
 * @ref     Null
 * @author  Krime <krimelam@gmail.com>
 * @copy    (c)mindmesser,inc.
 */

/*
 * @details
 * Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!
 *
 * The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.
 *
 * Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?
 *
 * You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.
 *
 * Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).
 *
 * Solving this problem
 *
 * Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only 1 Small input. Once you have solved the Small input, you have finished solving this problem.
 *
 * Input
 *
 * The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.
 *
 * Output
 *
 * For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).
 *
 * If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.
 *
 * Limits
 *
 * 1 <= T <= 100.
 * 1 <= both answers <= 4.
 * Each number from 1 to 16 will appear exactly once in each arrangement.
 */
#include <iostream>
#include <vector>

#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

#define N 16

int main(void) {
  int cases=0;
  scanf("%d", &cases);
  int t=cases;
  int r1=0, r2=0;
  int card[N*2];
  int find=0;
  int finds=0;

  while (t--) {
    scanf("%d", &r1);
    for (int i=0;i<N;i++) scanf ("%d", &card[i]);
    scanf("%d", &r2);
    for (int i=0;i<N;i++) scanf ("%d", &card[i+N]);

    for (int i=0;i<4;i++)
      for (int j=0;j<4;j++) {
        //printf("%d %d\n", card[r1*4-4+i], card[N+r2*4-4+j]);
        if (card[r1*4-4+i]==card[N+r2*4-4+j]) {
          find=card[r1*4-4+i];
          finds++;
        }
      }
    printf("Case #%d: ", cases-t);
    if (find == 0) {
      puts("Volunteer cheated!");
    } else {
      if (finds > 1) {
        puts("Bad magician!");
      } else {
        printf("%d\n", find);
      }
    }
    /*
    if (cases-t==77) {
      for (int i=0;i<4;i++) {
        for (int j=0;j<4;j++)
          printf("%d ", card[i*4+j]);
        puts("");
      }
      printf("%d\n", r1);
      for (int i=0;i<4;i++) {
        for (int j=0;j<4;j++)
          printf("%d ", card[N+i*4+j]);
        puts("");
      }
      printf("%d\n", r2);
    }
    printf("%d\n", finds);
    */
    find = 0;
    finds = 0;
  }
  return 0;
}
