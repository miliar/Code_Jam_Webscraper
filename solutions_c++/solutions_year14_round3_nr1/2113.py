#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

bool power_of_two(int a)
{
    if(a%2 != 0) return false;
    else if(a == 2) return true;
    else return power_of_two(a/2);
}

int pgcd(double a, double b)
{
    if(a != floor(a) || b != floor(b))
        return 1;
    if(a < 1 || b <1)
        return 1;

    while(a != b)
        if(a > b)
            a -= b;
        else
            b -= a;
    return a;
}

vector<long> split(string str, string delim)
{
      unsigned start = 0;
      unsigned end;
      vector<long> v;
      string str_;

      while( (end = str.find(delim, start)) != string::npos )
      {
          str_ = str.substr(start, end-start);
            v.push_back(strtol(str_.c_str(), NULL, 0));
            start = end + delim.length();
      }
      str_ = str.substr(start);
      v.push_back(strtol(str_.c_str(), NULL, 0));
      return v;
}

int main()
{
    ifstream file("fileA.txt");
    ofstream result_file("resultA.txt");




	int numCase;
	file >> numCase;
	int i, j, k, p ,q, pgcd_pq;

	double q_ = 0;



	for (i = 0; i < numCase; i++)
	{
    string  quotient;
        file >> quotient;
        p = split(quotient, "/")[0];
        q = split(quotient, "/")[1];

        pgcd_pq = pgcd(p,q);
        if(pgcd_pq != 1)
        {
            p = p/pgcd_pq;
            q = q/pgcd_pq;
        }

        q_ = q;
        k = 0, j= 0;

        double p_= p;
        int gcd_ = 1, gcd2_ = 1;


        if(power_of_two(q))
        {
            if(log(q)/log(2) < 40)
            {


                while(p_ < q_/2)
                {
                    k++;
                    p_=p_*2;
                    gcd_ = pgcd(p_, q_);
                    p_ = p_ /gcd_;
                    q_ = q_ /gcd_;
                }

            }
            else
                k=41;
        }
        else
            k=41;

        if(k == 41)
        {
            cout << "Case #" << (i+1) << ": "<< "impossible" << endl;
		result_file << "Case #" << (i+1) << ": " << "impossible"  << endl;
        }
        else
         {
             k++;
            cout << "Case #" << (i+1) << ": "<< k<< endl;
            result_file << "Case #" << (i+1) << ": " << k << endl;
        }


	}
	return 0;
}
