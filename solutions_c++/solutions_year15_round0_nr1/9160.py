#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    std::ifstream in("in.txt"); // used For debugging
    std::cin.rdbuf(in.rdbuf());
    cin.tie(0);

    int N, K, need, carry;
    cin >> N;
    for(int i=1;i<=N;++i){
      cin >> K;
      char c;
      carry = need = 0;
      for(int j=0;j<=K;++j){
        cin >> c;
        carry+= c-48-1;//48= '0', one used;
        if(carry==-1){
          ++need;
          carry=0;
        }

      }
      cout << "Case #"<< i << ": " << need << "\n";

    }
}
