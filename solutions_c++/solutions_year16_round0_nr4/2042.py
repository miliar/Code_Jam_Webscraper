#include <iostream>

int main()
{
    int testNum;
    std::cin >> testNum;
    for(int testId = 1; testId <= testNum; testId++)
    {
	 std::cout << "Case #" << testId << ": "; 
         int k, c, s;
	 std::cin >> k >> c >> s;
	 if (s * c >= k)
	 {
		 int j = 0;
		 while (j < k)
		 {
			 long long ans = 0;
			 for (int i = 0; i < c; i++)
			 {
				 if(j + i < k)
				 {
					 ans = ans * k + j + i;
				 }
			 }
			 j += c;
			 std:: cout << ans + 1 << " ";
		 }
		 std::cout << std::endl;
	 }
	 else
	 {
		 std::cout << "IMPOSSIBLE" << std::endl;
	 }
    }
    return 0;
}

