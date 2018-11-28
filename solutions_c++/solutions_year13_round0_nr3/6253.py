# include <iostream>
# include <conio.h>
# include <fstream>
# include <stdlib.h>
# include <math.h>
using namespace std;
ifstream fr("input.txt");
ofstream fw("output.txt");
int solve();
int my_sq(int i);
int PerfectSquare(int n)
{
    int h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        int t = (int) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return 0;
}

int check_palindrome(int n)
{   int rev=0,cn=n;
    while(cn>0)
    {   rev=(rev*10)+(cn%10);
        cn=cn/10;
    }

    if(rev==n)
        return 1;
    else
        return 0;
}
int main()
{   int t;
    fr>>t;
    for (int i=0;i<t;i++)
        fw<<"Case #"<<i+1<<": "<<solve()<<endl;
    //getch();
}
int solve()
{   int a,b;
    fr>>a>>b;
    //cout <<a<<b;
    //getch();
    int count=0;
    for (int i=a;i<=b;i++)
    {   if((check_palindrome(i))&&(PerfectSquare(i)))
        {   if ((check_palindrome(my_sq(i)))==1)
            count++;
            //cout <<i<<" ";
        }
    }
    return count;
}
int my_sq(int i)
{   int a = 1;
    int b = i;

    while (((b-a) > 1)||((a-b)>1))
    {
        b = i / a;
        a = (a + b) / 2;
    }

    return a;
}















