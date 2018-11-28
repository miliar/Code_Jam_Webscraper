/*

3

2 4
10 5

3 12
7 7 7

3 8
4 2 1

double minpercut[3] = {4, 3, 2};
double schedule[3] = {0,0,0};

Add 4, 3, 2 on each schedule, respectively.

deduct the amount of minimum time. 
and assign the customer for barber with schedule == 0,

if two or more barbers are available, 
select the one with lowest minPerCut.

*/



#include <iostream>
#include <fstream>


using namespace std;

int main()
{
  int T = 1;
  fstream fin, fout;

  fin.open("A.txt");
  fout.open("Result.txt");

  fin >> T;

  for (int t = 0; t < T; t++){
    int B = 0;
    double N = 0, n = 0;
    fin >> B;
    fin >> N;
    
    double *M = new double[B];
    double *S = new double[B];
    int cnt = 0, idx =0, last_idx=-1;

    for (int i = 0; i < B; i++){
      fin >> M[i];
      S[i] = 0;
    }
    
    while (1){
      cnt = 0;
      idx = -1;

      //Find the one with no customer.
      for (int i = 0; i < B; i++){
        if (S[i] == 0){
          cnt++;
          idx = i;
          break;
        }
      }
      //if there is only one baber without customer,
      if (cnt >= 1){
        S[idx] = M[idx];
        last_idx = idx;
        n++;  //  Customer n was assigned now.

        if (n == N) break;
        continue;
      }

      //And, if all barbers are working, deduct the minimum working time.
      if (cnt == 0){
        int min = S[0];

        for (int i = 1; i < B; i++){
          if (S[i] < min){
            min = S[i];
          }
        }
        cnt = 0;
        for (int i = 0; i < B; i++){
          S[i] -= min;
          if (S[i] == 0) cnt++;
        }
        if (cnt == B) break;
      }
    }

    cout << n << " , " << last_idx+1 << endl;
    N = fmod(N, n);
    n = 0;
    idx = last_idx;

    while (N != n){
      cnt = 0;
      idx = -1;

      //Find the one with no customer.
      for (int i = 0; i < B; i++){
        if (S[i] == 0){
          cnt++;
          idx = i;
          break;
        }
      }
      //if there is only one baber without customer,
      if (cnt >= 1){
        S[idx] = M[idx];
        n++;  //  Customer n was assigned now.

        if (n == N) break;
        continue;
      }

      //And, if all barbers are working, deduct the minimum working time.
      if (cnt == 0){
        int min = S[0];

        for (int i = 1; i < B; i++){
          if (S[i] < min){
            min = S[i];
          }
        }
        cnt = 0;
        for (int i = 0; i < B; i++){
          S[i] -= min;
          if (S[i] == 0) cnt++;
        }
        if (cnt == B) break;
      }
    }

    fout << "Case #"<<t+1<<": "<<idx+1 << endl;
  }

  fin.close();
  fout.close();
}

