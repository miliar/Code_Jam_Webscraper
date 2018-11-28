#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

#define REP(I, N) for(int I = 0; I < (N); I++)
#define FOR(I, A, B) for(int I = (A); I <= (B); I++)
#define FORD(I, A, B) for(int I = (A); I >= (B); I--)
#define ll long long
#define F first
#define S second
#define MP make_pair
#define PB push_back

int t;

int main()
{
  scanf("%d", &t);
  FOR(test, 1, t)
  {
    int len, res = 0, cnt = 0;
    scanf("%d", &len);
    string str = "";
    cin >> str;
    
    REP(i, len+1)
    {
      if(i > cnt && str[i] != '0')
	res += i-cnt, cnt += i-cnt;
      cnt += str[i]-'0';
    }
  
    printf("Case #%d: %d\n", test, res);
  }


  return 0;
}