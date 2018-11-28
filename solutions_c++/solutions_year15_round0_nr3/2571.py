#include <algorithm>
#include <cstdarg>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <memory>
#include <set>
#include <vector>
#include <intrin.h>
#include <exception>
#include <assert.h>
#include <set>
#include <string>
#include <chrono>
#include <sstream>
#include <bitset>
#include <list>
#include <deque>

#include <boost/multiprecision/integer.hpp>

using namespace std;

typedef int64_t i64;
typedef uint64_t u64;
typedef int32_t i32;
typedef uint32_t u32;
typedef boost::multiprecision::int128_t i128;
typedef boost::multiprecision::uint128_t u128;
typedef boost::multiprecision::int256_t i256;
typedef boost::multiprecision::uint256_t u256;
typedef boost::multiprecision::int512_t i512;
typedef boost::multiprecision::uint512_t u512;
typedef boost::multiprecision::int1024_t i1024;
typedef boost::multiprecision::uint1024_t u1024;

#define F(i,a) for(size_t (i)=0;(i)<(a);++(i))
#define R(i,a) for(i64 (i)=((a));(i)>=0;--(i))
#define D(i,a,b) for(size_t (i)=(a);(i)<(b);++(i))
#define E(i,a) for(auto (i)=(a).begin();(i)!=(a).end();++(i))
#define V vector
#define VI V<int>
#define VVI V<V<int>>
#define VL V<i64>
#define VVL V<V<i64>>
#define ALL(a) (a).begin(),(a).end()
#define VS V<string>
#define P pair
#define MP make_pair


#define DEBUG 0
#define PRINT 0



map<string,map<string,string>> q;

//leave it c++ to make treating chars as a string a project in itself
string c2s(char c0, char c1){
	ostringstream ss;
	ss << c0 << c1;
	return ss.str();
}

string c2s(char c0){
	ostringstream ss;
	ss << c0;
	return ss.str();
}

void init(){
		map<string,string> q0;
		q0["1"]="+1";
		q0["i"]="+i";
		q0["j"]="+j";
		q0["k"]="+k";
		q["1"]=q0;
		map<string,string> q1;
		q1["1"]="+i";
		q1["i"]="-1";
		q1["j"]="+k";
		q1["k"]="-j";
		q["i"]=q1;
		map<string,string> q2;
		q2["1"]="+j";
		q2["i"]="-k";
		q2["j"]="-1";
		q2["k"]="+i";
		q["j"]=q2;
		map<string,string> q3;
		q3["1"]="+k";
		q3["i"]="+j";
		q3["j"]="-i";
		q3["k"]="-1";
		q["k"]=q3;
}

inline
string mult(string lhs, string rhs){
	string v = q[c2s(lhs[1])][c2s(rhs[1])];
	if(lhs[0]=='-' && rhs[0]=='+' || lhs[0]=='+'  && rhs[0]=='-'){
		if(v[0]=='+') v[0]='-';
		else v[0]='+';
	}
	return v;
}

bool check(i64 i, i64 j, i64 k, i64 ic, i64 jc, i64 kc, i64 z){
	z-=k;
	if(z==0) return true;
	i128 ii(ic);
	i128 ij(jc);
	i128 ik(kc);

	V<i128> v;
	if(ii!=-1) v.push_back(ii);
	if(ij!=-1) v.push_back(ij);
	if(ik!=-1) v.push_back(ik);

	if(v.size()==3){
		i128 g0 = boost::multiprecision::gcd(v[0],v[1]);
		i128 g1 = boost::multiprecision::gcd(g0,v[2]);
		if((z%g1)==0) return true;
	}
	else if(v.size()==2){
		i128 g = boost::multiprecision::gcd(v[0],v[1]);
		if((z%g)==0) return true;
	}
	else if(v.size()==1){
		if((z%v[0])==0) return true;
	}

	return false;
	
}

