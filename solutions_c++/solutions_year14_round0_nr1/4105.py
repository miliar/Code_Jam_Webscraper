#include <iostream>
using namespace std;

struct Set
{
	int arr1[16], a, b, arr2[16], sel1[4], sel2[4];
};



int check_(int a[4], int b[4])
	{
		int sim = 0;
		int ans;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if(a[i] == b[j])
				{
					sim++;
					ans = b[j];
				}	
			}
		}

		if(sim == 1)
			return ans;
		else if(sim == 0)
			return -1;
		else if(sim > 1)
			return 0;
	}

int main()
{
	int cases;

	cin >> cases;
	Set *set;
	set = new Set[cases];
	int num = 0;
	while(num < cases)
	{
		cin >> set[num].a;
		for(int i = 0; i < 16; i ++)
			cin >> set[num].arr1[i];
		cin >> set[num].b;
		for(int i = 0; i < 16; i ++)
			cin >> set[num].arr2[i];
		num ++;
	}

	int ans;
	num = 0;
	while(num < cases)
	{
		for (int i = 0; i < 4; ++i)
		{
			set[num].sel1[i] = set[num].arr1[i + (set[num].a-1)*4];
			set[num].sel2[i] = set[num].arr2[i+ (set[num].b-1)*4];
		}

		ans = check_(set[num].sel1, set[num].sel2);

		if(ans == -1)
		{
			cout << "Case #" << num+1 << ": Volunteer cheated!" << endl;
		}
		else if(ans == 0)
		{
			cout << "Case #" << num+1 << ": Bad magician!" << endl;
		}
		else if (ans > 0)
		{
			cout << "Case #" << num+1 << ": " << ans << endl;	
		}
		num++;
	}

	cin.get();
	return 0;
}
