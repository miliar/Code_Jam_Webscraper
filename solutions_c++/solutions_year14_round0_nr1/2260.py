#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-result.txt", "w", stdout);
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    vector<int> s1;
    vector<int> s2;
    int r1, r2;
    scanf("%d", &r1);
    for (int j = 0; j < 16; ++j)
    {
      int a;
      scanf("%d", &a);
      if ((j / 4) + 1 == r1)
        s1.push_back(a);
    }

    scanf("%d", &r2);

    for (int j = 0; j < 16; ++j)
    {
      int a;
      scanf("%d", &a);
      if ((j / 4) + 1 == r2)
        s2.push_back(a);
    }

    vector<int> answers;

    for (int j = 0; j < s1.size(); ++j)
    {
      for (int k = 0; k < s2.size(); ++k)
        if (s1[j] == s2[k])
          answers.push_back(s1[j]);
    }

    printf("Case #%d: ", i + 1);

    if (answers.size() == 1)
      printf("%d", answers.front());
    else if (answers.size() == 0)
      printf("Volunteer cheated!");
    else
      printf("Bad magician!");



    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);

  return 0;
}
