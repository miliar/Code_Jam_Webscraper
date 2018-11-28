#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;

void solve()
{
    size_t N, M;
    std::cin >> N >> M;

    int lawn[N][M];
    
    for(size_t i = 0; i < N; i++)
    for(size_t j = 0; j < M; j++)
        std::cin >> lawn[i][j];


    std::vector<int> ver(N);
    std::vector<int> hor(M);

    
    for(size_t i = 0; i < N; i++)
    {
        int hmax = 0;
        for(size_t j = 0; j < M; j++)
            hmax = std::max(lawn[i][j], hmax);
        ver[i] = hmax;
    }
    
    for(size_t i = 0; i < M; i++)
    {
        int hmax = 0;
        for(size_t j = 0; j < N; j++)
            hmax = std::max(lawn[j][i], hmax);
        hor[i] = hmax;
    }

    
    for(size_t i = 0; i < N; i++)
    for(size_t j = 0; j < M; j++)
    {
        int h = lawn[i][j];
        if(h < ver[i] && h < hor[j])
        {
            std::cout << "NO";
            return;
        }
    }

    std::cout << "YES";
}

int main()
{
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}
