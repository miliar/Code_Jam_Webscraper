// 12.04.2014
//

/*
Problem B. Cookie Clicker Alpha 
Small input
8 points	You may try multiple times, with penalties for wrong submissions.
Large input
11 points	You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Introduction
Cookie Clicker is a Javascript game by Orteil, where players click on a picture of a giant cookie.
Clicking on the giant cookie gives them cookies. They can spend those cookies to buy buildings.
Those buildings help them get even more cookies. Like this problem, the game is very cookie-focused.
This problem has a similar idea, but it does not assume you have played Cookie Clicker.
Please don't go play it now: it might be a long time before you come back. 
Problem
In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second,
by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm.
Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second. 
Once you have X cookies that you haven't spent on farms, you win!
Figure out how long it will take you to win if you use the best possible strategy. 
Example
Suppose C=500.0, F=4.0 and X=2000.0. Here's how the best possible strategy plays out: 
1.	You start with 0 cookies, but producing 2 cookies per second.
2.	After 250 seconds, you will have C=500 cookies and can buy a farm that produces F=4 cookies per second.
3.	After buying the farm, you have 0 cookies, and your total cookie production is 6 cookies per second.
4.	The next farm will cost 500 cookies, which you can buy after about 83.3333333 seconds.
5.	After buying your second farm, you have 0 cookies, and your total cookie production is 10 cookies per second.
6.	Another farm will cost 500 cookies, while you can buy after 50 seconds.
7.	After buying your third farm, you have 0 cookies, and your total cookie production is 14 cookies per second.
8.	Another farm would cost 500 cookies, but it actually makes sense not to buy it:
   instead you can just wait until you have X=2000 cookies, which takes about 142.8571429 seconds.
Total time: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 seconds. 
Notice that you get cookies continuously: so 0.1 seconds after the game starts you'll have 0.2 cookies,
and PI seconds after the game starts you'll have 2*PI cookies. 
Input
The first line of the input gives the number of test cases, T. T lines follow.
Each line contains three space-separated real-valued numbers:
     C, F and X, whose meanings are described earlier in the problem statement. 
C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits.
There will be no leading zeroes. 
Output
For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and
y is the minimum number of seconds it takes before you can have X delicious cookies. 
We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct
if it is close enough to the correct number: within an absolute or relative error of 10^-6.
See the FAQ for an explanation of what that means, and what formats of real numbers we accept. 
Limits
1 <= T <= 100. 
Small dataset
1 <= C <= 500.
1 <= F <= 4.
1 <= X <= 2000.
Large dataset
1 <= C <= 10000.
1 <= F <= 100.
1 <= X <= 100000.
Sample

Input 
  	
Output 
  
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

Note
Cookie Clicker was created by Orteil. Orteil does not endorse and has no involvement with Google Code Jam. 




Введение

Cookie Clicker Javascript игры Orteil, где игроки нажмите на изображение гигантского cookie.
Нажав на гигантских cookie дает им печенье. Они могут потратить эти файлы cookie, чтобы купить зданий.
Эти здания помочь им получить даже несколько файлов cookie. Как эту проблему, игра очень cookie направленность.
Эта проблема была подобная мысль, но она не предполагаем, что вы сыграли Cookie Clicker.
Пожалуйста, не уходи играть сейчас: это может быть долгое время, прежде чем вы вернетесь.
Проблема

В этой задаче вам начать с " 0 " cookies". Вы получаете файлы cookie в размере 2 cookies в секунду, нажав на гигантском cookie.
В любое время вы имеете, по крайней мере, C cookies, вы можете купить cookie фермы.
Каждый раз, когда вы покупаете cookie фермы, стоит вам C cookies и дает вам дополнительные F файлы cookie в секунду.

После X файлов cookie, которые Вы не потратили на фермах, вы выигрываете!
Выяснить, сколько времени понадобится вам, чтобы победить, если вам использовать наилучшие стратегии.
Пример

Предположим, что C=500,0 млн тенге, F=4.0 и X=2000.0. Вот как лучшая возможная стратегия играет:

Вы начинаете с 0 cookies, но и производить 2 cookies в секунду.
После 250 секунд, Вы будете иметь C=500 cookies и можете купить ферму, которая производит F=4 cookies в секунду.
После покупки фермы, у вас есть 0 cookies, и ваша общая cookie производства 6 cookies в секунду.
Следующая ферма будет стоить 500 файлов cookie, которые можно купить примерно через 83.3333333 секунд.
После покупки второй ферме, вы имеете 0 cookies, и ваша общая cookie производства составляет 10 файлы cookie в секунду.
Еще одна ферма будет стоить 500 файлы cookie, в то время как вы можете купить через 50 секунд.
После покупки третьей ферме, вы имеете 0 cookies, и ваша общая cookie производство 14 файлы cookie в секунду.
Еще одна ферма будет стоить 500 cookies, но это на самом деле не имеет смысла покупать:
    вместо этого вы можете просто подождать, пока у вас есть X=2000 cookies, которая занимает около 142.8571429 секунд.

Общее время: 250 + 83.3333333 + 50 + 142.8571429 = 526.1904762 секунд.

Обратите внимание, что вы получите куки: 0,1 секунды после начала игры вы будете иметь 0.2 печенье,
- и p секунд после начала игры вы будете иметь 2*PI файлы cookie.
Вход
Первая строка входного файла содержит количество тестов, т. T строк.
Каждая строка содержит через пробел три вещественных числа:
       C, F и X, значение которых было описано ранее в постановке проблемы.
C, F и X каждый будет состоять, как минимум, 1 цифра, за 1 десятичной точки следуют от 1 до 5 цифр.
Там будет без лидирующих нулей.
Выход
Для каждого теста вывести одну строку, содержащую "Case #x: y", где x-test case number (начиная с 1) и
y-это минимальное количество секунд, которое потребуется, прежде чем вы сможете иметь X вкусного печенья.
Мы рекомендуем выводить y до 7 знаков после запятой, но это и не требуется. y будет считаться правильным,
если он находится достаточно близко к правильному номер: в абсолютной или относительной погрешности 10^-6.
См. часто задаваемые вопросы для объяснения того, что это означает, и какие форматы реальные цифры, которые мы принимаем.


*/

