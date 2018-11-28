#include <iostream>
#include <math.h>
#include <string>
#include <cstring>

char word[105];

bool isPalindrome(int num)
{
    int i = 0;

    sprintf(word, "%d",num);
    int j = strlen(word) - 1;
    //std::cout << "i = " << i << " j = " << j << std::endl;

    while(i < j)
    {
        if(word[i++] != word[j--])
            return false;
    }
    return true;
}

int main(void)
{
    int runs;
    std::cin >> runs;

    for(int r = 1; r <= runs; ++r)
    {
        int low ,high;
        std::cin >> low;
        std::cin >> high;

        int sqLow = sqrt(low);
        int sqHigh = sqrt(high);

        if(sqLow * sqLow < low)
            sqLow++;
        if(sqHigh * sqHigh <= high)
            sqHigh++;

        int count = 0;

        for(int i = sqLow; i < sqHigh; ++i)
        {
            //std::cout << i << "\t";
            if(isPalindrome(i))
            {
                //std::cout << "Candidate " << i << " ";
                int sq = i*i;
                if(isPalindrome(sq))
                {
                    ++count;
                    //std::cout << " was correct " << sq << std::endl;
                }
                else
                {
                    //std::cout << "Nops" << std::endl;
                }
            }
            else
            {
                //std::cout << "No...\n";
            }
        }

        std::cout << "Case #" << r << ": " << count << std::endl;
    }

    return 0;
}
