#include <string>
#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
int sleep(long long int n);
bool isGood(vector<bool>& check, long long int n);
int main(){
 
  fstream fin, fout;
  fin.open("C.bin");
  fout.open("output.out");
  if (!fin.is_open()) {
    cout << "in file was not open" << endl;
  }
  if (!fout.is_open()) {
    cout << "out file was not open" << endl;
  }
  int test_num;
  fin >>  test_num;
 for (int i = 0; i < test_num; i++) {
   long long int n;
   fin >> n;
   int result = sleep(n);
   if(result == 0)
    fout << "Case #" << i+1 << ": INSOMNIA"  << endl;
   else
    fout << "Case #" << i+1 << ": " << result << endl;
   
 }  
 
  fin.close();
  fout.close();
 
  return 0;
}

bool isGood(vector<bool>& check, long long int n){
  int m;
  // cout << "have:" << endl;
  while (n != 0){
    m = n % 10;
    check[m] = true;
    // cout << m << " ";
    n = n / 10;
  }
  // cout << endl;
  for (int i = 0; i < 10; i++) {
    if (check[i] == false) {
      //    cout << "don't have " << i << endl;
      return false;
    }
  }
  //   cout << endl;
  return true;
}
int sleep(long long int n){
  vector<bool> check(10, false);
  for (int i =  1; i < 10000; i++) {
    int temp = i * n;
    bool res = isGood(check, temp);
    if (res == true) return temp;
  }
  return 0;
}
