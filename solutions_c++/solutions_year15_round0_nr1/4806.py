#include <iostream>
using namespace std;

int main()
{
    int T, Smax, result;
    char ch;
    FILE *fp;
    fp = fopen("ProblemA.txt", "a");
    cin >> T;
    for (int count = 1; count <= T; count++)
    {
        result = 0;
        int ch_i, sum = 0;
        
        cin >> Smax;
        
        // 对应于第一个数字 
        cin >> ch;
        ch_i = ch - '0';
        sum += ch_i;
        
        for (int i = 0; i < Smax; i++)
        {// 会进入for循环，说明Smax >= 1，那么至少有两个数字，所以这里起始（i取0值时）相当于就是考虑第二个数字x1了！即result >= 1 - x0
            // 考虑数字x(i+1)，result >= 1 - (x0 + ... + xi) 
            if (result < i+1 - sum) // 这里的sum就等于x0 + ... + xi
            {
                result = i+1 - sum;
            }
            cin >> ch;
            ch_i = ch - '0';
            sum += ch_i;
        }
        cout << "Case #" << count << ": " << result << endl;
        fprintf(fp, "Case #%d: %d\n", count, result);  
    }
    fclose(fp);
}
