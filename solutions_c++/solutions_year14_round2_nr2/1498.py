#include <iostream>
#include <fstream>

int main()
{
	std::ifstream ins("input.txt");
	std::ofstream outs("output.txt");
	int T;
	ins >> T;
	for (int t = 1; t <= T; ++t)
	{
		outs << "Case #" << t << ": ";
		int a, b, k;
		ins >> a >> b >> k;
		int ans = 0;
		for (int i = 0; i < a; ++i)
			for (int j = 0; j < b; ++j)
				if ((i&j) < k)
					++ans;
		outs << ans << "\n";
	}
	ins.close();
	outs.close();
	return 0;
}