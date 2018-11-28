#include <iostream>
using namespace std;

int main() {
	int N, i, N1, N2, num[3], j, count, ans, tmp, k;
	cin >> N;
	for (i=0;i<N;i++)
	{
		cin >> N1;
		for (j=0; j<N1; j++)
		{
			cin >> num[0] >> num[1] >> num[2] >> num[3];
		}
		while(j<4)
		{
			cin >> tmp >> tmp >> tmp >> tmp;
			j++;
		}
		cin >> N2;
		for (j=0; j<N2; j++)
		{
			count = 0;
			for (k=0;k<4;k++)
			{
				cin >> tmp;
				if (tmp == num[0] || tmp==num[1] || tmp==num[2] || tmp==num[3])
				{
					ans = tmp;
					count += 1;
				}
			}
		}
		while(j<4)
		{
			cin >> tmp >> tmp >> tmp >> tmp;
			j++;
		}
		if (count == 1)
			cout << "Case #" << i+1 << ": " << ans << "\n";
		else if (count == 0)
			cout << "Case #" << i+1 << ": Volunteer cheated!\n";
		else
			cout << "Case #" << i+1 << ": Bad magician!\n";
	}
	return 0;
}