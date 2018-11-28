#include <array>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
using namespace std;

struct graph {
	typedef vector<int> conf;
	typedef pair<int, conf> priority;
	conf from;
	conf to;

	graph ( int d, conf& s ) : from(s) {}

	set<conf> reachable ( conf& current ) const {
		set<conf> out;

		// normal 
		conf another;
		for ( auto it : current ) {
			if ( it > 1 )
				another.push_back(it-1);
		}
		out.insert(another);


		//for ( auto it : current ) cout << it << " "; cout << endl;

		// special
		conf different = current;
    	auto last = std::unique(different.begin(), different.end());
   		different.erase(last, different.end());
		for ( int it : different ) {
			for ( int i = 1; i < it; ++i ) {
				conf another = current;
				auto element = lower_bound(another.begin(), another.end(), it);
				assert(*element == it);

				int a = i;
				int b = it - i;
				*element = a;
				another.push_back(b);

				sort(another.begin(), another.end());
				out.insert(another);
			}
		}

		/*for ( auto c : out ) {
			for ( auto it : c ) cout << it << " ";
			cout << endl;
		}

		getchar();*/

		return out;
	}

	// Dijkstra's algorithm
	int solve ( ) const {
	    set<priority> nodes;
	    map<conf, int> distance;
	    set<conf> visited;

	    // initialization of the distance map
	    //for ( auto vertex : this->data )
	    //    distance.insert( pair<conf, int>(vertex.first, numeric_limits<int>::max()));
	        // no need for the previous array, I don't need the minimum tree
	    

	    // in case v is not present
	    distance[to] = numeric_limits<int>::max();
	    distance[from] = 0;
	    nodes.insert(priority(0,from)); // the minimum is at the end

	    while ( !nodes.empty() ) {
	        conf current = nodes.begin()->second;
	        nodes.erase(nodes.begin());
	        visited.insert(current);

	        if ( current == to ) {
	        	break;
	        }

				for ( auto it : current ) assert(it != 0);
				//cout << it << " ";
				//cout << endl;
	        for ( auto x : reachable( current ) ) {
				for ( auto it : x ) assert(it != 0);

	            if ( visited.count( x ) == 0 ) {
	                int alt = distance[current] + 1;
	                
	                if ( distance.count(x) == 0 || alt < distance[x] ) {
	                    distance[x] = alt;
	                    nodes.insert(priority(alt, x));
	                    // nodes could be inserted twice but the one with lower distance
	                    // will be chosen first, therefore the algorithm is still correct.
	                    // further visit of the same node does not cause any addition to the queue
	                }
	            }
	        }
	    }

	    return distance[to];
	}
};


void readcase ( int n, ifstream& infile ) {
	int d;

	infile >> d; assert(d >= 0);
	vector<int> p;

	for ( int i = 0; i < d; ++i ) {
		int next;
		infile >> next;
		p.push_back(next);
	}

	sort(p.begin(), p.end());

	//for ( int i = 0; i < d; ++i ) cout << p[i] << " ";
	//cout << endl;

	cout << "Case #" << n+1 << ": " << graph(d, p).solve() << endl;
}




int main ( int argc, char** argv ) {
	if ( argc < 2 ) {
		cout << "Give me one file as input." << endl;
		return 1;
	}

	ifstream infile(argv[1]);

	int t;
	infile >> t;
	for ( int i = 0; i < t; ++i ) {
		readcase(i, infile);
	}

	return 0;
}