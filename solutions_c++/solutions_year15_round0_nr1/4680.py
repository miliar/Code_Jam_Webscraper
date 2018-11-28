#include <iostream>
#include <fstream>
#include <string>
#include <vector>


using namespace std;

struct person
{
    int shyness_level;
    int population;
    
    person(int s, int p)
    {
        shyness_level = s;
        population = p;
    }
};

int sum_lower_levels(vector <person *> audience, int level);

int main()
{
    ifstream fin("a.in");
    ofstream fout("a.out");
    int cases;
    fin >> cases;
    
    int current_case = 1;
    while(current_case <= cases)
    {
        int max_shyness; // 0 to 1000
        fin >> max_shyness;
        
        string data;
        fin >> data;
        vector < person * > audience;
        for(int i = 0; i < data.length(); i++)
        {
            person * temp = new person(i, data[i] - 0x30);
            audience.push_back(temp);
        }
        //sum the people in shyness levels 0 -> n-1 is > n for 0 < n < max_shyness
        int standing_people = 0;
        int people_added = 0;
        for(int i = 0; i < audience.size(); i++)
        {
            int sum = sum_lower_levels(audience, i);
            if(sum < i)
            {
                audience[i-1]->population += (i - sum);
                people_added += (i - sum);
            }
        }
        
        fout << "Case #" << current_case << ": " << people_added << endl;
        current_case += 1;
    }
    return 0;
}

int sum_lower_levels(vector <person *> audience, int level)
{
    int sum = 0;
    for(int i = 0; i < level; i++)
    {
        sum += audience[i]->population;
    }
    return sum;
}
