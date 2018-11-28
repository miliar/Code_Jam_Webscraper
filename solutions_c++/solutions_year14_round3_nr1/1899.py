#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int gcd(int a,int b)
{
    int r;
    while(b!=0)
    {
       r=a%b;
       a=b;
       b=r;
    }
    return a;
}

int is2Pow(int num) {
	int tmp = 1;
	int ret= 0;
	while ( tmp < num) {
		tmp *= 2;
		ret++;
		if ( tmp == num) 
			return ret;
	}
	return -1;
}

int greaterl(int num) {
	int tmp = 1;
	int ret= 0;
	while ( tmp < num) {
		tmp *= 2;
		ret++;
	}
	if (ret >= 1)
	  return ret-1;
	else
		return ret;

}

int main() {
  int N = 0;
  cin >> N;
  for (int i = 1; i <= N; i++) {
		 string str; int num1, num2;
		 int result = 0;
	   cin >> str;	
		 for (int i =0; i < str.size(); i++)
			 if (str[i] == '/')
			   str[i] = ' ';

		 stringstream ss(str);
		 //cout << "str: " << str << endl;
		 ss >> num1 >> num2; 

		 int tmp = gcd(num2, num1);
		 num2 /= tmp;
		 num1 /= tmp;
		 
		 int r2 = is2Pow(num2);
		 if (r2 == -1) {
		   cout << "Case #" << i << ": impossible"  << endl; 
			 continue;
     }
     int r1 = greaterl(num1);
  
		 //cout << "r1: " << r1 << " r2:" <<  r2 << endl;
		 cout << "Case #" << i << ": " << (r2-r1) << endl; 
		  
  }
  return 0; 
}
