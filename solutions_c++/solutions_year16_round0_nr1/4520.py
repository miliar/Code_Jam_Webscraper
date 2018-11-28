#include <iostream>
#include <sstream>
using namespace std;

int main()
{
    stringstream ss;
    int tt;
    cin >> tt;
    string lol;
    bool b[10] = {false};
    for(int t = 0;t<tt;t++)
    {
        long long num;
        cin >> num;
        long long orig = num;
        while(1)
        {
            if(num == 0)
            {
                cout << "Case #" << t+1 << ": INSOMNIA" << endl;
                break;
            }
           // cout << "Num:" <<num <<endl;
            ss << num;
            ss >> lol;
            //cout <<lol <<endl;
            ss.clear();
            int j = 0;
            while(j<lol.size())
            {
                b[(int)lol[j]-48] = true;
                j++;
            }
            bool ends = true;
            for(int i = 0;i<10;i++)
            {
                ends &= b[i];
            }
            if(ends)
            {
                cout << "Case #" << t+1 << ": "<<num << endl;
                for(int i=0;i<10;i++)
                {
                    b[i] = false;
                }
                break;
            }
            num += orig;
        }
    }


}
