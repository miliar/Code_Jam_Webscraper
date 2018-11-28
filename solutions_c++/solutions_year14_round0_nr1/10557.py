#include <fstream>
#include <iterator>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

int main(int argc, char **argv)
{
    using namespace std;

    if(argc != 2)
	exit(1);

    FILE *fp;
    fp = fopen(argv[1], "r");

    if(!fp)
	exit(2);
    
    int count = 0;
    fscanf(fp, "%d\n", &count);

    for(size_t i = 0; i < count; ++i)
    {
	int first_row = 0;
	int m_one[4][4];

	fscanf(fp, "%d\n", &first_row);
	for(size_t i = 0; i < 4; ++i)
	    fscanf(fp, "%d %d %d %d\n", &m_one[i][0], &m_one[i][1], &m_one[i][2], &m_one[i][3]);

	int second_row = 0;
	int m_two[4][4];

	fscanf(fp, "%d\n", &second_row);
	for(size_t i = 0; i < 4; ++i)
	    fscanf(fp, "%d %d %d %d\n", &m_two[i][0], &m_two[i][1], &m_two[i][2], &m_two[i][3]);

	
	set<int> one;
	set<int> two;
	vector<int> intersection;

	int *row_one = &m_one[first_row - 1][0];
	int *row_two = &m_two[second_row - 1][0];

	for(size_t i = 0; i < 4; ++i)
	{
	    one.insert(*row_one++);
	    two.insert(*row_two++);
	}

	set_intersection(one.begin(), one.end(), two.begin(), two.end(),
			 inserter(intersection, intersection.end()));

	size_t s = intersection.size();
	if(s == 1)
	{
	    cout << "Case #" << (i+1) << ": " << *intersection.begin() << "\n";
	}
	else if(s > 1 && s <= 4)
	{
	    cout << "Case #" << (i+1) << ": Bad magician!\n";
	}
	else
	{
	    cout << "Case #" << (i+1) << ": Volunteer cheated!\n";
	}
    }

    return 0;
}
