#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <string>


using namespace std;

int main()
{
    int taille;

    std::vector<string> data;
    vector<int> result;
    string temp;
    int cpt;

    cin >> taille;

    for (int i = 0; i < taille; i++)
    {
        cin >> temp;
        data.push_back(temp);
    }

    for(int i = 0; i < taille; i++)
    {
        temp = data[i];
        cpt = 0;
        for(int j = data[i].size(); j >= 0; j--)
        {
            if(temp[j] == '-')
            {
                for(int k = 0; k <= j; k++)
                {
                    if(temp[k] == '-')
                        temp.replace(k, 1, "+");
                    else
                        temp.replace(k, 1, "-");
                }
                cpt++;
            }
        }
        result.push_back(cpt);
    }

    for(int i = 0; i < result.size(); i++)
    {
        std::cout << "Case #" << i + 1 << ": " << result[i] << std::endl;
    }
}
