#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

class solve {
  public:
    solve() {
      processIn();
      printf("%d\n",calcMinFriendNum());
    }
    ~solve() {
     delete[] shyStr;
    }

    int processIn() {
      scanf("%d",&Smax);
      getchar();
      shyStr = new char[Smax+2];
      gets(shyStr);
      return 0;
    }

    int calcMinFriendNum() {
      int standNum = 0;
      int minFriendNum = 0;
      for(int i = 0;i <= Smax;i++) {
        shyStr[i] -= '0';
        if(shyStr[i] == 0)
            continue;
        if(i > standNum) {
            minFriendNum += i-standNum;
            standNum = i+shyStr[i];
        }
        else {
            standNum += shyStr[i];
        }
      }
      return minFriendNum;
    }
  private:
    int Smax;
    char* shyStr;
};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i = 1;i <= T;i++) {
        printf("Case #%d: ",i);
        solve Oviation;
    }
    return 0;
}
