// http://github.com/lvv
#include <scc/cj.h>	       
#include <scc/tuple_hash.h>	       
#include <lvv/lvv.h>


	typedef array<short,26>		keytab_t;
	typedef bitset<201>		chests_t;

int				n;      // number of chests		(<=200)
//vint 				K;	// available keys               (total <=400)
//bitset<200>			C;	// unopened chests
vector<vint>			cK;	// chest's keys list
vint				cT;	// chest's key type to open     (types 1..25)
vint				route;	// chests opening sequance
long				try_count=0;

	typedef 	tuple<chests_t,keytab_t>		key_type;

struct key_hasher {
	size_t operator()(const key_type &key ) const {
		return
			  std::hash<chests_t>()(get<0>(key)) 
			^ std::hash<keytab_t>()(get<1>(key)) 
		;
	}
};

unordered_set<key_type, key_hasher>	bad_route;



bool open_chests(chests_t C, keytab_t K);


bool try_chest(int i,  chests_t C,  keytab_t K) {
								try_count ++;
        C.reset(i);
	K[cT[i]]--;
	for(int k: cK[i])  K[k]++; // move keys from chest to available keys
	return open_chests(C,K);
};


bool open_chests(chests_t C, keytab_t K) {

	if (C.none()) return true;                 
	if (bad_route.find(tie(C,K)) != bad_route.end()) return false;

        iFOR(n) {
		if (C.test(i)  &&  K[cT[i]] > 0) {
			route.push_back(i+1);
								//__ setw(route.size()), " ", "TRY: ", i, C, K;
			if (try_chest(i, C, K)) {
								//__ "*********************** GOOD: ", i, C, K;
				return true;
			} else {
				route.pop_back();
			}
		}
	}
	bad_route.insert(tie(C,K));
	return false;
};


int main() {
	int cases(in);  NL;
	FOR(case_, 1, cases+1)  {

		// INPUT 

		int k0;
		cin >> k0 >> n;

		cT = vint(n,0);
		cK.resize(n);
		route.clear();
		bad_route.clear();
		keytab_t		K{{0}};	// available keys               (total <=400)
		chests_t    		C;	// unopened chests

		int kt;
		kFOR(k0) { cin >> kt;  K[kt]++; }

		iFOR(n) {
			int k;
			cin >> cT[i] >> k;
			cK[i].resize(k);
			jFOR(k) cin >> cK[i][j];
			C.set(i);
		}

		/////  RESULT
							//PR5(K, cT, cK, C, route);
		_  "Case #",  case_, ": "; 
		if (open_chests(C,K)) 	iFOR(n) _ route[i], " ";
		else			_ "IMPOSSIBLE";
		_ endl;
							//PR1(try_count);
	}                                                                        
}                                                                                
