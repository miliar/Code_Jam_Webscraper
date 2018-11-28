
#include <iostream>
#include <sstream>
#include <numeric>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <stdio.h>
#include <fstream>
using namespace std;

unsigned long long ToInt(string num)
{
	istringstream buffer(num);
	unsigned long long value;
	buffer >> value;  
	return value;
}

vector<int> ToVec(long num)
{
	vector<int> res;
	while(num>0)
	{
		res.push_back(num%10);
		num/=10;
	}
	reverse(res.begin(),res.end());
	return res;
}
bool isPalindrom(vector<int> vec)
{
	vector<int> revVec = vec;
	reverse(revVec.begin(),revVec.end());
	return revVec == vec;
}
bool All9(vector<int> vec)
{
	for(int i = 0 ; i < vec.size(); i++)
		if(vec[i]!=9)
			return false;
	return true;
}
vector<int> getNextSmallestPalindrom(vector<int> vec)
{
	int n = vec.size();
	vector<int> res;

	if(n==1)
	{
		if(vec[0]<9)
		{
			vec[0]++;
			return vec;
		}
		res = vector<int>(n+1,1);
		return res;
	}
	if(All9(vec))
	{
		res = vector<int>(n+1,0);
		res[0] = 1;
		res[n] = 1;
		return res;
	}

    int mid = n/2;
 
    bool leftsmaller = false;
 
    int i = mid - 1;
 
    int j = (n % 2)? mid + 1 : mid;
 
  
    while (i >= 0 && vec[i] == vec[j])
        i--,j++;

    if ( i < 0 || vec[i] < vec[j])
        leftsmaller = true;
 
    while (i >= 0)
    {
        vec[j] = vec[i];
        j++;
        i--;
    }

    if (leftsmaller == true)
    {
        int carry = 1;
        i = mid - 1;
 
        if (n%2 == 1)
        {
            vec[mid] += carry;
            carry = vec[mid] / 10;
            vec[mid] %= 10;
            j = mid + 1;
        }
        else
            j = mid;
 
        while (i >= 0)
        {
            vec[i] += carry;
            carry = vec[i] / 10;
            vec[i] %= 10;
            vec[j++] = vec[i--]; // copy mirror to right
        }
    }
	return vec;
}

long double ToNum(vector<int> vec)
{
	unsigned long long num = 0;
	int multiplier = 1;
	for(int i = vec.size()-1 ; i >= 0; i--)
	{
		num += vec[i]*multiplier;
		multiplier *=10;
	}
	return num;
}

int main () 
{
  fstream fin;
  fstream fout;
  fin.open("C-small-attempt0.in",ios::in);
  fout.open("C-small-attempt0.out",ios::out);

  long  A;
  long  B;
  vector<int> vecA;
  string sA;
  int T,count;
  fin>>T;
  for(int i = 0 ; i < T ; i++)
  {
	  fin>>A>>B;
	  count = 0;

	  while(A<=B)
	  {
		  vecA = ToVec(A);
		  if(A<=B)
		  {
			  long  sqrtA = (long) sqrt((double)A);
			  if(sqrtA*sqrtA == A)
			  {
				  vector<int> vecSqrt = ToVec(sqrtA);
				  if(isPalindrom(vecSqrt))
					  count++;
			  }
		  }
		  else
			  break;
		  
		  vecA = getNextSmallestPalindrom(vecA);
		  A = ToNum(vecA);
	  }
	  fout<<"Case #"<<i+1<<": "<<count<<endl;
  }

  fout.close();
  fin.close();
  return 0;
}