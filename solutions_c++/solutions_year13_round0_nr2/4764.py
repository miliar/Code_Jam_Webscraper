#include <iostream>

using namespace std;
int RowCount,ColCount;
int** garden;

bool checkRow(int val,int i)
{
    if (val>100)
        return false;
    for(int j=0;j<ColCount;j++)
        if(garden[i][j]>
           val)
            return false;
    return true;
}

bool checkCol(int val,int j)
{
    if (val>100)
        return false;
    for(int i=0;i<RowCount;i++)
        if(garden[i][j]>val)
            return false;
    return true;
}

void freeze()
{
    for(int i=0;i<RowCount;i++)
        delete[] garden[i];
    delete[] garden;
}
int submain()
{
    cin >> RowCount >> ColCount;
    garden=new int*[RowCount];
    for(int i=0;i<RowCount;i++)
    {
        garden[i]=new int[ColCount];
        for(int j=0;j<ColCount;j++)
            cin>>garden[i][j];
    }
    for(int i=0;i<RowCount;i++)
        for(int j=0;j<ColCount;j++)
            if(!checkRow(garden[i][j],i) && !checkCol(garden[i][j],j))
            {
                cout << "NO" << endl;
                freeze();
                return 0;
            }
    freeze();
    cout << "YES" << endl;
    return 0;
}

int main()
{
    int c;
    cin >> c;
    for(int i=1;i<=c;i++)
    {
        cout << "Case #" << i << ": ";
        submain();
    }
    return 0;
}
