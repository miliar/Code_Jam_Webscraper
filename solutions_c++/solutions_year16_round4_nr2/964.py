#include <iostream>
#include <algorithm>
#include <iomanip>

//double tie[201][201][402];
double tie[201][402];
double p[200];
double pp[200];
int n;
int k;

double f_tie(int i, int z)
{
    if (tie[i][n + z] >= 0)
    {
        //std::cout << "LOG " << " " << i << " " << z << " : " << tie[i][n+z] << "\n";
        return tie[i][n + z];
    }

    tie[i][n + z] = pp[i] * f_tie(i + 1, z + 1) + (1 - pp[i]) * f_tie(i + 1, z - 1);
    //std::cout << "LOG " << " " << i << " " << z << " : " << tie[i][n+z] << "\n";
    return tie[i][n + z];
}

double find()
{
    for (int j = 0 ; j <= n ; ++j)
        for (int z = 0 ; z <= 2 * n ; ++z)
            tie[j][z] = -1;
    for (int z = 0 ; z <= 2 * n ; ++z)
        tie[k][z] = 0;
    tie[k][n] = 1;
    return f_tie(0, 0);
}

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        std::cin >> n >> k;
        /*for (int i = 0 ; i <= n ; ++i)
            for (int z = 0 ; z <= 2 * n ; ++z)
                tie[0][i][z] = tie[1][i][z] = 0;
        int curr = 0;
        tie[0][0][n] = 1;*/
        for (int i = 0 ; i < n ; ++i)
            std::cin >> p[i];
        std::sort(p, p + n);
#if 0
            for (int j = 0 ; j <= n ; ++j)
                for (int z = 0 ; z <= 2 * n ; ++z)
                    tie[1 - curr][j][z] = tie[curr][j][z];
            for (int j = 0 ; j < n ; ++j)
            {
                for (int z = 0 ; z <= 2 * n ; ++z)
                {
                    double x = 0;
                    if (z > 0)
                        x += p[i] * tie[curr][j][z - 1];
                    if (z < 2 * n)
                        x += (1 - p[i]) * tie[curr][j][z + 1];
                    tie[1 - curr][j + 1][z] = std::max(tie[1 - curr][j + 1][z], x);
                }
            }
            curr = 1 - curr;
            /*for (int j = 0 ; j <= n ; ++j)
                for (int z = 0 ; z <= 2 * n ; ++z)
                    tie[i][j][z] = -1;*/
        }
#endif
        
        double res = 0;//find();
        /*for (int z = 0 ; z < 1 << n ; ++z)
        {
            int c = 0;
            for (int i = 0 ; i < n ; ++i)
            {
                if (z & (1 << i))
                    pp[c++] = p[i];
            }
            if (c == k)
            {
                double d = find();
                if (d > res)
                {
                    res = d;
                    std::cout << d << " : ";
                    for (int i = 0 ; i < k ; ++i)
                        std::cout << pp[i] << " ";
                    std::cout << "\n";
                }
            }
        }*/
        for (int z = 0 ; z <= k ; ++z)
        {
            int c = 0;
            for (int i = 0 ; i < z ; ++i)
                pp[c++] = p[i];
            for (int i = 0 ; i < k - z ; ++i)
                pp[c++] = p[n - i - 1];
            double d = find();
            if (d > res)
            {
                res = d;
            }
        }
        /*for (int i = 0 ; i < n ; ++i)
            std::cout << p[i] << " ";
        std::cout << "\n";*/
        /*
        int mid = n / 2;
        for (int i = 0 ; i < k / 2 ; ++i)
        {
            pp[2 * i] = p[mid + i];
            pp[2 * i + 1] = p[mid - 1 - i];
        }
        res = std::max(res, find());
        if (n % 2)
        {
            ++mid;
            for (int i = 0 ; i < k / 2 ; ++i)
            {
                pp[2 * i] = p[mid + i];
                pp[2 * i + 1] = p[mid - 1 - i];
            }
        }
        res = std::max(res, find());
        */
        std::cout.setf(std::ios::fixed);
        std::cout.precision(8);
		std::cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}

