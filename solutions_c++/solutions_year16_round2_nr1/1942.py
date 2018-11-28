#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

//#define small 
#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;

void reduce (std::vector<int>& wOc, std::string& str, int repetitions){
  //reduces the occurences of str's letters in wOc by repetitions

  for(int i = 0; i < str.size(); i++){
    wOc[str[i]] -= repetitions;
  }
}

int main()
{
#if defined(small)
  freopen("A-small-attempt0.in", "r", stdin);
#elif defined(large)
  freopen("A-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    fprintf(stderr, "Case #%d: ", t);
    
    std::string str;
    std::cin >> str;
    std::vector<std::string> numberStr = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

    std::vector<int> wOc(200);
    for(int i = 0; i < str.size(); i++){
      wOc[str[i]]++;
    }

    std::vector<int> numberOc(10);
    std::vector<int> numbs = {0, 6, 8, 2, 7, 5, 4, 3, 9, 1};
    std::vector<char> lets = {'Z', 'X', 'G', 'W', 'S', 'V', 'F', 'T', 'I', 'O'};
    for(int i = 0; i < numbs.size(); i++){
      numberOc[numbs[i]] += wOc[lets[i]];
      reduce(wOc, numberStr[numbs[i]], wOc[lets[i]]);
    }

    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < numberOc[i]; j++) {
	printf("%d", i);
	fprintf(stderr, "%d", i);
      }
    }
    
    printf("\n");
    fprintf(stderr, " \n");
  }
  return 0;
}