# include <stdio.h>
# include <math.h>
# include <string.h>

# define isDigit(x) ((x) >= 'A' && (x) <= 'Z')
# define isdigit(x) ((x) >= 'a' && (x) <= 'z')
# define convert(x) ( isdigit (x) ? (x)-'a'+'A' : (x)-'A'+'a' )



# define TRR_JUDGE



const double eps = 10-8;

int n, m, k, i, j, t, r;
double c, f, x;
double mint, curt, sumt, v, p2, x2;


int main ()
{
# ifdef TRR_JUDGE
   freopen ("B.txt", "rt", stdin);
   freopen ("B.out", "wt", stdout);
# endif

   scanf ("%d\n", &t);

   for ( int i=1; i <= t; i++ )
   {
      scanf ("%lf %lf %lf", &c, &f, &x);

/*
# ifdef TRR_JUDGE
      printf ("%0.7lf %0.7lf %0.7lf\n", c, f, x);
# endif
*/

      if ( c > x )
         mint = x*0.5;
      else
      {
         mint = x*0.5; sumt = 0.0; v = 2.0; curt = 0.0;
         for ( int k=0; k < 1000000/*mint > curt*/; k++ )
         {
            sumt += c/v;
            v += f;
            curt = sumt + x/v;
            if ( curt < mint )
               mint = curt;
         }
      }

//printf ("r=%d   ", r);

      printf ("Case #%d: %0.7lf\n", i, mint);
   }

   return 0;
}
