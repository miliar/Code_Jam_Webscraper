#include <iostream>
#include <vector>

using namespace std;

const unsigned int HORIZONTAL = 0;
const unsigned int VERTICAL   = 1;

bool isFeasible(const vector<vector<unsigned int> >& field);

/*
template <class T>
void printMatrix(const vector<vector<T> >& field) {
  cout <<"\nMATRIX:\n";
  for (unsigned i = 0; i < field.size(); ++i) {
    for (unsigned j = 0; j < field[0].size(); ++j) {
      cout << field[i][j] << " ";
    }
    cout <<" \n";
  }
}
*/

int main() {
  unsigned int T;

  // Read in # test cases
  cin >> T;
  for (unsigned int i = 1; i <= T; ++i) {
    // Read # rows and # cols
    unsigned int num_rows, num_cols;
    cin >> num_rows >> num_cols;

    // Initialize our field
    vector<vector<unsigned int> > field;
    for (unsigned int row = 0; row < num_rows; ++row) {
      vector<unsigned int> row_heights;
      for (unsigned int col = 0; col < num_cols; ++col) {
	unsigned int height;
	cin >> height;
	row_heights.push_back(height);
      }
      field.push_back(row_heights);
    }

    // Solve and print
    if (isFeasible(field)) {
      cout << "Case #" << i << ": YES\n";
    } else {
      cout << "Case #" << i << ": NO\n";
    }
  }

  return 0;
}

bool isFeasible(const vector<vector<unsigned int> >& field) {
  // Get back the # rows and # cols from the vector
  unsigned int num_rows = field.size();
  unsigned int num_cols = field[0].size();

  // Initialize a 2D vector of visited nodes
  vector<vector<bool> > isVisited;
  for (unsigned int i = 0; i < num_rows; ++i) {
    vector<bool> row;
    for (unsigned int j = 0; j < num_cols; ++j) {
      row.push_back(false);
    }
    isVisited.push_back(row);
  }

  // Start solving
  unsigned int modes[2] = {HORIZONTAL, VERTICAL};
  for (unsigned int mode = 0; mode < VERTICAL + 1; ++mode) {
    unsigned int i_max = (modes[mode] == HORIZONTAL) ? num_rows : num_cols;
    unsigned int j_max = (modes[mode] == HORIZONTAL) ? num_cols : num_rows;
    for (unsigned int i = 0; i < i_max; ++i) {
      unsigned int height = 0;
      unsigned int max_so_far = 0;

      // Keep track of (x, y) coordinates that we want to mark as visited
      vector<pair<unsigned int, unsigned int> > markAsVisited;
      for (unsigned int j = 0; j < j_max; ++j) {
	unsigned int row = (modes[mode] == HORIZONTAL) ? i : j;
	unsigned int col = (modes[mode] == HORIZONTAL) ? j : i;

	// Initialize at the first non-visited node
	if (isVisited[row][col] && height == 0) {
	  max_so_far = max(max_so_far, field[row][col]);
	  continue;
	}

	// Initialize
        if (height == 0) {
          height = field[row][col];
        }

	// Failure condition
	if (field[row][col] > height || field[row][col] < max_so_far) {
	  markAsVisited.clear();
	  break;
	} 

	// Mark visited node
	if (field[row][col] == height) {
	  markAsVisited.push_back(make_pair(row, col));
	}	
      }

      // Mark as appropriate
      unsigned int visitedCount = markAsVisited.size();
      for (unsigned int k = 0; k < visitedCount; ++k) {
	isVisited[markAsVisited[k].first][markAsVisited[k].second] = true;
      }
    }
  }

  // Count the # of visited nodes
  unsigned int count = 0;
  for (unsigned int i = 0; i < num_rows; ++i) {
    for (unsigned int j = 0; j < num_cols; ++j) {
      if (isVisited[i][j]) {
	++count;
      }
    }
  }

  // Success if all nodes are visited
  return count == num_rows * num_cols;
}
