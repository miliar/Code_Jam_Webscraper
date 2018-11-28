#include <iostream>
#include <algorithm>

using namespace std;

int a[20000];

int main()
{
    int T, N, X;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
	cin >> N >> X;
	for (int i = 0; i < N; i++)
	    cin >> a[i];
	sort(a, a + N);
	reverse(a, a + N);
	int j = N - 1;
	int ans = 0;
	for (int i = 0; i <= j; i++)
	{
	    if (a[i] + a[j] <= X)
		j--;
	    ans++;
	}
	cout << "Case #" << t << ": ";
	cout << ans << endl;
    }
}

    
