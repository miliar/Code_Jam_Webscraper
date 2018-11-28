#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>

using namespace std;


int main()

{
    freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int temp[] = {0,1,2,3,4,5,6,7,8,9};
	vector <int> digits(temp,temp+10);
    int T,N,i = 0;
    cin >> T;
	for (int caseN = 1; caseN <= T; ++caseN) {
		cin >> N;
		digits.assign(temp,temp+10);
		if (N == 2 * N) {
			cout << "Case #" << caseN << ": INSOMNIA" << endl;
			continue;
		}
		else {
		i = 1;
			while(digits.size()>=1){
				int copyN=i*N;
				while(copyN>0){
					digits.erase(remove(digits.begin(),digits.end(),copyN%10), digits.end());
					copyN/=10;
				}
				i++;			
			}
		}
		cout << "Case #" << caseN << ": " << (i-1)*N << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;

}
