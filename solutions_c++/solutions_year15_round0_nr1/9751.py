#include <iostream>
#include <fstream>

using namespace std;

int test_case, i, j, Smax, counter, required, a[7];
unsigned long int holder;

int main()
{

    void calc_ovation(int i);
    ifstream fin;
    fin.open("G:\\Codex\\A-small-attempt1.in");
    ofstream fout;
    fout.open("G:\\Codex\\Ovation_out.txt");
    fin>>test_case;
    for (i=0; i<test_case ; i++)
    {
    counter = 0;
    required = 0;
    fin>>Smax;
    fin>>holder;
    for(j=0; j<Smax+1; j++)
    {
        a[Smax-j] = holder%10;
        holder = holder/10;
    }

    for(j=0; j<Smax; j++)
    {
        counter+= a[j];
        if(counter < j+1 && a[j+1]!=0)
        {required += j+1 - counter;
        counter+=required;
        }
    }
    fout <<"Case #"<<i+1<<": ";
    fout << required;
    fout<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}

