#include <iostream>
#include <string>
#include <set>

using namespace std;


struct tcase
{
    int answer1;
    int arrangement1[16];
    int answer2;
    int arrangement2[16];
};

struct result
{
    int rejectCount;
    int answer;
};

void addRow(const int* data, int row, set<int>& s, result& r)
{
    int first = row * 4;
    int end = first + 4;
    for (int i = first; i < end; ++i)
    {
        if (!s.insert(data[i]).second)
        {
            ++r.rejectCount;
            r.answer = data[i];
        }
    }
}


result solve(const tcase& tc)
{
    result r = {0,0};
    set<int> s;
    addRow(tc.arrangement1,tc.answer1-1,s,r);
    addRow(tc.arrangement2,tc.answer2-1,s,r);
    return r;
}

void getarr(int* arr)
{
    for (int i = 0; i < 16; i++)
    {
        cin >> arr[i];
        if ((i+1)%4==0)
        {
            string dummy;
            getline(cin,dummy);
        }
    }
}

int main (int argc, char* argv[])
{
    int N = 0;
    string dummy;
    cin >> N;
    getline(cin,dummy);

    for (int i = 0; i < N; ++i)
    {
        tcase tc;
        cin >> tc.answer1;
        getline(cin,dummy);
        getarr(tc.arrangement1);
        cin >> tc.answer2;
        getline(cin,dummy);
        getarr(tc.arrangement2);

        result r = solve(tc);
        cout << "Case #" << i+1 << ": ";
        switch (r.rejectCount)
        {
        case 0:
            cout << "Volunteer cheated!";
            break;
        case 1:
            cout << r.answer;
            break;
        default:
            cout << "Bad magician!";
            break;
        }
        cout << endl;
    }

    return 0;
}

