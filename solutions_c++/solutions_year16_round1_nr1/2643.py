#include <iostream>
#include <cstdio>
#include <vector>
#include <list>

using namespace std;


int main() {
  int T;
  char word[1005];
  list<char> res;

  scanf("%d", &T);

  for(int caso = 1; caso <= T; caso++) {
    scanf("%s", word);

    res.clear();
    res.push_front(word[0]);

    for(int i = 1; word[i] != '\0'; i++) {
      if(word[i] < res.front())
        res.push_back(word[i]);
      else
        res.push_front(word[i]);
    }

    printf("Case #%d: ", caso);
    for(list<char>::iterator it = res.begin(); it != res.end(); it++) {
      printf("%c", *it);
    }
    printf("\n");
  }


  return 0;
}
