#include<iostream>
#include<deque>
#include<algorithm>
#include<cassert>
#include<iterator>
using std::cout;
using std::cin;
using std::endl;

typedef std::deque<double> weights_t;

// alpha is maximum assured win: naomi,s score
//beta is minimum assured loss: naomi,s score
// we are maximizing naomi's score
// positive color is naomi
/*
int conventional(weights_t& ken, weights_t& naomi, char naomiScore, char depth, signed char alpha, signed char beta, signed char color) {
	if (ken.size() == 1) {
		return color * ((*ken.begin() > *naomi.begin()) + naomiScore);
	}
	char bestValue = -60;
	
	//generating cihldren: 
	
}
*/


std::ostream& operator<<(std::ostream& out, const weights_t& w) {
	std::copy(w.begin(), w.end(), std::ostream_iterator<double>(out, " "));
	return out;
}


// try to minimize Naomi's losses
// if naomiLosses hits maxNaomiLosses, prune
// we will minimize maxNaomiLosses too
// assume that ken will always pick the lightest weight that beats naomi's, and his lightest weight otherwise
char conventional(weights_t& ken, weights_t& naomi, char naomiLosses, char fewestNaomiLosses) {
	if (naomiLosses >= fewestNaomiLosses) {
		//cout << "prune" <<endl;
		return fewestNaomiLosses;
	}

	char nBlocks = ken.size();	

	if (nBlocks == 1) {
		//cout << "terminal" << (int)(naomiLosses + (char)(*ken.begin() > *naomi.begin()))<<endl;
		return naomiLosses + (char)(*ken.begin() > *naomi.begin());
	}

	for (auto i = naomi.begin(); i != naomi.end(); ++i) {
		auto kenWeight = std::find_if(ken.begin(), ken.end(), [i](double k) {
			return k > (*i);
		});
		if (kenWeight != ken.end()) {
			++naomiLosses;
		}
		else {
			// dump lowest weight since ken loses
			kenWeight = ken.begin();
		}

		weights_t naomi2(nBlocks-1), ken2(nBlocks-1);
		// omit current naomi,s weight
		std::copy_if(naomi.begin(), naomi.end(), naomi2.begin(), [i](double n) { return n != (*i);} );
		// omit curent ken's weight
		std::copy_if(ken.begin(), ken.end(), ken2.begin(), [kenWeight](double k) {return k != (*kenWeight);} );
		char fullLosses = conventional(ken2, naomi2, naomiLosses, fewestNaomiLosses);
		fewestNaomiLosses = std::min(fullLosses, fewestNaomiLosses);
		//cout << "new fewest"<<(int)fewestNaomiLosses<<"over"<< (int)naomiLosses<<endl;
	}

	//cout << "out of children"<<(int)fewestNaomiLosses<<endl;
	return fewestNaomiLosses;
}

/*
the difference is now that naomi can basically choose which block ken puts out.

she can choose any block that is heavier than hers.
*/
/*
char deceitful(weights_t& ken, weights_t& naomi, char naomiLosses, char fewestNaomiLosses) {

	//cout << endl <<"fewest losses "<< (int) fewestNaomiLosses<<endl<<"N "<<naomi<<endl<<"K "<<ken<<endl;

	if (naomiLosses >= fewestNaomiLosses) {
		//cout << "prune" <<endl;
		return fewestNaomiLosses;
	}


	char nBlocks = ken.size();	

	if (nBlocks == 1) {
		//cout << "terminal" << (int)(naomiLosses + (char)(*ken.begin() > *naomi.begin()))<<endl;
		return naomiLosses + (char)((*ken.begin()) > (*naomi.begin()));
	}

	for (auto i = naomi.begin(); i != naomi.end(); ++i) {
		//go through all blocks heavier than naomi's
		auto heavyBegin = std::find_if(ken.begin(), ken.end(), [i](double k) {
			return k > (*i);
		});

		weights_t::iterator kenBegin, kenEnd;
		

		//none heavier: play the lightest as usual.
		if (heavyBegin == ken.end()) {
			kenBegin = ken.begin();
			kenEnd = 1+ken.begin();
}
		else {
			kenBegin = heavyBegin;
			kenEnd = ken.end();
			++naomiLosses;
			
		}




		for (auto kenWeight = kenBegin; kenWeight != kenEnd; ++kenWeight) {
				weights_t naomi2(nBlocks-1), ken2(nBlocks-1);
				// omit current naomi,s weight
				std::copy_if(naomi.begin(), naomi.end(), naomi2.begin(), [i](double n) { return n != (*i);} );
				// omit curent ken's weight
				std::copy_if(ken.begin(), ken.end(), ken2.begin(), [kenWeight](double k) {return k != (*kenWeight);} );
				char fullLosses = deceitful (ken2, naomi2, naomiLosses , fewestNaomiLosses);

				fewestNaomiLosses = std::min(fullLosses, fewestNaomiLosses);
			}


		//cout << "new fewest"<<(int)fewestNaomiLosses<<"over"<< (int)naomiLosses<<endl;
	}

	//cout << "out of children"<<(int)fewestNaomiLosses<<endl;
	return fewestNaomiLosses;
}
*/

