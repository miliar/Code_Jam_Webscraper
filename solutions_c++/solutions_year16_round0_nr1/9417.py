#include <iostream>
#include <string>     // std::string, std::to_string
#include <cstdio>
#include <cstring>


using namespace std;



string calc_sheep (long long int N)
{
    long long int M = N;
    long int i = 0;
    bool checked_digit [10] = {false};
    bool AND = false;
    long long int ans = 0;
    char *check_string = (char*)malloc (100);
    if (N == 0) return string("INSOMNIA");

    for (i=1; i<100000; i++)
    {
        M = N * i;
        sprintf (check_string, "%lld", M);
        for (unsigned int l=0; l<strlen(check_string); l++)
          checked_digit[ check_string[l] - '0' ] = true;

        AND = true;
        for (int l=0; l<10 ; l++)
          AND = AND and checked_digit[l];

        if (AND)
        {
            ans = M;
            break;
        }
    }

    return std::to_string ( ans  );
}


int main ()
{

  int CaseCount;
  cin >> CaseCount;

  for (int cc=0; cc<CaseCount ; cc++)
  {
    int number;
    cin >> number;


    cout << "Case #" << (cc+1) << ": " ;
    cout << calc_sheep (number);

    cout << endl;
  }



  return 0;
}
