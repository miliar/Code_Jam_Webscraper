#include <fstream>
#include <string>
#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

ifstream in;
ofstream out;

int N;
int M;


int main(int argc, char *argv[]) {
  assert(argc==3 || argc==4);
  string name=string(argv[1])+"-"+argv[2];
  if (argc==4)
    name += string("-")+argv[3];
  in.open((name+".in").c_str());
  assert(in);
  out.open((name+".out").c_str());
  assert(out);
  
  int T;
  in >> T;
  for (int t=1;t<=T;++t) {
    cout<<"t="<<t<<endl<<endl;
    in >> N >> M;
    map<int,int> v; // pos -> +-people
    vector<pair<int,int> > b; // price -> number_of_tickets
    long int count = 0;
    for (int i=0;i<M;++i) {
      int o,e,p;
      in >> o >> e >> p;
      v[o] += p;
      v[e] -= p;
      int k = e-o;
      count += p*(2*N-k+1)*k/2;
      while (count >= 1000002013)
	count -= 1000002013;      
    }
    int mass = 0;
    int c = 0;
    int last = 0;
    for(map<int,int>::iterator i = v.begin(); i!=v.end(); ++i) {
      cout << "***"<<endl;
      cout << "count: "<<count<<endl;
      cout << "tickets: ";
      for (int x=0;x<b.size();++x) {
	cout << "("<<b[x].first<<","<<b[x].second<<")";
      }
      cout << endl;
      cout << i->first<< " "<< i->second<< " "<< mass << " "<<c<< " " <<endl;
      int pos = i->first;
      int k = pos-last;
      cout << k<< " "<<c<<" "<<mass<<endl;
      int cc = k*c - mass*k*(k-1)/2;
      for (int x = 0; x<b.size(); ++x) {
	b[x].first-=k;
      }
      cout <<"cc="<<cc<<endl;
      assert (cc>=0);
      count -= cc;
      while (count <0)
	count += 1000002013;
      c -= k*mass;
      int people = i->second;
      if (people>0) {
	c += N*people;
	b.push_back(pair<int,int>(N,people));
      }
      while (people<0) {
	int n,price;
	cout<<"people="<<people<<" n="<<n<<" price="<<price<<" bsize="<<b.size()<<endl;
	n = b.back().second;
	price = b.back().first;
	if (n>-people) n=-people;
	people += n;
	c -= n * price;
	assert(c>=0);
	if (b.back().second > n) {
	  b.back().second -= n;
	} else {
	  assert (b.back().second == n);
	  b.pop_back();
	}
      }
      assert (c>=0);
      mass += i->second;
      assert(mass >=0);
      last = pos;
      cout <<"mass="<<mass<<" cost="<<c<<endl;
    }

    out<<"Case #"<<t<<": "<<count;
    out<<endl;
  }
  return 0;
}
