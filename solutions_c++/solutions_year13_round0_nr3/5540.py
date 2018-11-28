#include<string>
#include<fstream>
#include<vector>
#include<cmath>
#include<unordered_set>
using namespace std;

string inFile = "C-small.in";
string outFile = "C-small.out";
long long GetNumber(long long A, long long B);
bool IsFair(long long number);
unordered_set<long long> fair(1000);

int main()
{
  long long arr[9] = {1,2,3,4,5,6,7,8,9};
  fair.max_load_factor(0.7f);
  fair.insert(arr, arr+9);

  ifstream in(inFile);
  if(in)
  {
    ofstream out(outFile);
    long long totalTests;
    in>>totalTests;
    long long count = 0;
    long long A, B;
    while(count < totalTests)
    {
      in>>A>>B;
      long long result = GetNumber(A, B);
      out<<"Case #"<<count+1<<": ";
      out<<result;
      ++count;
      if(count!=totalTests)
        out<<endl;
    }
  }
  in.close();
  return 0;
}

long long  GetNumber(long long  A, long long B)
{
  long long totalNumber = 0;
  for(long long number = A; number<=B; ++number)
  {
    if(number==1 || number==4 || number==9) {
      ++totalNumber;
      continue;
    } else if(10<=number && number<100) {
      continue;
    } else {
      long long sr1 = sqrt((double)number) - 1.0;
      long long sr2 = sr1+1;
      long long sr3 = sr2+1;
      
      if(number==121)
      {
        int b = 121;
      }
      if(number == 484)
      {
        int b = 484;
      }
      if(sr1*sr1==number || sr2*sr2==number || sr3*sr3==number) { // square
        if(sr1*sr1==number && IsFair(sr1)) { // square root is fair
          fair.insert(sr1);
          if(IsFair(number)) {
            ++totalNumber;
            fair.insert(number);
          }
        } else if(sr2*sr2==number && IsFair(sr2)) { // square root is fair
          fair.insert(sr2);
          if(IsFair(number)) {
            ++totalNumber;
            fair.insert(number);
          }
        } else if(sr3*sr3==number && IsFair(sr3)) {
          fair.insert(sr3);
          if(IsFair(number)) {
            ++totalNumber;
            fair.insert(number);
          }
        } else { //not faire
          continue;
        }
      } else {
        continue;
      }
    } 
  }
  return totalNumber;
}

bool IsFair(long long number)
{
  if(fair.find(number)!=fair.end())
    return true;
  vector<int> vec;
  while(number!=0)
  {
    vec.push_back(number%10);
    number/=10;
  }
  for(int i=0; i<vec.size()/2; ++i)
  {
    if(vec[i]!=vec[vec.size()-1-i])
      return false;
  }
  return true;
}