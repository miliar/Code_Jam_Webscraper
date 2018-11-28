#include <string>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#include <vector>
#define VECTOR(a) VECTOR_((a), sizeof(a) / sizeof(a[0]))
template <typename T>

std::vector<T> VECTOR_(T *array, std::size_t size) {
  return std::vector<T>(array, array + size);
}
static bool sort_using_greater_than(double u, double v)
{
   return u > v;
}


int main()
{
  char new_line;
  int count;
  cin >> count;
  for (int c = 1; c <= count; c++) {
    int N;
    cin >> N;

    double *naomi_blocks = new double[N];
    for (int i = 0; i < N; i++) {
      cin >> naomi_blocks[i];
    }

    double *ken_blocks = new double[N];
    for (int i = 0; i < N; i++) {
      cin >> ken_blocks[i];
    }
    std::sort(&naomi_blocks[0], &naomi_blocks[N], sort_using_greater_than);
    std::sort(&ken_blocks[0], &ken_blocks[N], sort_using_greater_than);

    int decitful_score = 0, score = 0;
    // deceitful war
    {
      vector<double> naomi = vector<double>(naomi_blocks, naomi_blocks + N);
      vector<double> ken = vector<double>(ken_blocks, ken_blocks + N);

      for (int i = naomi.size() - 1; i >= 0; i--) {
        int ken_index = 0;
        bool naomi_is_win = true;// = naomi[i] > ken[0];

        for (int j = ken.size() - 1; j >= 0; j--) {
          if (naomi[j] < ken[j])
            naomi_is_win = false;
        }

        if (!naomi_is_win) {
          ken.erase(ken.begin());
        } else {
          ken.erase(ken.begin() + ken.size() - 1);
        }
        if (naomi_is_win) decitful_score++;
      }
    }

    // war
    {
    std::sort(&naomi_blocks[0], &naomi_blocks[N], sort_using_greater_than);
    std::sort(&ken_blocks[0], &ken_blocks[N], sort_using_greater_than);

      vector<double> naomi = vector<double>(naomi_blocks, naomi_blocks + N);
      vector<double> ken = vector<double>(ken_blocks, ken_blocks + N);
      for (int i = 0; i < naomi.size(); i++) {
        int ken_index = 0;
        bool ken_is_win = ken[0] > naomi[i];
        for (int j = 0; j < ken.size(); j++) {
          if (ken_is_win) {
            ken_index = ken[j] > naomi[i] ? j : ken_index;
          } else {
            ken_index = ken[j] < naomi[i] ? j : ken_index;
          }
        }
        ken.erase(ken.begin() + ken_index);
        if (!ken_is_win) score++;
      }
    }
    printf("Case #%d: %d %d\n", c, decitful_score, score);
  }
}
