#include <iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;



 vector<int> v;
long long int sleep(long long int n,int caseNum)
{
 
  v.clear();
  long long int digit;
  long long int nNew;
  long long int nNewtwo=0;
  for(int i = 1; v.size() < 10; i++){
   
    nNew = n * i;
    
    nNewtwo = nNew;
    while ( nNew > 0 ) {
      digit = nNew % 10;
      if( find(v.begin(), v.end(), digit) != v.end())
        ;
      else
	v.push_back(digit);
      nNew = nNew / 10;
    }
    
  }
  return( nNewtwo);
  //  cout << "Case #" << caseNum+1<< ": " << nNewtwo << endl;
 
}

int main()
{
  ofstream out;
  out.open("answers.txt");
  int n;
  long int sheep;
  cin >> n;
  for(int i = 0; i < n; i++)
    {
      cin >> sheep;
      if(sheep != 0)
	out << "Case #" << i+1<< ": " << sleep(sheep,i) << endl;
      else{
	out << "Case #" << i+1<< ": "<< "INSOMNIA" << endl;
      }
    }

}
