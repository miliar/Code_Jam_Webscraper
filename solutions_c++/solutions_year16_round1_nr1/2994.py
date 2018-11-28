#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <string>


using namespace std;

string sor(string in)
{
    string ret = string(1,in.front());
    reverse(in.begin(),in.end());
    in.pop_back();
    char temp;
    while(in.size() > 0)
    {
        temp = in.back();
        if(temp < ret.front())
        {
            ret = ret + string(1,temp);
        }
        else
        {
            ret = string(1,temp) + ret;

        }
        in.pop_back();
    }
    return ret;
}


int main()
{
    int times;
    cin >> times;
    string in;
    string out;
    for(int i = 0; i < times;i++)
    {
        cin >> in;
        out = sor(in);
        cout << "Case #" << i+1<< ": " << out << endl;
    }

}
