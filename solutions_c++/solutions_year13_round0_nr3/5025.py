#include <iostream>
#include <vector>

using namespace std;

vector<int> fs_num;

bool is_pal(int i)
{
    if (i < 10)
        return true;
    else if (i < 100)
    {
        if ((i % 10) == ( i /10))
            return true;
        else return false;
    }
    else if (i < 1000)
    {
        if ((i % 10) == ( i /100))
            return true;
        else return false;
    }
    else if (i < 10000)
    {
        if ((i % 10) == ( i /1000))
        {
            if(((i/10) % 10) == ((i /100) % 10))
                return true;
            else
                return false;
        }
        else return false;
    }
}


void create_fs()
{
    for (int i = 1; (i * i) < 1001; i++)
        if (is_pal(i))
        {
            int sq = i*i;
            if (is_pal(sq))
                fs_num.push_back(sq);
        }
}

int main()
{
    create_fs();
    int l = fs_num.size();

    int t;
    cin >> t;
    for (int i =1; i < t+1; i++)
    {   
        int a,b;
        cin >> a >> b;
        int res = 0;
        if (a <= fs_num[l-1])
        {
            int j = -1;
            while(fs_num[++j] < a);
            while( (j <l) && (fs_num[j++] <= b))
                res++;

        }
        cout << "Case #" << i << ": " << res << endl;
    }
}
