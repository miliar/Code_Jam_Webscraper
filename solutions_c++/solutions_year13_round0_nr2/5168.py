#include<iostream>
using namespace std;
int main()
{

    int case_num = 0;
    cin >> case_num;
    bool * results = new bool[case_num];
    for (int case_index = 0; case_index < case_num; ++ case_index)
    {
        int row, col;
        int ** data;
        int * row_max;
        int * col_max;
        cin >> row >> col;
        row_max = new int[row];
        col_max = new int[col];
        data = new int*[row];
        for (int i = 0; i < row; ++i)
            row_max[i] = -1;
        for (int j = 0; j < col; ++j)
            col_max[j] = -1;

        for (int i = 0; i < row; ++i)
        {
            data[i] = new int[col];
            for (int j = 0; j < col; ++j)
            {
                int tmp = 0;
                cin >> tmp;
                data[i][j] = tmp;
                if (tmp > row_max[i])
                    row_max[i] = tmp;
                if (tmp > col_max[j])
                    col_max[j] = tmp;
            }
        }
        bool flag = false;
        for (int i = 0; i < row; ++i)
            for (int j = 0; j < col; ++j)
                if(data[i][j] < row_max[i] && data[i][j] < col_max[j])
                {
                    results[case_index] = false;
                    flag = true;
                }
        if(!flag)
        {
            results[case_index] = true;
        }

    }

    for ( int i = 0; i < case_num; ++i)
    {
        if(results[i])
            printf("Case #%d: YES\n",i+1);
        else
            printf("Case #%d: NO\n",i+1);

    }
}
