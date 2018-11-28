#include <iostream>
#include <string>


using namespace std;

#define DEBUG 1

void printResult(int test, long long result) {
   cout << "Case #" << test << ": " << result << '\n';
}

char vowels[] = "aeiou";
char* vowelEnd = vowels + sizeof(vowels)/sizeof(vowels[0]);

bool hasN(char* s, long long len, long long n) {
  long long counter = 0;
  for(int i = 0; i < len; ++i) {
    if(find(vowels, vowelEnd, s[i]) == vowelEnd) {
      counter++;
      if(counter == n) {
        return true;
      }
    } else {
      counter = 0;
    }
  }
  return false;
}


int main(int argc, char* argv[]) {

  ios::sync_with_stdio(false);

  int number_of_tests;
  cin >> number_of_tests;

  char name[1000000];
  int n;

  for(int i = 1; i <= number_of_tests; ++i) {
    cin >> name >> n;

    long long nameLen = strlen(name);
    long long counter = 0;

    for(long long k = 0; k < nameLen; ++k) {
      for(long long j = nameLen-1; j >= k; --j) {
        if(hasN(&name[k], j - k + 1, n)) {
          counter++;
        } else {
          break;
        }
      }
    }

    printResult(i, counter);

    memset(name, '\0', 1000000);
  }

  return 0;
}