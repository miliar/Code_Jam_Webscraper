#include <cstdio>
#include <iostream>
using namespace std;

int m[17];

int main() {
  int T, A, tmp, cnt=1, ans, ansCnt;

//  freopen("A-small-attempt5.in", "r", stdin);
//  freopen("output5.out", "w", stdout);

  for (cin >> T; T--;) {
	for (int i = 0; i < 17; i++) m[i]=0;
	ansCnt = 0;
    cin >> A;
    for (int i = 0; i < 16; i++)
    {
        cin >> tmp;
        if(i >= (A-1)*4 && i < A*4) m[tmp] = 1;
    }
	cin >> A;
	for (int i = 0; i < 16; i++)
	{
		cin >> tmp;
		if(i >= (A-1)*4 && i < A*4 && m[tmp] == 1)
		{
			ansCnt++; ans = tmp;
		}
	}
    if(ansCnt == 1) cout << "Case #" << cnt++ << ": " << ans << "\n";
    else if(ansCnt > 1) cout << "Case #" << cnt++ << ": Bad magician!\n";
    else if(ansCnt < 1) cout << "Case #" << cnt++ << ": Volunteer cheated!\n";
  }

  return 0;
}
