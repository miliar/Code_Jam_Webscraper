#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int i, int j);
int levelpancakes(vector<int> & plates);
bool pancakes_are_cuttable(const vector <int> & plates);
int cut_pancakes(vector <int> & plates);
void print_vector(const vector <int> & plates);

int main()
{
    ifstream fin("b.in");
    ofstream fout("b.out");
    
    int cases;
    int current_case = 1;
    fin >> cases;
    while(current_case <= cases)
    //while(true)
    {
        int diners_with_pancakes;
        fin >> diners_with_pancakes;
        //cin >> diners_with_pancakes;
        vector<int> plates;
        for(int i = 0; i < diners_with_pancakes; i++)
        {
            int pancakes;
            fin >> pancakes;
            //cin >> pancakes;
            plates.push_back(pancakes);
        }
        
        sort(plates.begin(), plates.end(), compare);
        //now it will take plates[0] minutes to eat with no magic minutes
        //we need to level out these pancakes for maximum eating efficiency
        int minutes = levelpancakes(plates);
        cout << "Case #" << current_case << ": " << minutes << endl;
        fout << "Case #" << current_case << ": " << minutes << endl;
        current_case++;
    }
    fin.close();
    fin.close();
    return 0;
}

bool compare(int i, int j)
{
    return i > j;
}

int levelpancakes(vector<int> & plates)
{
    //The highest stacks of pancakes need to be cuttable so chop the highest stacks
    int magic_minutes = 0;
    cout << "____________________" << endl;
    while(pancakes_are_cuttable(plates))
    {   
        print_vector(plates);
        cout << " is cutable " << endl;
        magic_minutes += cut_pancakes(plates);
        sort(plates.begin(), plates.end(), compare);
        print_vector(plates);
        cout << " after cut " << endl << endl;
        
    }
    
    return plates[0] + magic_minutes;
}

bool pancakes_are_cuttable(const vector <int> & plates)
{
    int maxes = 1;
    int minmax = plates[0];
    int i = 0;
    while(i < plates.size() - 1 && plates[i] <= plates[i+1]+1)
    {
        maxes++;
        i++;
        minmax = plates[i];
    }
    
    print_vector(plates);
    cout << "maxes = " << maxes << endl;
    
    // a magic minute will save time if we can reduce max stack by (maxes + 1)
    //but the pancakes we are reducing are <= min max - 2
    if((maxes+1) <= plates[0] / 2 )
        return true;
    else
        return false;
}

int cut_pancakes(vector <int> & plates)
{
    int maxes = 1;
    int minmax = plates[0];
    int i = 0;
    while(i < plates.size()-1 && plates[i] <= plates[i+1]+1)
    {
        maxes++;
        i++;
        minmax = plates[i];
    }
	int max_after_split;
	if (plates.size() == 1 || i + 1 == plates.size())
	{
		max_after_split = 0;
	}
	else
		max_after_split = plates[i + 1];
	int ideal_cut = plates[0] / 2;

	//multiple 9's is bad
	//max after split >= 7 is bad
	//max after split == 6 is good if the 6 can be split
	//max after split == 5 is good if the 5 can be split
	//max after split == 4 is good 
	//max after split == 3 is ideal
	vector<int> temp = plates;
	temp.erase(temp.begin());
	if (maxes == 1 && plates[0] == 9 && (max_after_split < 5 || (max_after_split < 7 && pancakes_are_cuttable(temp))))
	{
		//there is a special case 9 to deal with in spot 0
		plates[0] = 3;
		plates.push_back(3);
		plates.push_back(3);
		return 2;	//only special split the 9
	}
		
    for(int j = 0; j < maxes; j++)
    {
		ideal_cut = plates[j] / 2;
        plates[j] -= ideal_cut;
        plates.push_back(ideal_cut);
    }
    return maxes;
}

void print_vector(const vector <int> & plates)
{
    for(int i = 0; i < plates.size(); i++)
    {
        cout << plates[i] << " ";
    }
    cout << endl;
}
