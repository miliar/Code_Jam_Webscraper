#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    ifstream fin("shy.in");
    ofstream fout("shy.out");
    int cases,max_shyness,standing,added;
    fin >> cases;
    string s_people;
    for(int i=1;i<=cases;i++)
    {
        fin >> max_shyness;
        getline(fin,s_people);
        s_people.erase(0,1);
        standing=s_people[0]-48;
        added=0;
        for(int z=1;z<=max_shyness;z++)
        {
            if(standing<z)
            {
                added+=z-standing;
                standing=z;
            }
            standing+=s_people[z]-48;
        }
        fout << "Case #" <<  i << ": " << added << "\n";
    }
    return 0;
}
