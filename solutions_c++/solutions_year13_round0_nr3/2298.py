#include<iostream>
#include<vector>
#include<string>
#define rep(x,n) for (int x = 0; x < n; x++)
#define pb push_back
using namespace std;
 string tab[40] = {"1",
"4",
"9",
"121",
"484",
"10201",
"12321",
"14641",
"40804",
"44944",
"1002001",
"1234321",
"4008004",
"100020001",
"102030201",
"104060401",
"121242121",
"123454321",
"125686521",
"400080004",
"404090404",
"10000200001",
"10221412201",
"12102420121",
"12345654321",
"40000800004",
"1000002000001",
"1002003002001",
"1004006004001",
"1020304030201",
"1022325232201",
"1024348434201",
"1210024200121",
"1212225222121",
"1214428244121",
"1232346432321",
"1234567654321",
"4000008000004",
"4004009004004",
"200000000000000"};
bool por(const string aa, const string bb)
{
 if (aa.size() < bb.size()) return true;
 if (aa.size() > bb.size()) return false;
 rep(x,aa.size())
 {
  if (aa[x] < bb[x]) return true;
  if (aa[x] > bb[x]) return false;
 }
 return false;
}
int main()
{
 int t; cin >> t; string aa,bb; bool p; int y,yy,wyn;
 rep(x,t)
 {
     aa.clear();bb.clear();
  cin >> aa; cin.get(); cin >> bb; y = -1; wyn = 0;
  do
  {
    ++y;
    p = por(aa,tab[y]);
  } while(!p);
  yy = -1;
  do
  {
    ++yy;
    p = por(bb,tab[yy]);
  } while(!p);
  wyn = yy - y;
  if (y > 0)
  {
    if (tab[y-1] == aa) ++wyn;
  }
  //cout << "yy " << yy << " y " << y <<"\n";
  cout << "Case #" << x+1 << ": " << wyn << "\n";
 }
 return 0;
}