string proc(const string& s, i64 x){
	if(s.size()*x<3) return "NO";

	map<string,set<i64>> mi,mj,mk;
	set<i64> si,sj,sk;
	map<i64, set<i64>> jval;
	map<i64, i64> jcyc;
	string curr = "+1";
	i64 i = 0,j=0,k=0;
	bool icycfound = false;
	for(;i<s.size()*x;) {
		string next = c2s('+',s[i % s.size()]);
		curr = mult(curr,next);
		if(mi.find(curr)==mi.end()){
			set<i64> sit;
			mi[curr]=sit;
		}
		if(curr == "+i"){
			si.insert(i);
		}
		if(mi[curr].find(i % s.size()) != mi[curr].end()){
			//cycle found
			icycfound=true;
			break;
		}
		mi[curr].insert(i % s.size());
		++i;
	}
	//no +i found from left before we hit a cycle
	if(si.size()==0) return "NO";
	int i_cycle_len = (icycfound?i:-1);

	for(auto ii=si.begin();ii!=si.end();++ii){
		//we know its +i at each si
		set<i64> sjt;
		jval[(*ii)] = sjt;
		curr="+1";
		j=(*(ii))+1;
		mj.clear();
		i64 j_cycle_len = 0;
		bool jcycfound=false;
		for(;j<s.size()*x;){
			string next = c2s('+',s[j % s.size()]);
			curr = mult(curr,next);
			if(mj.find(curr)==mj.end()){
				set<i64> sjt0;
				mj[curr]=sjt0;
			}
			if(curr=="+j"){
				jval[*(ii)].insert(j);
			}
			if(mj[curr].find(j % s.size()) != mj[curr].end()){
				//cycle found
				jcycfound=true;
				break;
			}
			mj[curr].insert(j % s.size());
			++j;
		}
		if(jcycfound){
			jcyc[*ii]=j-(*ii);
		} else {
			jcyc[*ii]=-1;
		}
	}
	//all i's found cycles without j's
	if(jval.size()==0) return "NO";

	for(auto ii=si.begin();ii!=si.end();++ii){
		for(auto ij=jval[*ii].begin(); ij!=jval[*ii].end();++ij){
			i = *ii;
			j = *ij;
			k = (*ij)+1;
			curr = "+1";
			mk.clear();
			i64 j_cycle_len = jcyc[*ii];
			i64 k_cycle_len = 0;
			bool kcycfound=false;
			sk.clear();
			for(;k<s.size()*x;){
				string next = c2s('+',s[k % s.size()]);
				curr=mult(curr,next);
				if(mk.find(curr)==mk.end()){
					set<i64> skt;
					mk[curr]=skt;
				}
				if(curr=="+k"){
					if(k==s.size()*x-1) return "YES";
					sk.insert(k);
				}
				if(mk[curr].find(k%s.size()) != mk[curr].end()){
					//cycle found;
					kcycfound=true;
					break;
				}
				mk[curr].insert(k%s.size());
				++k;
			}
			if(kcycfound){
				k_cycle_len=k;
			}
			else {
				k_cycle_len=-1;
			}

			if(check(i,j,k,i_cycle_len,j_cycle_len,k_cycle_len,s.size()*x)){
				return "YES";
			}
		}
	}
	
	return "NO";

}

string proc1(ofstream& fo, const string& l, i64 x){
	if(l.size()*x<3) return "NO";

	VS vi,vk;
	vi.reserve(l.size()*x);
	vk.reserve(l.size()*x);
	string s;
	s.reserve(l.size()*x);
	F(i,x){
		s+=l;
	}
	/*fo << s << endl;*/
	string curr = c2s('+',s[0]);
	vi.push_back(curr);
	/*fo << curr << " ";*/
	D(i,1,s.size()){
		string next = c2s('+',s[i]);
		curr=mult(curr,next);
		vi.push_back(curr);
		/*fo<< curr << " ";*/
	}
	/*fo << endl;*/
	curr = c2s('+',s[s.size()-1]);
	vk.push_back(curr);
	bool switch_signs = false;
	for(int i=s.size()-2;i>=0;--i){
		string next=c2s('+',s[i]);
		if(curr[1]=='1' || next[1]=='1') switch_signs=false; else switch_signs=true;
		curr=mult(next,curr);
		//multiplying backwards is equivlent to negating the forward mult
		//unless one argument is +-identity
		//perhaps its easier to just do it correctly in the first place, whoops
		//if(switch_signs){if(curr[0]=='+') curr[0]='-'; else curr[0]='+';}
		vk.push_back(curr);
	}
	std::reverse(ALL(vk));

	/*F(i,vk.size()){
		fo << vk[i] << " ";
	}
	fo<<endl;*/

	F(i,vi.size()){
		if(vi[i]=="+i") {
			for(int j=i+1;j<vi.size()-1;++j){
				if(vi[j]=="+k" && vk[j+1]=="+k"){
					return "YES";
				}
			}
		}
	}

	return "NO";

}


