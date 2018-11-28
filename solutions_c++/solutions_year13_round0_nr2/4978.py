#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void RemoveRow(int * mat, int & nrow, int & ncol, int irow)
{
    for(int i = irow*ncol; i < (nrow-1)*ncol; i++)
        mat[i] = mat[i+ncol];
    nrow --;
}

void RemoveCol(int * mat, int & nrow, int & ncol, int jcol)
{
    for(int i = 0; i < nrow; i++)
    {
        for(int j = 0; j < ncol-1; j++)
        {
            int j2 = j<jcol?j:j+1;
            mat[i*(ncol-1)+j] = mat[i*ncol+j2];
        }
    }
    ncol --;
}

void PrintMat(int * mat, int nrow, int ncol)
{
    for(int i = 0; i < nrow; i++)
    {
        for(int j = 0; j < ncol; j++)
            cout << " " << mat[i*ncol+j];
        cout << endl;
    }
}

bool IsRow(const int * mat, int nrow, int ncol, int irow, int h)
{
    for(int i = irow*ncol; i < (irow+1)*ncol; i++)
        if(mat[i] != h)
            return false;
    return true;
}

bool IsCol(const int * mat, int nrow, int ncol, int jcol, int h)
{
    for(int i = jcol; i < nrow*ncol; i+=ncol)
        if(mat[i] != h)
            return false;
    return true;
}

bool DoOnce(int * mat, int & nrow, int & ncol, int h)
{
    vector<int> stack;
    for(int i = 0; i < nrow; i++)
    {
        if(IsRow(mat, nrow, ncol, i, h))
            stack.push_back(i);
    }
    while(stack.size())
    {
        RemoveRow(mat, nrow, ncol, stack.back());
        stack.pop_back();
    }

    for(int i = 0; i < ncol; i++)
    {
        if(IsCol(mat, nrow, ncol, i, h))
            stack.push_back(i);
    }
    while(stack.size())
    {
        RemoveCol(mat, nrow, ncol, stack.back());
        stack.pop_back();
    }

    return find(mat, mat+nrow*ncol, h) == mat+nrow*ncol;
}

int MatMax(const int * mat, int nrow, int ncol)
{
    int m = -1;
    for(int i = 0; i < nrow*ncol; i++)
        if(mat[i] > m)
            m = mat[i];
    return m;
}

int main()
{
    int * mat = new int[10000];

    int T;
    cin >> T;
    for(int k = 0; k < T; k++)
    {
        int N,M;
        cin >> N >> M;
        for(int i = 0; i < N*M; i++)
            cin >> mat[i];
        bool r = true;
        for(int h = 1; h < MatMax(mat, N, M); h++)
        {
            r = DoOnce(mat, N, M, h);
            if(r == false)
                break;
        }
        if(r)
            cout << "Case #" << k+1 << ": " << "YES" << endl;
        else
            cout << "Case #" << k+1 << ": " << "NO" << endl;
    }

    delete[] mat;
    return 0;
}
