#include "iostream"
#include <fstream>
#include <iomanip>
#include "cmath"
using namespace std;
int getMax(int arr[], int n){
  int mx = arr[0];
  for (int i = 1; i < n; i++)
    if (arr[i] > mx)
      mx = arr[i];
  return mx;
}

void countSort(int arr[], int n, int exp){
  int output[n];
  int i, count[10] = {0};
  for (i = 0; i < n; i++)
    count[ (arr[i]/exp)%10 ]++;
  for (i = 1; i < 10; i++)
    count[i] += count[i - 1];
  for (i = n - 1; i >= 0; i--){
    output[count[ (arr[i]/exp)%10 ] - 1] = arr[i];
    count[ (arr[i]/exp)%10 ]--;
  }
  for (i = 0; i < n; i++)
    arr[i] = output[i];
}
 
void radixsort(int arr[], int n){
  int m = getMax(arr, n);
  for (int exp = 1; m/exp > 0; exp *= 10)
    countSort(arr, n, exp);
}

int main(int argc, char const *argv[]){
  ofstream myfile;
  myfile.open ("output.txt");
  int cases;
  cin >> cases;
  for(int c=0; c<cases; ++c){
    int blocks, n;
    cin >> n;

    int n_blocks[n];
    for (int i = 0; i < n; ++i){
      double temp;
      cin >> temp;
      n_blocks[i] = temp*10000;
    }

    int k_blocks[n];
    for (int i = 0; i < n; ++i){
      double temp;
      cin >> temp;
      k_blocks[i] = temp*10000;
    }

    radixsort(n_blocks, n);
    radixsort(k_blocks, n);

    int win_deceit=0, lower=-1, upper=n-1;
    for (int i = n-1; i > lower; --i){
      // cout << n_blocks[i] << " " << k_blocks[upper] << endl;
      while(n_blocks[i] < k_blocks[upper--]){
        ++lower;
      }
      if (n_blocks[i] > k_blocks[upper])
        win_deceit++;
    }

    int win=n;
    for (int i = 0; i < n; ++i){
      for (int j = 0; j < n; ++j){
        if(k_blocks[j] > n_blocks[i]){
          win--;
          k_blocks[j] = 0;
          break;
        }
      }
    }

    myfile << "Case #" << c+1 << ": " << win_deceit << " " << win << endl;
  }
  return 0;
}