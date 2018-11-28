#include <iostream>
#include <cstdio>
// #include <fstream>
// #include <cstdlib>
#include <vector>

#define forn(i, n) for(int i = 0; i < n; i++)

using namespace std;

typedef vector<int> vint;
typedef vector<vint> vvint;

struct s_4_neighbours
{
	int left;
	int right;
	int up;
	int down;
};

int get_left_neighbour(vvint& lawn, int i, int j)
{
	int value = lawn[i][j];
	// j--;
	while (j >= 0 and lawn[i][j] == value)
	{
		j--;
	}

	return lawn[i][max(0, j)];
}

int get_right_neighbour(vvint& lawn, int i, int j, int m)
{
	int value = lawn[i][j];
	
	while (j < m and lawn[i][j] == value)
	{
		j++;
	}
	return lawn[i][min(m - 1, j)];
}

int get_upper_neighbour(vvint& lawn, int i, int j)
{
	int value = lawn[i][j];
	
	while (i >= 0 and lawn[i][j] == value)
	{
		i--;
	}
	return lawn[max(0, i)][j];
}

int get_lower_neighbour(vvint& lawn, int i, int j, int n)
{
	int value = lawn[i][j];
	
	while (i < n and lawn[i][j] == value)
	{
		i++;
	}
	return lawn[min(n - 1, i)][j];
}

void get_neighbours(vvint& lawn, int i, int j, int n, int m, s_4_neighbours& neighbours)
{
	neighbours.left = get_left_neighbour(lawn, i, j);
	neighbours.right = get_right_neighbour(lawn, i, j, m);
	neighbours.up = get_upper_neighbour(lawn, i, j);
	neighbours.down = get_lower_neighbour(lawn, i, j, n);
}

// bool is_border(int i, int j, int n, int m)
// {
	// return ((i == 0) or (i == n - 1) or (j == 0) or (j == m - 1))
// }

bool has_bigger_neighbours(vvint& lawn, int i, int j, int n, int m)
{
	int value = lawn[i][j];
	s_4_neighbours neighbours;
	get_neighbours(lawn, i, j, n, m, neighbours);
	
	// forn(k, 4)
	// {
		// if (neighbours[k] > value)
		// {
			// result ++;
		// }
	// }
	bool result = false;
	bool horizontal = ((neighbours.left > value) or (neighbours.right > value));
	bool vertical = ((neighbours.up > value) or (neighbours.down > value));

	// cout << i << " " << j << "  " << value << " - ";
	// cout << neighbours.left << " " << neighbours.right << " " << neighbours.up << " " << neighbours.down << "  ";
	// cout << (neighbours.left > value) << " " << (neighbours.right > value) << " ";
	// cout << (neighbours.up > value) << " " << (neighbours.down > value) << "  ";
	// cout << horizontal << " " << vertical << endl;

	// if ((neighbours.left > value and vertical) or (neighbours.right and vertical))
	// {
		// result = false;
	// }

	if ((horizontal) and (vertical))
	{
		result = true;
		// cout << "aaa";
	}

	/* Check for borders. */
	// if ((is_border(i, j, n, m)) and (horizontal or vertical))
	// {
	// 	result = true;
	// }

	// bool result = not(horizontal and vertical);

	return result;
}

int main(void)
{
	// ifstream cin("B-small-attempt0.in");
	// ofstream cout("B-small-attempt0.out");
	
	int casos;
	cin >> casos;    
  
	forn(caso, casos)
	{
		int n, m;
		cin >> n >> m;

		vvint lawn (n, vint(m, 0));

		forn(i, n)
		{
			forn(j, m)
			{
				cin >> lawn[i][j];
			}
		}

		/* Check if a position has two neighbours that are higher. */
		bool result = true;

		forn(i, n)
		{
			forn(j, m)
			{	
				// cout << i << " " << j << "  " << lawn[i][j] << "   " << count_bigger_neighbours(lawn, i, j, n, m) << endl;				
				if (has_bigger_neighbours(lawn, i, j, n, m))
				{
					result = false;
					// break;
				}
			}
			// cout << endl;
		}
        
    cout << "Case #" << caso + 1 << ": ";
    // cout << "  n: " << n << " m: " << m << "   ";
    
    if (result)
    {
    	cout << "YES" << endl;
    }
    else
    {
    	cout << "NO" << endl;
    }
	}

	return 0;
}