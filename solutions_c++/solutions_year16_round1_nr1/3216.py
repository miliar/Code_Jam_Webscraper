#include <fstream>
#include<deque>
using namespace std;

int main()
{
    fstream fin;
    fstream fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
    deque<char> qu;
    int t,i;
    fin>>t;
    string s;
    for(i=1;i<=t;i++)
    {
        fout<<"Case #"<<i<<": ";
        fin>>s;
        qu.push_back(s[0]);
        for(int j=1;j<s.size();j++)
        {
            if(s[j]>=qu.front())
                qu.push_front(s[j]);
            else
                qu.push_back(s[j]);
        }
        for (std::deque<char>::iterator it = qu.begin(); it!=qu.end(); ++it)
            fout << *it;
        fout<<endl;
        qu.clear();
    }

    return 0;
}
