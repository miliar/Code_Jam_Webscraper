#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>


using namespace std;
int cf(float num){
    int inum = (int)num;
    if (num == (float)inum) {
        return inum;
    }
    return inum + 1;
}

int main()
{
	long long int t, d, k, ix, max_k = -1, ans, min_ans;
	std::vector<int> vint;
	cin >> t;
	for (int i=1; i<=t;i++)
	{	
		ans = 0;
		cin >> d;
		ix = d;
		vint.clear();
		while (ix--)
		{	
			cin >> k;
			vint.push_back(k);
			if (k > max_k)
				max_k = k;
		}
		for (int j=1;j<=max_k;j++){	
			ans = 0;
			for (int l=0; l<d; l++){
				ans = ans + cf(vint[l]*1.0/j) - 1;
			}
			ans = ans + j;
			if (j == 1)		min_ans = ans;
			if (ans < min_ans)		min_ans = ans;
		}
		cout << "Case #" << i << ": " << min_ans << endl;
	}
	return 0;
}
