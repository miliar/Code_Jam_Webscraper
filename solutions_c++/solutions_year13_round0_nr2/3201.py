#include <iostream>

int max(int a, int b)
{
    return a>b?a:b;
}

bool Valid(int**& a, int l, int w)
{
    int max_row[l];
    int max_col[w];
    for(int i = 0; i < l; i++)
        max_row[i] = 1;
    for(int i = 0; i < w; i++)
        max_col[i] = 1;

    //Now look at the max for each col and row.
    for(int i = 0; i < l; i++)
        for(int j = 0; j < w; j++)
        {
            max_row[i] = max(max_row[i],a[i][j]);
            max_col[j] = max(max_col[j],a[i][j]);
        }
    for(int i = 0; i < l; i++)
        for(int j = 0; j < w; j++)
            if(a[i][j] != max_row[i]
            && a[i][j] != max_col[j])
                return false;
    return true;

}

void setup(int**& arr, int l, int w)
{
    arr = new int*[l];
    for(int i = 0; i < l; i++)
        arr[i] = new int[w];
    for(int i = 0; i < l; i++)
        for(int j = 0; j < w; j++)
        {
            std::cin >> arr[i][j];
        }
}

int main()
{
    int num_trials;
    std::cin >> num_trials;
    for(int i = 0; i < num_trials; i++)
    {
        int l, w;
        std::cin >> l >> w;
        int ** arr;
        setup(arr, l, w);
        std::cout << "Case #" << i + 1 << ": ";
        if(Valid(arr, l, w))
            std::cout << "YES\n";
        else
            std::cout << "NO\n";
        delete[] arr;
    }
}