#include <bits/stdc++.h>

using namespace std;

typedef std::vector<int> vi;

int solve(int R, int C, int W)
{
  if(W == 1){
    return R * C;
  }
  /*
    最初は両端からWの次の幅を見ていく
    残りの幅が2W未満になればW+1回で確定できる
    ただし残りの幅がWちょうどの時はWで確定できる
    最後の行の時はそれ、それ以前は1回で否定
   */
  int ans = 0;
  for(int r = 0; r < R; ++r){
    int w = C;
    for(; w >= 2 * W; w -= W){
      ++ans;
    }
    if(r == 0){
      if(w == W){
        ans += W;
      }else{
        ans += W + 1;
      }
    }else{
      ++ans;
    }
  }
  return ans;
}

int main(){
  int T;
  std::cin >> T;
  for(size_t i = 1; i <= T; ++i){
    int R, C, W;
    std::cin >> R >> C >> W;
    std::cout << "Case #" << i << ": " << solve(R, C, W) << "\n";
  }
}
