#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define ll long long

int N = 32;
int J = 500;
int count_j = 0;
int number_of_bases = 9;

vector<int> number(N);

void Initialize_Number() {
  for (int i = 1; i < number.size()-1; ++i) {
    number[i] = 0;
  }
  number[0] = 1;
  number[number.size()-1] = 1;
}

void Print(vector<int> number_in) {
  for (int i = number_in.size()-1; i >= 0; --i)
    cout << number_in[i];
}

ll Number_In_Base(vector<int> number_in, int base) {

  ll number_in_base = 1;
  ll coeff = 1;

  for (int i = 1; i < number_in.size(); ++i) {

    coeff *= base;
    number_in_base += number_in[i] * coeff;

  }

  return number_in_base;

}

ll Get_Factor(ll number_in_base) {
  ll factor = -1;

  ll sqrt_of_number_in_base = int(sqrt(number_in_base));

  for (int i = 2; i <= sqrt_of_number_in_base; ++i) {
    if (number_in_base % i == 0) {
      factor = i;
      break;
    }
  }

  return factor;
}

vector<ll> Compute(vector<int> number_in) {
  vector<ll> number_in_bases(number_of_bases);
  vector<ll> factors;

  for (int i = 0; i < number_in_bases.size(); ++i) {
    number_in_bases[i] = Number_In_Base(number_in, i+2);
    ll factor = Get_Factor(number_in_bases[i]);
    factors.push_back(factor);
    if (factor < 0) break;
  }

  return factors;
}

void Solve(vector<int> number_current, int pos) {

  if ((pos == number.size()-1) || (count_j == J))
    return;

  vector<int> number_given(number_current);
  number_current[pos] = 1;

  vector<ll> factors = Compute(number_current);
  if (factors.size() == number_of_bases) {
    if ((factors.size() == 1 && factors[0] > 0) ||
        (factors.size() > 1 && factors.size() == number_of_bases)) {
      count_j++;
      Print(number_current);
      for (int i = 0; i < factors.size(); ++i) {
        cout << " " << factors[i];
      }
      cout << endl;
    }
  }

  Solve(number_current, pos+1);

  Solve(number_given, pos+1);

  return;

}

int main()
{
  Initialize_Number();

  cout << "Case #1:" << endl;
  Solve(number, 0);

  return 0;
}
