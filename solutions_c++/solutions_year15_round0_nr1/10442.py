#include <fstream>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

  int t,i,smax,ctr,j;
in>>t;
for ( i = 1; i <= t; ++i)
 {
   in>>smax;
   	char s[smax+2];
    int sum[smax+2];
       	in>>s;

   	sum[0]=s[0] - '0';
   	ctr=0;

  for (j=1; j <= smax  ; ++j)
  {

          if (sum[j - 1] >= j)
          {
          }
          else
          {
              ctr+=j-sum[j - 1];
              sum[j - 1] = j;
          }

            sum[j] = sum[j-1] + s[j] - '0';
  }
  out<<"Case #"<<i<<":"<<" "<<ctr<<endl;
}
 return 0;
}

