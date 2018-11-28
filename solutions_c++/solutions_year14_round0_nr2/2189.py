#include <fstream>
#include <iomanip>

void write_sn(std::ostream& out, int t, int T)
{
	if (t != T)
	{
		out << "\n";
	}
}

int main()
{
	std::ifstream input_file("input.txt");
	std::ofstream out_file("output.txt");
	int T;
	input_file >> T;
	out_file << std::fixed;
	out_file << std::setprecision(7);
	for (int t = 1; t <= T; ++t)
	{
		double c, f, x;
		input_file >> c >> f >> x;
		int k = static_cast<int>(ceil((x*f - c*f - 2*c)/(c*f)) + 0.1);
		out_file << "Case #" << t << ": ";
		if (k <= 0)
		{
			out_file << x/2;
		}
		else
		{
			double xk = x / (2 + k*f);
			double res = 0;
			double cur;
			bool was_sum_xk = false;
			for (int i = 1; i <= k; ++i)
			{
				cur = c / (2 + (k-i)*f);
				if (cur >= xk && !was_sum_xk)
				{
					res += xk;
					was_sum_xk = true;
				}
				res += cur;
			}
			if (!was_sum_xk)
				res+= xk;
			out_file << res;
		}
		write_sn(out_file, t, T);
	}

	return 0;
}