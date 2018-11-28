#include <fstream>

using namespace std;

int main()
{
    ifstream in("standingovation.in");
    ofstream out("standingovation.out");

    int t;
    in>>t;

    for(int c=0;c<t;c++)
    {
        int smax;
        string people;

        in>>smax>>people;

        int stand = 0, added=0;
        for(int i=0;i<=smax;i++)
        {
            if(i>stand+added && people[i]-'0'!=0)
                added+=i-stand;
            stand+=people[i]-'0';
        }
        out<<"Case #"<<c+1<<": "<<added<<endl;
    }
}
