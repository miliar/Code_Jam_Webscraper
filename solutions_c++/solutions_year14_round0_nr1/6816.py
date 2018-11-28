#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

typedef pair<double, double> couple;
#define rep(i, n) for (int i = 0; i < n; ++i) 

int ligne1[4];
int ligne2[4];

void
read_input() {
    int first_answer,second_answer;
    cin >> first_answer;
    int cards1[4][4], cards2[4][4];

    rep(i, 4) {
	rep(j,4){
	    cin >> cards1[i][j];
	    if(i+1 == first_answer)
		ligne1[j] = cards1[i][j];	    
	}
    }

    cin >> second_answer;
    
    rep(i, 4) {
	rep(j,4){
	    cin >> cards2[i][j];
	    if(i+1 == second_answer)
	    {
		ligne2[j] = cards2[i][j];
	    }
	}
    }
}

void
solve(){
    int answer;
    int nb_candidate=0;
    cerr << "ligne1 :" << endl;
    rep(i,4){
	cerr << ligne1[i] << " " << endl;
    }
    cerr << "ligne2 :" << endl;
    rep(i,4){
	cerr << ligne2[i] << " " << endl;
    }
    rep(i,4){
	rep(j,4){
	    if(ligne1[i] == ligne2[j])
	    {
		nb_candidate++;
		answer  = ligne1[i];
		//cerr << ligne1 << " = " << ligne2  << endl;
	    }
	}
    }
    if(nb_candidate==0)
	cout << "Volunteer Cheated!"  << endl;
    else if(nb_candidate > 1)
	cout << "Bad Magician!" << endl;
    else 
	cout << answer << endl;	    
}



int
main(int argc, char *argv[]) {

    int nb_input;
    cin >> nb_input;
    
    for(int nb_case = 0; nb_case < nb_input; nb_case++)
    {
	
	read_input();

	cout << "Case #" << nb_case+1 << ": " ;
	solve();
    }
  return 0;
}
