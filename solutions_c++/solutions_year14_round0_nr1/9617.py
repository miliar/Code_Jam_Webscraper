#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cstdlib>
using namespace std;

void upisi_u_datoteku(int iteration, int same_number_counter, int number_counter)
{
    ofstream outfile;
    outfile.open("outfile.txt",ios::in | ios::out | ios::app);

    if(same_number_counter == 0)
    {

        outfile<<"Case #"<<iteration<<": "<<"Volunteer cheated!"<<endl;
    }
    else if(same_number_counter == 1)
    {
        outfile<<"Case #"<<iteration<<": "<<number_counter<<endl;
    }
    else
    {
         outfile<<"Case #"<<iteration<<": "<<"Bad magician!"<<endl;
    }
}

vector<string> vrati_vektor(string s)
{
    vector<string> vektor(4);
    string temp;
    istringstream iss;
    iss.str(s);

    int temp_count = 0;
    while(getline(iss, temp, ' '))
    {
        vektor[temp_count] = temp;
        temp_count ++;
    }

    return vektor;
}
//rjesavanje funkcije
void rijesi(int iteration, vector<string> first_vector, vector<string> second_vector)
{
    int same_numbers_counter = 0;
    int same_number = 0;
    for(int i=0; i<4; ++i)
    {
        int first_num = atoi(first_vector[i].c_str());
        for(int j=0; j<4; ++j)
        {
            int second_num = atoi(second_vector[j].c_str());

            if(first_num == second_num)
            {
                same_numbers_counter ++;
                same_number = first_num;
            }
        }
    }

    upisi_u_datoteku(iteration, same_numbers_counter, same_number);
}

//ucitavanje
void ucitaj()
{
    ifstream infile("to.in");

    string line;
    getline(infile, line);
    int test_counter = atoi(line.c_str());

    for(int i=1; i<=test_counter; i++)
    {
        getline(infile, line);
        int first_row_appearance = atoi(line.c_str());


        vector<string> first_vector;
        vector<string> second_vector;
        for(int j=1; j<=4; ++j)
        {
            getline(infile, line);
            if(first_row_appearance == j)
            {
                first_vector = vrati_vektor(line);
            }
        }

        getline(infile, line);
        int second_row_appearance = atoi(line.c_str());


        for(int j=1; j<=4; ++j)
        {
            getline(infile, line);
            if(second_row_appearance == j)
            {
                second_vector = vrati_vektor(line);
            }
        }

        rijesi(i, first_vector, second_vector);
    }
}


int main()
{
    ucitaj();

return 0;
}
