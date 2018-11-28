#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

string intToStr(unsigned long long n)
{
     string tmp;
     if(n < 0) {
          tmp = "-";
          n = -n;
     }
     if(n > 9)
          tmp += intToStr(n / 10);
     tmp += n % 10 + 48;
     return tmp;
}

int main()
{
    int n;
    cin >> n;
    for(int h=0; h<n;h++)
    {
        cout << "Case #" << (h+1) << ": ";

        int a, b;
        int licz=0;
        cin >> a >> b;
        string tmp, tmp1;
        double cc;
        unsigned long long c;
        for(int i=a;i<=b;i++)
        {
            tmp = intToStr(i);
            tmp1 = tmp;
            reverse(tmp1.begin(),tmp1.end());
            if(tmp == tmp1)
            {
                cc = pow(i, 0.5);
                c = cc;
                if(cc==c)
                {


                    tmp = intToStr(c);
                    tmp1 = tmp;
                    reverse(tmp1.begin(),tmp1.end());
                    if(tmp == tmp1)
                    {
                        licz++;
                    }
                }
            }


        }
        cout << licz << endl;
    }
    return 0;
}
