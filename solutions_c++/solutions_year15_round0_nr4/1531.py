#include <bits/stdc++.h>
using namespace std;
#define int long long

int x,r,c;

void pain()	{
  cin >> x >> r >> c;
  if((r * c) % x != 0)  {
    cout<<"RICHARD\n";
    return;
  }
  if(x > max(r, c))  {
    cout<<"RICHARD\n";
    return ;
  } 
  if(x == 1 or x == 2 or (x == 3 and min(r,c) >= 2) or (x == 4 and r * c >= 12))	{
    cout<<"GABRIEL\n";
  } else	{
    cout<<"RICHARD\n";
  }
}

#undef int
int main()	{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string input = "input-qual-D.txt";
	string output = "output-qual-D.txt";
	freopen(input.c_str(), "r", stdin);
	freopen(output.c_str(), "w", stdout);
	int tt; cin >> tt;
	for(int iii=1; iii<=tt; iii++)	{
		cout << "Case #" << iii << ": ";
		pain();
	}
}

