#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <assert.h>
#include <queue>
#include <sstream>
#include <iomanip>

using namespace std;

bool officialprint=true;

std::vector<int> sCount;

int totalPeopleCount=0;
int smax;

int solve()
{
  int countPeople=0;

  int peopleNeeded=0;

  for (int s=0; s<=smax; ++s) {
    if (!officialprint) cout << "s: "<< s << " countPeople: "<< countPeople << " peopleNeeded: " << peopleNeeded << endl;

    int moreFriends=0;
    if (countPeople < s) {
       moreFriends = s - countPeople;
    }
    peopleNeeded += moreFriends;

    countPeople += sCount[s] + moreFriends;

    if (!officialprint) cout << "  s: "<< s << " countPeople: "<< countPeople << " peopleNeeded: " << peopleNeeded << endl;
  }

  return peopleNeeded;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;
  
  //  if (!officialprint)  cout << "Number of cases: " << numCases << endl;

  for (int c=0; c<numCases; ++c) {
    i >> smax;

    string bla;
    i >> bla;

    sCount.clear();
    sCount.resize(smax+1);

    assert(bla.size() <= smax+1);

    totalPeopleCount = 0;

    for (int c=0; c<bla.size(); ++c) {
      sCount[c] = int(bla[c] - '0');
      totalPeopleCount += sCount[c];
      if (!officialprint) cout << " Number of people with shyness " << c << " : " << sCount[c] << endl;
    }
    
    int answer = solve();
    cout << "Case #" << c+1 << ": " << answer << endl;
  }

  return true;
}




int main(int argv, char* argc[])
{
  if (argv < 2) {
    cout << "Usage " << argc[0] << " <inputFile>" << endl;
    exit(1);
  }

  ifstream filei(argc[1]);

  if (!readFile(filei)) {
    cout << "Couldn't parse file " << argc[1] << endl;
    exit(1);
  }

  //    for (long int d=0; d<100; ++d) {
  //      for (long int b=0; b<100; ++b) {
  //        cout << "d: " << d << " b: " << b << endl;
  //
  //        long int ff = f(d,b);
  //        long int hh = h(d,b);
  //        
  //        cout << "f: " << ff << " h: " << hh << endl;
  //
  //        assert(ff == hh);
  //
  //
  //        cout << setw(4) << h(d,b) << " ";
  //      }
  //      cout << endl;
  //    }

  //  cout << "********************" << endl;
  //
  //  cout << "h(5,2) = " << h(5,2) << endl;
  //
  //  cout << "********************" << endl;
  //
  //  cout << "h(5,3) = " << h(5,3) << endl;

  return 0;
}
