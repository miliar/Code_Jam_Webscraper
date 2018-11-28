#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;


int checker (vector<int> & v1, vector<int> & v2)
{
    int count=0;

    for (int i=0; i<v1.size(); i++)
    {
        for (int j=0; j<v2.size(); j++)
        {
            if (v1[i] == v2[j])
                count++;
        }
    }


    return count;

}

int that_one (vector<int> & v1, vector<int> & v2)
{
    for (int i=0; i<v1.size(); i++)
    {
        for (int j=0; j<v2.size(); j++)
        {
            if (v1[i] == v2[j])
                return v1[i];
        }
    }
}

int main ()
{
    ifstream in("A-small-attempt1.in");
    ofstream out("output.txt");
    int T;
    in >> T;

    int a1;
    int a2;
    vector<int> row_1(4);
    vector<int> row_2(4);

    vector<int> result(T);
    vector<int> number(T);


    for (int j=0; j<T; j++)
    {

        in >> a1;
        for (int i=0; i<a1; i++)
        {
            in.ignore(9999,'\n');
        }
        for (int i=0; i<4; i++)
        {
            in >> row_1[i];
        }
        for (int i=0; i<5-a1; i++)
        {
            in.ignore(9999,'\n');
        }

        in >> a2;

        for (int i=0; i<a2; i++)
        {
            in.ignore(9999,'\n');
        }
        for (int i=0; i<4; i++)
        {
            in >> row_2[i];
        }
        for (int i=0; i<5-a2; i++)
        {
            in.ignore(9999,'\n');
        }


        result[j] = checker(row_1, row_2);
        if (result[j] == 1)
        {
            number[j] = that_one(row_1, row_2);
        }
        else
            number[j] = 0;

    }

    for (int j=0; j<T; j++)
    {
        out << "Case #" << j+1 << ": ";
        if (result[j] == 0)
        {
            out << "Volunteer cheated!" << endl;
        }
        else if (result[j] == 1)
        {
            out << number[j] << endl;
        }
        else if (result[j] > 1)
        {
             out << "Bad magician!" << endl;
        }
    }

}