char deceitful(weights_t& ken, weights_t& naomi, char naomiLosses, char fewestNaomiLosses) { 
	if (naomiLosses >= fewestNaomiLosses) {
		//cout << "prune" <<endl;
		return fewestNaomiLosses;
	}

	char nBlocks = ken.size();

	double kenLightest = * ken.begin();
	double kenHeaviest = * ken.rbegin();
	// find Naomi's lightest block that outweights Ken's lightest but isn't a winner
	auto naomiHalfwinner = std::find_if(naomi.begin(), naomi.end(), [kenLightest,kenHeaviest](double n) { return n > kenLightest && n < kenHeaviest; });

	if (naomiHalfwinner != naomi.end()) {
		// claim it.
		weights_t naomi2(nBlocks - 1), ken2(nBlocks - 1);
		std::copy_if(naomi.begin(), naomi.end(), naomi2.begin(), [naomiHalfwinner](double n) { return n != (*naomiHalfwinner);});
		std::copy_if(ken.begin(), ken.end(), ken2.begin(), [kenLightest](double k) { return k != kenLightest; });
		char fullLosses = deceitful(ken2, naomi2, naomiLosses, fewestNaomiLosses);
		fewestNaomiLosses = std::min(fullLosses, fewestNaomiLosses);
	}
	else {
		//take winners, lose the rest
		return std::find_if(naomi.begin(), naomi.end(), [kenHeaviest](double n) { return n > kenHeaviest; }) - naomi.begin();
	}
	return fewestNaomiLosses;
}

int main() {
	int nCases;
	cin >> nCases;
	++nCases;
	int weightsPerPlayer;
	for (int i=1; i!=nCases; ++i) {
		cin >> weightsPerPlayer;
		weights_t ken, naomi;
		for (int j = 0; j !=weightsPerPlayer; ++j) {
				double x;
		cin>>x;
			naomi.push_back(x);
		}
		for (int j = 0; j !=weightsPerPlayer; ++j) {
				double x; cin>>x;
			ken.push_back(x);
		}
		//lighetest to ehaviest
		sort(ken.begin(), ken.end());
		sort(naomi.begin(), naomi.end());

		// we get naomi's minimum loss.
		cout << "Case #" << i << ": " ;
		cout << weightsPerPlayer - deceitful(ken, naomi, 0, 60);



		/* plain strategy*/
		// count how many of naomi's maxima are greater than ken's maxima

/*
		int plainWins = 0;
		for (int j=weightsPerPlayer-1; i != -1; --j) {

		}
*/
/*
		//theese will be updated
		auto kenMin = ken.begin();
		auto kenMax =ken.end()-1;
		auto naomiMin = naomi.begin();
		auto naomiMax =naomi.end() - 1;
		//deceit strategy

		int deceitWins = 0;
		while (kenMin != kenMax) {
			if (*naomiMax < *kenMax) {
				//knock out a high weight
				++naomiMin;
				--kenMax;
			}
			else {
				// claim a winner
				--naomiMax;
				++kenMin;
				++deceitWins;
			}
		}
		deceitWins += (*kenMax < *naomiMax);

		cout<<deceitWins;
*/

		/*
		normal strategy:
		naomi pick the smallest block.
		ken will pick his smallest block that beats naomi's block.

		deceit strategy:
		naomi should pick her lowest block and say it is heavier than
		ken's second heaviest block. then ken will dispose his heaviest.
		she should do this until she gets sure winners.
		she should play all her winners.
		then she should repeat the strategy.

		but naomi can also exaggerate her block's weights! so instead of taking
her winners first, she should first bluff every block that is larger than ken's smallest block
		*/

cout<<" "<<weightsPerPlayer - conventional(ken, naomi, 0, 60);
cout<<endl;
	}
}
