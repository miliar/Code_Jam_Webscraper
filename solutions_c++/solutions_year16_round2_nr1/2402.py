#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char input[2010];
int num[20];
int alpha[30];

int main() {

   int T, C, i, j, cnt;
   cin>> C;
   for (T = 1; T <= C; T++) {
      cin >> input;
      memset(num, 0, sizeof(num));
      memset(alpha, 0, sizeof(alpha));
      int len = strlen(input);
      for (i = 0; i < len; i++) {
         int tmp = input[i]-'A';
         alpha[tmp]++;
      }

      num[0] = alpha['Z'-'A'];
      num[2] = alpha['W'-'A'];
      num[4] = alpha['U'-'A'];
      num[6] = alpha['X'-'A'];
      num[8] = alpha['G'-'A'];
      num[7] = alpha['S'-'A'] - num[6];
      num[5] = alpha['F'-'A'] - num[4];
      num[3] = alpha['H'-'A'] - num[8];
      num[1] = alpha['O'-'A'] - num[0] - num[2] -num[4];
      num[9] = alpha['I'-'A'] - num[5] - num[6] - num[8];

      cout << "Case #" <<T<<": ";

      for( i= 0; i <10; i++) {
         for (j = 0; j < num[i]; j++)
            cout<< i;
      }

      cout<<endl;
   }
   return 0;
}
