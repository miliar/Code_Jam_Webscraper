#include<iostream>
#include<math.h>

using namespace std;

long jamcoinsToShow = 0;

long long checkPrime(long long jam){
  long long sqrtJam = sqrt(jam);
  for(long long i = 2; i <= sqrtJam ; i++){
    if(jam % i == 0){
      return i;
    }
  }
  return 1;
}


long long jamPow(int base, int n){
  if(n == 0){
    return 1;
  }
  return base*pow(base, n-1);
}

long long getBaseN(int jamcoin[] , int n, int base){
  long long jam = 0;
  for(int i = n-1 ; i >= 0 ; i--){
    jam += jamcoin[i]*jamPow(base, n-1-i);
  }
  return jam;
}

void generateJamCoin(int jamcoin[], int lowIndex, int highIndex, int n){
  if(highIndex < lowIndex){
    if(jamcoinsToShow > 0){
      long long divisors[9] = {0};
      for(int base = 2 ; base <= 10 ; base++){
        long long jam = getBaseN(jamcoin, n, base);
        long long divisor = checkPrime(jam);
        if(divisor > 1 && divisor < jam){
          divisors[base-2] = divisor;
        }
        else{
          return;
        }
      }
      cout<<"\n";
      for(int index = 0 ; index < n ; index++){
        cout<<jamcoin[index];
      }
      for(int index = 0 ; index < 9 ; index++){
        cout<<" "<<divisors[index];
      }
      jamcoinsToShow--;

    }
  }
  else{
    jamcoin[highIndex] = 0;
    generateJamCoin(jamcoin, lowIndex, highIndex-1, n);
    jamcoin[highIndex] = 1;
    generateJamCoin(jamcoin, lowIndex, highIndex-1, n);
  }
}

void printJamCoin(int n){
  cout<<"Case #1:";
  int jamcoin[n];
  jamcoin[0] = 1;
  jamcoin[n-1] = 1;
  generateJamCoin(jamcoin, 1, n-2 , n);
}


int main(){
  long t;
  cin>>t;
  while(t--){
    int n;
    long j;
    cin>>n>>j;
    jamcoinsToShow = j;
    printJamCoin(n);
  }
  return 0;
}
