#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

typedef vector<long> LongVector;

ofstream outfile;
//ofstream outfile2;


bool isPrime(long long number,long long& divisor)
{
    divisor = number;
    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) { divisor = 2; return false;}
    for(long long i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) { divisor = i; return false;}
    }
    return true;

}


long long power(long long value, long powerV) {
	long long result = 1;
    long i;
	for (i = 0; i < powerV; ++i) {
		result *= value;
	}

	return result;
}


long long func2(std::string strVal,int baseVal)
{
    long long output = 0;


    long len = strVal.length();
    long index;
    //cout << output+power(10,9) << " " << power(9,9) << endl;
    for(index=0;index<len;index++)
    {
        //cout << index << " " <<strVal[index] << " " << pow(baseVal,len-index-1)<< " " << strVal[index] <<endl;
        if(strVal[index] == '1')
        {
            //long long temp = power(baseVal,len-index-1);
      //      cout << output << " " << power(baseVal,len-index-1) << endl;
        //    output += temp;
            output = output + power(baseVal,len-index-1);
          //  cout << output << endl;
        }
    }
    return output;
}


bool func(std::string strVal)
{
   // outfile2 << strVal << endl;
  //  cout << strVal << endl;
  //  return false;

    std::reverse(strVal.begin(), strVal.end());

    int index;

    long long arr[9];
    for(index=2;index<=10;index++)
    {

        long long p = func2(strVal,index);
     //   cout << p << endl;
        long long divisor;
        bool bIsPrime = isPrime(p,divisor);
        if(bIsPrime == true)
            return false;
      //  cout << strVal << " " << index<< " " <<p << " " << bIsPrime << " " << divisor <<endl;
        arr[index-2] = divisor;
    }
    //cout << "Hereeeeeeeeeeeeeeeeeeeee";
    outfile << strVal << " " << arr[0]<< " " <<  arr[1]<< " " << arr[2]<< " " <<  arr[3]<< " " <<  arr[4]<< " " << arr[5]<< " " << arr[6]<< " " << arr[7]<< " " << arr[8] << endl;
    return true;
}

int main()
{
    int n = 16;
    int j = 50;
 //cout << pow (2,n-2)<<endl;


    outfile.open("out.txt");
    outfile << "Case #1:" << endl;
//outfile2.open("out2.txt");
    int curPositive = 0;
    //long long i;
    long long i,jj;
    long long totalVal = power(2,n-2);
    for (i=0;i<totalVal;i++)//loop through permutations
    {
      //  cout << i << endl;
      std::string strVal ="1";
      for (jj=0;jj<n-2;jj++)//loop through binary digits
      {

        if (i&(long long)power(2,jj))//check digits is 1 or 0
          strVal += "1";
          //cout<<'1';

        else
            strVal += "0";
          //cout<<'0';
      }
      //cout<<'\n';
      strVal += "1";

      bool bOut = func(strVal);
      if(bOut == true)
        curPositive += 1;
     //cout << "Found " << curPositive  << endl;
      if(curPositive == j)
        break;
    }

    //long long p = pow(9,33);
   // long long divisor;
    //bool bIsPrime = isPrime(41,divisor);
    //cout  << " " << bIsPrime << " " << divisor <<endl;
    return 0;
}
