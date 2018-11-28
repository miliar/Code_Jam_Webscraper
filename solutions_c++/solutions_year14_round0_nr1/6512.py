// 12.04.2014
//

/*
Problem A. Magic Trick 
Problem
Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it! 
The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row.
Each card has a different number from 1 to 16 written on the side that is showing.
Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in. 
Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order.
Once again, he asks the volunteer which row her card is in.
With only the answers to these two questions, the magician then correctly determines which card the volunteer chose.
Amazing, right? 
You decide to write a program to help you understand the magician's technique.
The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions:
the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement.
The rows are numbered 1 to 4 from top to bottom. 
Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen
(the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated). 
Solving this problem
Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only 1 Small input.
Once you have solved the Small input, you have finished solving this problem. 
Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case starts with a line containing an integer: the answer to the first question.
The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space.
The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.
Output
For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1). 
If there is a single card the volunteer could have chosen, y should be the number on the card.
If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes.
If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes.
The text needs to be exactly right, so consider copying/pasting it from here. 
Limits
1 <= T <= 100.
1 <= both answers <= 4.
Each number from 1 to 16 will appear exactly once in each arrangement. 



Input 
  	
Output 
  
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!





Недавно вы пошли на магическое шоу. Вы были очень впечатлены один из трюков,
так что вы решили попробовать разобраться в том, в чем секрет!
Маг начинает устраивая 16 карт в квадрате сетки: 4 ряда карт, 4 карты в каждой строке.
Каждая карта имеет различные число от 1 до 16 написано на той стороне, которая показывает.
Далее, маг просит волонтера выбрать карту и сказать ему, в какой строке что-карты.
Наконец, маг организует 16 карточек в квадратную сетку снова, возможно, в другом порядке.
В очередной раз, он просит добровольцев, которые строки ее карты.
Только ответы на эти два вопроса, маг затем правильно определяет, какие карты добровольцев выбрали. Поразительно, правда?
Вы решили написать программу, чтобы помочь вам понять, что маг техники.
Программа будет предоставлена договоренностей двух карт, и добровольческих ответы на два вопроса:
номер строки, выбранные карты в первые договоренности, и номер строки, выбранной карточки во втором договоренности.
Строки пронумерованы от 1 до 4 сверху вниз.
Ваша программа должна определить, какие карты добровольцев выбрали, или если существует более одной карты волонтер может
выбрали (маг плохая работа); или если не существует никаких карт в соответствии с волонтерами ответы (волонтер обманули).
В решении этой проблемы
Как правило, Google Code Jam проблемы 1 маленький вход и 1 большой вклад. Эта проблема имеет только 1 маленький вход.
Как только вы решили малого входа, у вас есть готовые решения этой проблемы.
Вход
Первая строка входного файла содержит количество тестов, T.
T тестовых случаев следовать. Каждый тест начинается со строки, содержащей целое число: ответ на первый вопрос.
Следующие 4 строки представляют первые расположения карт: каждый из них содержит 4 целых числа, разделенных одним пробелом.
В следующей строке содержится ответ на второй вопрос, и следующие четыре строки содержат второй вариант, в таком же формате.
Выход
Для каждого теста вывести одну строку, содержащую "Case #x: y", где x-test case number (начиная с 1).
Если есть одна карта, доброволец мог бы выбрать, y должно быть число на карте.
Если существует несколько карт, доброволец может выбрали, y должно быть "плохой волшебник!", без кавычек.
Если нет карт в соответствии с волонтерами ответы, y должно быть "Добровольческой обманул!", без кавычек.
Текст должен быть абсолютно точной, так что рассмотреть возможность копирования/вставки из здесь.

*/

# include <stdio.h>
# include <math.h>
# include <string.h>

# define isDigit(x) ((x) >= 'A' && (x) <= 'Z')
# define isdigit(x) ((x) >= 'a' && (x) <= 'z')
# define convert(x) ( isdigit (x) ? (x)-'a'+'A' : (x)-'A'+'a' )



# define TRR_JUDGE



const int N = 4;

int n, m, k, i, j, t, r;
int a [N][N], b [N][N];

int main ()
{
# ifdef TRR_JUDGE
   freopen ("A.txt", "rt", stdin);
   freopen ("A.out", "wt", stdout);
# endif

   scanf ("%d\n", &t);

   for ( int i=1; i <= t; i++ )
   {
      scanf ("%d", &n);
      for ( int j=0, l; j < N; j++ )
         for ( l=0; l < N; l++ )
            scanf ("%d", &a [j][l]);
      scanf ("%d", &m);
      for ( int j=0, l; j < N; j++ )
         for ( l=0; l < N; l++ )
            scanf ("%d", &b [j][l]);

      n--, m--;
/*
# ifdef TRR_JUDGE
      printf ("%d\n", k);
# endif
*/

      k = 0;
      for ( int j=0, l; j < N; j++ )
         for ( l=0; l < N; l++ )
            if ( a [n][j] == b [m][l] )
               { k++, r = a [n][j]; break; }

//printf ("r=%d   ", r);

      printf ("Case #%d: ", i);
      if ( k == 1 )
         printf ("%d\n", r);
      else if ( k == 0 )
         printf ("Volunteer cheated!\n");
      else
         printf ("Bad magician!\n");
   }

   return 0;
}
