#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <string>
#include <cstdlib>


using namespace std;

bool toutChiffres(vector<bool>& m)
{
    for(int i = 0; i < m.size(); i++)
    {
        if(m[i] == false)
            return false;
    }
    return true;
}

void marqueChiffre(vector<bool>& m, string& nombre)
{
    char c;
    for(int i = 0; i < nombre.size(); i++)
    {
        c = nombre[i];
        m[nombre[i] - '0'] = true;
    }
}

int main()
{
    int n = 1;
    int taille;
    int temp;
    char buffer[256];
    std::vector<int> data;
    vector<int> result;
    std::vector<bool> marque(10, false);
    string nombre;

    cin >> taille;

    for (int i = 0; i < taille; i++)
    {
        cin >> temp;
        data.push_back(temp);
    }


    for(int i = 0; i < taille; i++)
    {
        n = 1;
        for(int j = 0; j < 10; j++)
            marque[j] = 0;

        if(data[i] == 0)
            result.push_back(-1);
        else
        {
            while(!toutChiffres(marque))
            {
                temp = data[i] * n;
                itoa(temp, buffer, 10);
                nombre = buffer;
                marqueChiffre(marque, nombre);
                n++;
            }
            result.push_back(data[i] * (n - 1));
        }
    }


    for(int i = 0; i < result.size(); i++)
    {
        if(result[i] != -1)
            std::cout << "Case #" << i + 1 << ": " << result[i] << std::endl;

        else
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
    }
}
