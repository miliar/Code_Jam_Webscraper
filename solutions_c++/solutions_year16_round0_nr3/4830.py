#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>     /* atoi */

using namespace std;

string jamcoin;

bool isprime(unsigned long long n){
    if (n == 2){
        return true;
    }
    if (n == 3){
        return true;
    }
    if ((n % 2)==0){
        return false;
    }
    if ((n % 3)==0){
        return false;
    }

    unsigned long long i = 5;
    unsigned long long w = 2;

    while ((i * i) <= n){
        if ((n % i) == 0){
            return false;
        }
        i += w;
        w = 6 - w;
    }
    return true;
}

unsigned long long nonTrivial(unsigned long long n){
  for (unsigned long long i = 2; i < n; i++) {
    if ((n%i) == 0){
      return i;
    }
  }
}

bool getNext(int digits){
  int start, end;
  start = 1;
  end = digits -2;
  for (int i = end; i >= start; i--) {
    if (jamcoin.at(i)=='1') {
      jamcoin.at(i)='0';
    } else {
      jamcoin.at(i)='1';
      return true;
    }
  }
  return false;
}

unsigned long long myPow(unsigned long long base, int power){
  unsigned long long result=1;
  for (int i = 0; i < power; i++) {
    result *= base;
  }
  return result;
}

unsigned long long getRealNum(int base, int digits){
  unsigned long long result =0;
  unsigned long long a;
  for (int i = digits-1; i >= 0; i--) {
    a = jamcoin.at(i)-48;

    result += a * myPow((unsigned long long)base, digits-(i+1));
    // cout << a<< "--" << result<<endl;
  }
  return result;
}

int main (int argc,char *argv[]){
  int digits, num_of_coins;
  unsigned long long rl[11];
  string dieretes;
  string line;
  ifstream myfile (argv[1]);

  if (myfile.is_open())
  {
    getline (myfile,line);
    int cases = stoi(line);
    dieretes = "";
    for (int i = 0; i < cases; i++) {
      cout<<"Case #" << i+1 <<":" << endl;

      //getline (myfile,line);
      myfile >> digits ;
      myfile >> num_of_coins ;
      //cout << digits << " = " << num_of_coins <<endl;

      jamcoin = "";
      for (int i = 0; i < digits; i++) {
        jamcoin += "0";
      }
      jamcoin.at(0)='1';
      jamcoin.at(digits-1)='1';
      //cout <<jamcoin<<endl;
      do  {
        for (int j = 2; j <= 10; j++) {
          rl[j] = getRealNum(j, digits);
          //cout << jamcoin<< " == " << rl[j] << " || " << isprime(rl[j]) << endl;
          if (isprime(rl[j])){
            dieretes = "";
            break;
          } else {
            dieretes += " "+to_string(nonTrivial(rl[j])) ;
            if (j==10){
              cout<<rl[j] << dieretes << endl;
              num_of_coins--;
              dieretes = "";
            }
          }
        }
      } while (getNext(digits)  && num_of_coins != 0);
      //cout<<"Case #" << i+1 <<": " << "ds" << endl;

    }

  }

  myfile.close();

}
