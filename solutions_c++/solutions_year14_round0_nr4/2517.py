#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <string>
#include <sstream>
#include <map>
#include <limits>
#include <cmath>

using namespace std;

int maximizeWin(int n, deque<double> oponnent, deque<double> player)
{
	int wins = 0;
    for(int i = 0;i < n;i++){
        //round
        if(oponnent.back() > player.back()){
//            cout << "putting player- " << player.front() << " vs opponent- " << oponnent.back() << endl;
            //ken has the biggest number
            //better deal with it by losing my smallest number
            player.pop_front();
            oponnent.pop_back();
        }else{
//            cout << "putting Player- " << player.back() << " vs opponent- " << oponnent.back() << endl;
            player.pop_back();
            oponnent.pop_back();
            wins++;
        }
    }

    return wins;
}

int main() {

	int cases;
	cin>>cases;
	for (int k = 1; k<=cases; k++) {

		int n;

		cin>>n;
		deque<double> naomi(n);
		deque<double> ken(n);
		for (int i = 0; i<n; i++) {
			double temp;
			cin>>temp;
			naomi[i] = temp;
		}
		for (int i = 0; i<n; i++) {
			double temp;
			cin>>temp;
			ken[i] = temp;
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int newWins, oldWins;
		newWins = maximizeWin(n, ken, naomi);
		oldWins = n-maximizeWin(n, naomi, ken);


		cout<<"Case #"<<k<<":"<<" "<<newWins<<" "<<oldWins<<endl;
	}
	return 0;
}

