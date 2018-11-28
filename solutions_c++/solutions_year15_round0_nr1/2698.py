#include<fstream>
#include<iostream>
#include<cstdio>
#include<map>
#include<string>

using namespace std;

#define FL(i, a, b) for(int i = a; i < b; i++)
#define MIN(a, b) ((a > b)? b : a)
#define MAX(a, b) ((a > b)? a : b)

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("file input\n");
    return -1;
  }

  ifstream fin(argv[1]);
						
  int T;
  fin>>T;
  FL(t,0,T) {																																																							
    int S;
    string nums;
    fin>>S>>nums;

    int ans = 0;
    int total = 0;
    FL(i, 0, nums.size()) {
      int num = nums[i] - '0';
      if (total >= i) {
        total += num;
      } else {
        ans += 1;
        total += num + 1;
      }
    }

    printf("Case #%d: %d\n",t + 1,ans																													);
  }
  return 0;
}

