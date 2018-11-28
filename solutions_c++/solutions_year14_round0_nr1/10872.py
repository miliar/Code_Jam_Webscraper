#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void read_2Dvector(vector< vector<int> > &a)
{
    for(int i = 0; i < a.size(); i++)
    {
        for(int j = 0; j < (a.at(i)).size(); j++)
            cin >> (a.at(i)).at(j) ;
    }
}

void findCard(int case_number)
{
    int row1, row2, answer, count = 0;
    vector< vector<int> > argmnt(4, vector<int>(4, 0));
    vector<int> myrow1(4, 0);  vector<int> myrow2(4, 0);

    cin >> row1;
    read_2Dvector(argmnt);
    myrow1 = argmnt.at(row1-1);
    //sort(myrow1.begin(), myrow1.end());

    cin >> row2;
    read_2Dvector(argmnt);
    myrow2 = argmnt.at(row2-1);
    //sort(myrow2.begin(), myrow2.end());

    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            if(myrow1.at(i) == myrow2.at(j))
            {
                answer = myrow1.at(i);
                count++;
            }
        }
    }

    cout << "Case #" << case_number << ": ";
    if(count == 1)
    {
        cout << answer;
    }
    else if(count == 0)
    {
        cout << "Volunteer cheated!";
    }
    else if(count > 1)
    {
        cout << "Bad magician!";
    }
    cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        findCard(i);
    }
    return 0;
}
