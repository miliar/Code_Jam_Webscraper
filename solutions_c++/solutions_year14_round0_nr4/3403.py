#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void
print_vector(vector<double> v)
{
  int i;
  for (i=0;i<v.size();i++)
    cout << v[i] << endl;
}

int main()
{
  int numberOfTestCases=0;
  int maxTestCases=0;
  int N=0;
  int dSteps;
  int wSteps;

  vector<double> naomiWeights;
  vector<double> kenWeights;
  vector<double> naomiWeightscpy;
  vector<double> kenWeightscpy;

  int i,j,k;

  double input;

  cin >> maxTestCases;

  while(numberOfTestCases != maxTestCases) {
    numberOfTestCases++;

    cin >> N;

    naomiWeights.clear();
    kenWeights.clear();
    naomiWeightscpy.clear();
    kenWeightscpy.clear();

    for(i=0;i<N;i++) {
      cin >> input;
      naomiWeights.push_back(input);
    }

    for(i=0;i<N;i++) {
      cin >> input;
      kenWeights.push_back(input);
    }

//     print_vector(naomiWeights);
//     print_vector(kenWeights);

    sort(naomiWeights.begin(), naomiWeights.end());
    sort(kenWeights.begin(), kenWeights.end());

    //    cout << "naomiWeights: ";
    //    print_vector(naomiWeights);
    //    cout << "kenWeights: ";
    //    print_vector(kenWeights);

    naomiWeightscpy = naomiWeights;
    kenWeightscpy = kenWeights;

    dSteps=N;
    for(i=0;i<naomiWeights.size();i++) {
      for(j=0;j<kenWeights.size();j++)
	if (kenWeights[j] > 0) {
	  if (kenWeights[j] > naomiWeights[i]) {
	    for (k=kenWeights.size() - 1; k >=j; k--) {
	      if (kenWeights[k] > 0) {
		kenWeights[k] = -1;
		break;
	      }
	    }
	    dSteps--;
	  } else {
	    kenWeights[j] = -1;
	  }
	  break;
	}
    }

    wSteps=N;
    for(i=0;i<naomiWeightscpy.size();i++) {
      for (j=0;j<kenWeightscpy.size();j++) {
	if (kenWeightscpy[j] > 0 && kenWeightscpy[j] > naomiWeightscpy[i]) {
	  kenWeightscpy[j] = -1;
	  wSteps--;
	  break;
	}
      }
	
    }

    cout << "Case #" << numberOfTestCases << ": " << dSteps << " " << wSteps << endl;
  }

  return 0;
}

    
