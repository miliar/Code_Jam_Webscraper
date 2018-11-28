#include <iostream> 
#include <sstream>
#include <vector>
using namespace std; 
using ULL = unsigned long long;
ULL power(ULL n, int p)
{
if(p == 0) return 1;
ULL ans = n;
for(int i=1; i<p; ++i)
ans *= n;
return ans;
}
int main() {
int T, K, C, S;
cin >> T;
for (int i = 1; i <= T; ++i) {
cin >> K >> C >> S;
vector<ULL> answer;
ULL exp = power(K, C-1);
for(auto j=0; j<S; ++j)
answer.push_back(1+static_cast<ULL>(j) * exp);
cout << "Case #" << i << ":";
for(auto a:answer) cout <<" "<<a;
cout<<endl;
}
return 0;
}
