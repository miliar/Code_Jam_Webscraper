#include <stdio.h>
#include <math.h>
#include <string>
#include <sstream>

#define TRUE 1
#define FALSE 0

int isPalindrome(int _x)
{
    std::stringstream sstm;
    sstm << _x;
    std::string str = sstm.str();
    if (str == std::string(str.rbegin(), str.rend()))
        return TRUE;
    return FALSE;
}

int checkForMagic(int _x)
{
    float sqrt_f = sqrt(float(_x));
    int sqrt_i = int(sqrt_f);
    if (float(sqrt_i) != sqrt_f)
        return FALSE;
    
    if (isPalindrome(_x) && isPalindrome(sqrt_i))
        return TRUE;
    
    return FALSE;
}

int main()
{
    int num;
    scanf("%d\n", &num);

    for (int i = 0; i < num; i++)
    {
        int total = 0;
        int min, max;
        scanf("%d %d\n", &min, &max);
        for (int i = min; i <= max; ++i)
        {                       
            if (checkForMagic(i))
                total++;
        }
        printf("Case #%d: %d\n", i+1, total);
        total = 0;
    }
    return 0;
}
