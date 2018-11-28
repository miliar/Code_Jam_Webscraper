#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <math.h>
#include <map>
#include <string>
using namespace std;
typedef unsigned int Uint;

int main(){
	ifstream in("in.txt");
	ofstream out("out.out");
	int n;
	in >> n;
	for (int i = 0; i < n; ++i){
		long counter = 0;
		long A, B, K = 0;
		in >> A >> B >> K;
		std::vector<long> AV(A);
		std::vector<long> BV(B);

		long tmp = 0;
		for (auto&& ii : AV){
			ii = tmp;
			tmp++;
		}

		tmp = 0;
		for (auto&& ii : BV){
			ii = tmp;
			tmp++;
		}

		for (auto&& ii : AV){
			for (auto&& jj : BV){
			//	cout << ii << " " << jj << " " << (ii & jj) << endl;
				if ( (ii&jj)  < K)
					++counter;
			}
		}

		out << "Case #"<<i+1<<": " << counter<<endl;
	}
	return 0;
}


//#include <iostream>
//#include <fstream>
//#include <vector>
//#include <array>
//#include <math.h>
//#include <map>
//#include <string>
//using namespace std;
//typedef unsigned int Uint;
//
//int main(){
//	ifstream in("in.txt");
//	ofstream out("out.out");
//	int n;
//	in >> n;
//	for (int i = 0; i < n; ++i){
//		int k;
//		in >> k;
//		vector<char> min;
//		vector<string> strs(k);
//		vector<int> trans(k);
//		int counter = 0;
//		bool flag = true;
//
//		for (auto&& ii : strs)
//			in >> ii;
//
//		int iter = 0;
//
//		for (auto&& ii : strs){
//			vector<char> tmin;
//			vector<char> vv;
//			for (auto&& jj : ii){
//				vv.push_back(jj);
//			}
//			for (auto&& j = vv.begin() + 1; j != vv.end(); ++j){
//				auto&& jp = j - 1;
//				if (*j == *jp){
//					*jp = '0';
//					counter++;
//				}
//			}
//			trans[iter] = counter;
//			counter = 0;
//
//			if (min.empty()){
//				for (auto&& j = vv.begin(); j != vv.end(); ++j){
//					if (*j != '0')
//						min.push_back(*j);
//				}
//			}
//			else{
//				for (auto&& j : vv){
//					if (j != '0')
//						tmin.push_back(j);
//				}
//
//				if (min.size() == tmin.size()){
//					for (int h = 0; h < min.size(); ++h){
//						if (min[h] != tmin[h]){
//							flag = false;
//							break;
//						}
//					}
//				}
//				else{
//					flag = false;
//					break;
//				}
//			}
//			iter++;
//		}
//		if (flag){
//			string eq = strs[0];
//			bool eqflag = true;
//			for (auto&& jj = strs.begin() + 1; jj != strs.end(); ++jj){
//				if (eq != *jj){
//					eqflag = false;
//					break;
//				}
//			}
//
//			if (eqflag){
//				out << "Case #" << i + 1 << ": 0" << endl;
//			}
//			else{
//				int minl = strs[0].length();
//				auto& hh = strs.begin();
//				for (auto&& jj = strs.begin()+1; jj != strs.end(); ++jj){
//					if (jj->length() < minl){
//						minl = jj->length();
//						hh = jj;
//					}
//				}
//				string minst = *hh;
//				minl = minst.length();
//				for (int is = 1; is < minl; ++is){
//					bool flag1 = true;
//					int js = is - 1;
//					char s1 = minst[js];
//					char s2 = minst[is];
//					if (s1 == s2){
//						for (auto&& ks : strs){
//							if ((ks[js] != s1) || (ks[is] != s2)){
//								flag1 = false;
//								break;
//							}
//						}
//						if (flag1){
//							for (auto&& nn : trans)
//								--nn;
//						}
//					}
//				}
//				std::sort(trans.begin(), trans.end());
//				int choose = (trans.size() + 1) / 2 -1;
//				int finalizer = trans[choose];
//				bool trFlag = true;
//				for (auto&& bb = 0; bb < trans.size(); ++bb){
//					if (bb == choose){
//						trans[bb] = 0;
//					}
//					else if ((bb < choose) && (trans[bb] != finalizer)){
//						trans[bb] = finalizer - trans[bb];
//						trFlag = false;
//					}
//					else if (trans[bb] != finalizer){
//						trans[bb] -= finalizer;
//						trFlag = false;
//					}
//				}
//				if (trFlag){
//					for (auto&& nn : trans){
//						nn = finalizer;
//					}
//				}
//
//				unsigned int res = 0;
//				for (auto&& bb : trans){
//					res += bb;
//				}
//				out << "Case #" << i + 1 << ": " <<res<< endl;
//			}
//
//		}
//		else{
//			out << "Case #" << i + 1 << ": Fegla Won" << endl;
//		}
//	}
//
//	return 0;
//}