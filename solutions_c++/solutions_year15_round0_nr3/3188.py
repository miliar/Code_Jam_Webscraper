#include <iostream>
using namespace std;

char value[10001][10001]; // 用于存储l_x字符串[i, j)的四元乘积，数组较大，所以定义成全局变量！

char table[300][300]; // 四元乘积表 

char l[10001];
char l_x[10001];
     
char multiply(char ch1, char ch2) // ch1对应l_x[]中元素，只会是i,j,k中的一种，右边是乘积的值，可以为负数和1等等 
{
    return table[ch1][ch2 + 150]; 
} 

void get_value(int L, int X) // 计算l_x字符串[i, j)的四元乘积，char可以为负数！ 
{
    // 最先得到[L * X - 1, L * X )，再是[L * X - 2, L * X)，[L * X - 2, L * X - 1)，再是[L * X - 3, L * X)，[L * X - 3, L * X - 1)，[L * X - 3, L * X - 2)，依次使用之前得到的值来计算下去 
    for (int i = L * X - 1; i >= 0; i--)
    {
        for (int j = L * X; j > i; j--)
        {
            if (j - i == 1) // [i, j) = [i, i+1)，即l_x[i] 
            {
                value[i][j] = l_x[i];
            }
            else
            {
                value[i][j] = multiply(l_x[i], value[i+1][j]);// [i, j) = [i, i+1) 和 [i+1, j)的四元乘积，即l_x[i]和value[i+1][j]（在value[i][j]前已计算得到）的四元乘积
            }            
        }
    }
    
//    for (int i = 0; i <= L * X; i++)
//    {
//        for (int j = 0; j <= L * X; j++)
//        {
//            if(value[i][j] == -'i')
//                cout << "-i" << " "; 
//            else if(value[i][j] == -'j')
//                cout << "-j" << " "; 
//            else if(value[i][j] == -'k')
//                cout << "-k" << " "; 
//            else if(value[i][j] == -1)
//                cout << "-1" << " "; 
//            else if(value[i][j] == 'i')
//                cout << "i" << " "; 
//            else if(value[i][j] == 'j')
//                cout << "j" << " "; 
//            else if(value[i][j] == 'k')
//                cout << "k" << " "; 
//            else if(value[i][j] == 1)
//                cout << "1" << " "; 
//            else
//                cout << "*" << " ";
//        }
//        cout << endl;
//    }
}

int main()
{
    int T, L, X;
    bool result;
    
    FILE *fp, *fp_input;
    fp_input = fopen("ProblemC-small_input.txt", "r");
    fp = fopen("ProblemC.txt", "w");
    
    table['i'][-1 + 150] = -'i';
    table['i'][-'i' + 150] = 1;
    table['i'][-'j' + 150] = -'k';
    table['i'][-'k' + 150] = 'j';
    table['i'][1 + 150] = 'i';
    table['i']['i' + 150] = -1;
    table['i']['j' + 150] = 'k';
    table['i']['k' + 150] = -'j';
    table['j'][-1 + 150] = -'j';
    table['j'][-'i' + 150] = 'k';
    table['j'][-'j' + 150] = 1;
    table['j'][-'k' + 150] = -'i';
    table['j'][1 + 150] = 'j';
    table['j']['i' + 150] = -'k';
    table['j']['j' + 150] = -1;
    table['j']['k' + 150] = 'i';
    table['k'][-1 + 150] = -'k';
    table['k'][-'i' + 150] = -'j';
    table['k'][-'j' + 150] = 'i';
    table['k'][-'k' + 150] = 1;
    table['k'][1 + 150] = 'k';
    table['k']['i' + 150] = 'j';
    table['k']['j' + 150] = -'i';
    table['k']['k' + 150] = -1;
    
    // cin >> T;
    fscanf(fp_input, "%d", &T); 
    for (int count = 1; count <= T; count++)
    {
        result = false;
        // cin >> L >> X;
        fscanf(fp_input, "%d", &L);
        fscanf(fp_input, "%d", &X);
        
        for (int i = 0; i < L; i++)
        {
            // cin >> l[i];
            l[i] = fgetc(fp_input);
            while (l[i] == '\n') // 遇到换行符，则继续读取 
            {
                l[i] = fgetc(fp_input);
            }
        }
        
        for (int i = 0; i < X; i++)
        {
            for (int j = 0; j < L; j++)
            {
                l_x[i*L + j] = l[j];
            }
        }
        
        get_value(L, X);
        
        if (value[0][L * X] != -1) // 最后四元乘积结果与i*j*k=-1不同，那么一定不可以归约成i*j*k
        {
            result = false;
        } 
        else
        {
            for (int i = 1; i <= L * X - 2; i++)
            {
                if (value[0][i] == 'i') // [0, i)
                {
                    // cout << "[0, " << i << ")" << endl;
                    for (int j = i; j <= L * X - 1; j++)
                    {
                        if (value[i][j] == 'j') // [i, j)
                        {
                            //cout << "[" << i << ", " << j << ")" << endl;
                            if (value[j][L * X] == 'k') // [j, L * X)
                            {
                                result = true;
                                goto print_place;
                            }
                            // 否则，继续判断下一个j，看[i, j)四元乘积能否是'j' ，且[j, L * X)能否是'k'
                            else
                            {
                                continue;
                            }
                        }
                        // 否则，继续判断下一个j，看[i, j)四元乘积能否是'j' 
                        else
                        {
                            continue;
                        } 
                    }
                }
                // 否则，继续判断下一个i，看[0, i)四元乘积能否是'i' 
                else
                {
                    continue;
                }
            }
        } 
        

    print_place:
        
        cout << "Case #" << count << ": ";
        if (result)
        {
            cout << "YES" << endl;
            fprintf(fp, "Case #%d: YES\n", count);
        }
        else
        {
            cout << "NO" << endl;
            fprintf(fp, "Case #%d: NO\n", count);
        }  
    }
    fclose(fp_input);
    fclose(fp);
    
    return 0;
}
