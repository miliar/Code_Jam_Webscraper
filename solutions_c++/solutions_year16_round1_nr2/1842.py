#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <cmath> 
#include <map>
#include <set>

using namespace std;
typedef long long LL;

typedef unsigned long long int ULL;



main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
      std::vector<std::vector<int> > matrix;
      int N;
      cin >> N;
      for (int i = 0; i < 2*N - 1; i++)
      {
         matrix.push_back(std::vector<int>());
         std::vector<int>& current = matrix.back();
         for (int j = 0; j < N ; j++)
         {
            int val;
            cin >> val;
            current.push_back(val);
         }
      }
      std::set<int> done;
      int index = -1;
      int col; 
      int num;
      for (int i = 0; i < N; i++)
      {
         std::map<int, int> count;
         for (int j = 0; j < 2*N - 1; j++)
            if (done.find(j) == done.end())
               count[matrix[j][i]] = count[matrix[j][i]] + 1;
         int min = count.begin()->first;
         if (count.begin()->second == 2)
         {
            for (int j = 0; j < 2*N - 1; j++)
               if (matrix[j][i] == min){
                  done.insert(j);
               }
         }
         else 
         {
            for (int j = 0; j < 2*N - 1; j++)
               if (matrix[j][i] == min)
               {
                  index = j;
                  break;
               }
         }
         if (index != -1)
         {
            col = i;
            break;
         }
      }
      std::map<int, int> occur;
      for (int i = 0; i < 2*N - 1; i++)
         occur[matrix[i][col]] = occur[matrix[i][col]] + 1;
      for (int i = 0; i < N; i++)
         if (occur.find(matrix[index][i]) != occur.end())
            occur[matrix[index][i]] = occur[matrix[index][i]] - 1;
      std::set<int> final_set;
      for (std::map<int, int>::iterator it = occur.begin(); it != occur.end(); ++it)
         if (it->second > 0)
            final_set.insert(it->first);
      final_set.insert(matrix[index][col]);
      for (std::set<int>::iterator it = final_set.begin(); it != final_set.end(); ++it)
         cout << *it << " ";

      std::cout << std::endl;


      }
      
	exit(0);
}