void gen_file(){
	ofstream fo("C:/gcj/c2015.txt");
	fo << 1000 << endl;
	VS v;
	v.push_back("i");
	v.push_back("j");
	v.push_back("k");
	F(i,1000){
		int l = (rand()%10000)+1;
		int x = 10000/l;
		fo << l << " " << x << endl;
		F(j,l){
			fo << v[rand()%3];
		}
		fo << endl;
	}
}

int main(int argc, char** argv){
	string fs;
#if DEBUG==1
	fs = "c2015";
#else
	fs = *(++argv); 
#endif
	string infile = "C:/gcj/" + fs + ".txt";
	string outfile = "C:/gcj/" + fs + "_out.txt";
	ifstream fi(infile.c_str());
	ofstream fo(outfile.c_str());
	
	init();

	std::cout << "Running " << infile << endl;
	
	i64 t,l,x;
	fi >> t;
	F(i, t){
		fi >> l >> x;
		string s;
		fi >> s;
#if PRINT == 1
			fo << s << " ";
			fo << endl;
#endif
		fo << "Case #" << i + 1 << ": " << proc1(fo,s,x) << endl;
		std::cout << "Case #" << i+1 << " complete" << endl;
#if PRINT == 1
			fo << endl << endl;
#endif
	}

	fo.flush();
	fo.close();
	fi.close();
	return 0;
}


/* B 2015 small
int proc(ofstream& fo, const VI& v, bool split63){

	//well this is a cheesy solution 
	VI vp(v);
	make_heap(ALL(vp));
	int best = vp.front();
	int stop = vp.front()+1;
	int curr = best;
	int moves = 0;
	while(moves<=stop && vp.front()>1){
		int m = vp.front(),k;
		pop_heap(ALL(vp));
		vp.pop_back();
		if(split63 && m==9){
			m=6;
			k=3;
		}
		else {
			k = m/2;
			m -= k;
		}
		vp.push_back(m);
		push_heap(ALL(vp));
		vp.push_back(k);
		push_heap(ALL(vp));
		++moves;
		curr=moves+vp.front();
		if(best>curr) best=curr;
#if PRINT == 1
		fo << "curr = " << curr << " best = " << best << " moves = " << moves << endl;
		F(i,vp.size()){
			fo << vp[i] << " ";
		}
		fo << endl;
#endif 
	}
	return best;
}

void gen_file(int n){
	ofstream fo("C:/gcj/b2015.txt");
	fo << n + 1 <<endl;
	F(i,2){
		int p = 1000;
		fo << p << endl;
		F(j,p){
			fo << 1000 << " ";
		}
		fo << endl;
	}
	F(i,n){
		int p = (rand() % 1000)+1;
		fo << p << endl;
		F(j,p){
			fo << 1000 - (rand()%100) << " ";
		}
		fo << endl;
	}
	fo.flush();
	fo.close();
}

//B 2015
int main(int argc, char** argv){
	string fs;
#if DEBUG==1
	fs = "b2015";
	//gen_file(100);
	//return 0;
#else
	fs = *(++argv); 
#endif
	string infile = "C:/gcj/" + fs + ".txt";
	string outfile = "C:/gcj/" + fs + "_out.txt";
	ifstream fi(infile.c_str());
	ofstream fo(outfile.c_str());

	cout << "Running " << infile << endl;

	int t,p,n;
	fi >> t;
	F(i, t){
		fi >> n;
		VI v;
		F(j,n){
			fi >> p;
			v.push_back(p);
#if PRINT == 1
			fo << p << " ";
#endif
		}
#if PRINT == 1
			fo << endl;
#endif
		fo << "Case #" << i + 1 << ": " << min(proc(fo,v,true),proc(fo,v,false)) << endl;
		cout << "Case #" << i+1 << " complete" << endl;
#if PRINT == 1
			fo << endl << endl;
#endif
	}

	fo.flush();
	fo.close();
	fi.close();
	return 0;
}

*/