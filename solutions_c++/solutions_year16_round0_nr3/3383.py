#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
//for every number, convert it from it's representation to base 10
vector<long> base10Rep(string inp)
{
  vector<long> reps;
  for(int i = 2; i <= 10; i++)
  {
    long n = std::stol(inp,0, i);
    reps.push_back(n);
  }
  return reps;
}
//find the divisor of our number, excluding 1 and the number
int divisor(long long number)
{
  for(int i = 2; i<number; i++)
  {
    if(number%i == 0)
    {
      return i;
    }
  }
  return 0;
}




bool isPrime (long num)
{
  //quick tests
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

int main(int argc, char const *argv[]) {
  ifstream in(argv[1]);
  ofstream out("output.txt");


  int t;
  in>>t;
  auto negate = [](char x){
    if(x == '1')
    {
      return '0';
    }
    return '1';
  };
  auto toString = [](vector<int> x)
  {
    string r;
    for(auto c: x)
    {
      r+=to_string(c);
    }
    return r;
  };

  auto anyPrime = [](vector<long> in)
  {
    bool any = false;
    for(auto x: in)
    {
      if(isPrime(x))
      {
        any = true;
        return any;
      }
    }
    return any;
  };
  for(int i = 1; i<=t; i++)
  {
    out<<"Case #"<<i<<":"<<endl;
    int n,j;
    in>>n>>j;
    vector<int> rep(n);
    for(int i = 0; i< rep.size(); i++)
    {
      if(i == 0 || i == rep.size()-1)
      {
        rep[i] = 1;
      }
      else
      {
          rep[i] = 0;
      }
    }
    int timesPer = 0;

    for(long x = 0; x < pow(2.0, n-2); x++)
    {
      //  for(int i = 0 ; i< rep.size();i++)
      //  {
          vector<long> z = base10Rep(toString(rep));
          //cout<<z.at(z.size()-1)<<endl;
          if( timesPer < j && !anyPrime(z) )
          {
            timesPer++;

            out<<z.at(z.size()-1)<<" ";
            for(auto v:z)
            {
              out<<divisor(v)<<" ";
            }
            out<<endl;
          }
        //}

        for(int j = rep.size()-2 ; j>=1 ; j--)
        {
            if(++rep[j]<=1)
                break;
            else
                rep[j]=0;
        }
  }

  }
  return 0;
}
