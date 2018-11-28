#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ifstream fin("A-large.in");

    int T=0;
    fin >> T;

    ofstream fout("outputAlarge.txt");
    for (int i=0; i<T; i++) {
        int Smax;
        fin >> Smax;

        vector<char> people(Smax+1);
        for (int j=0; j<=Smax; j++) {
            char numAtj;
            fin >> numAtj;

            people[j] = numAtj;
        }

        //if all have at least 1, 0 needed
        //if sum of people of shyness 0 to m is equal or greater than next person's shyness n(>m) for all n then 0 needed
        //if sum of people of shyness 0 to m is less than next person's shyness n(>m) then total-n people are needed

        int needed = 0;
        int total = 0;
        for (int j=0; j<=Smax; j++) {
            if (total < j) {
                needed += j-total;
                total += j-total;
            }
            total += (people[j] - '0');
        }

        cout << "Case #" << i+1 << ": " << needed << "\n";
        fout << "Case #" << i+1 << ": " << needed << "\n";
    }
    fin.close();
    fout.close();

    return 0;
}
