#include <bits/stdc++.h>
using namespace std;

int main()
{
int tc;
freopen("k.in", "r", stdin);
freopen("b.out", "w+", stdout);
cin >> tc;
for (int i = 1; i <= tc ; i++)
{
int N, sum, k=1;
set <char> st;
cin >> N;
if (N==0) { cout << "Case #" << i << ": INSOMNIA" << endl; continue;   }
while (st.size() < 10)
{
  sum =  N * k++;
 // char *intStr = itoa(sum);
  //string str = to_string(sum);
  stringstream ss;
ss << sum;
string str = ss.str();
  for (int j= 0; j < str.size(); j++)
      st.insert(str[j]);


}
  cout << "Case #" << i << ": " << sum << endl;

}

return 0;
}

