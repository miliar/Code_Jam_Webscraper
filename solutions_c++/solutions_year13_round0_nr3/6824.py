#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
bool pal(unsigned int n)
{
    unsigned int temp = n, reverse=0;
   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }
   if ( n == reverse )
      return true;
   else
      return false;
}

int main()
{
    ofstream of("fairandsquare.txt");
    unsigned int t, m, n, a, b, j, p, count;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>m>>n;
        a = sqrt(m);
        b = sqrt(n)+1;
        count=0;
        for(j=a; j<b; j++)
        {
            p = j*j;
            if(pal(j) && pal(p) && p>=m && p<=n)
                count++;
        }
        of<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
