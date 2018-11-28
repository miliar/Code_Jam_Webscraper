#include <iostream>
#include <cmath>
#include <map>
using namespace std;

long insomnia(long N, long M, map<int, bool> *checkedDigits){
  if(N == 0)
    return -1;

  long remainder = N*M;
  int digit;

  while(remainder != 0.0){
    digit = remainder - 10*floor(remainder/10);
    remainder = floor(remainder/10);
   
    pair<map<int, bool>::iterator, bool> retval;
    retval = checkedDigits->insert(pair<int, bool>(digit, true));
    if(!retval.second && checkedDigits->size() == 10)
	break;
  }

  if(checkedDigits->size() == 10)
    return N*M;
  
  return insomnia(N, M+1, checkedDigits);
}

int main(){
	int t, n;
	cin >> t;
	map<long, long> alreadyChecked;
	map<int, bool> checkedDigits;
	int lastNumber;

	for(int i = 1; i <= t; ++i){
		cin >> n;
		checkedDigits.clear();

		map<long, long>::iterator found;
		found = alreadyChecked.find(n);
		if(found != alreadyChecked.end())
		  lastNumber = found->second;
		else{
		  lastNumber = insomnia(n, 1, &checkedDigits);
		  alreadyChecked.insert(pair<long, long>(n, lastNumber));
		}

		  cout << "Case #" << i << ": ";
		if(lastNumber == -1)
		  cout << "INSOMNIA" << endl;
		else
		  cout << lastNumber << endl;
		    
	}

}
