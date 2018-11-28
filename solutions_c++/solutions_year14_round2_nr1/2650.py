

#include <iostream>
#include <iomanip> //setprecision
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <iterator> //istream_iterator

using namespace std;

#define REP(i,N) for(int i=0;i<(N);i++)
#define FOR(i,A,B) for(int i=(A);i<=(B);i++)
#define ROF(i,A,B) for(int i=(B);i>=(A);i--)
#define ALL(A) (A).begin(),(A).end()

#define ISIi std::istream_iterator<int>
#define ISS std::istringstream
#define cinL2B(L,B) getline(cin,L); B.clear(); B.str(L);

typedef pair<int,int> pi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vector<vi> > vvvi;
typedef vector<pi> vpi;
typedef vector<vpi> vvpi;
typedef queue<pi> qpi;
typedef set<int> si;
typedef set<pi> spi;
typedef set<si> ssi;


int N;
vs words;

/*
int handle_all(vii & elems,const vi& b,int l){
  int m=elems.size();
  int min=-1;

  REP(i,m){
    int rez=0;
    REP(j,l)
      if(a[j]>b[j]){
	rez+=(a[j]-b[j]);
	int xx=a[j]-b[j];
	while(xx){
	  vi nou(l);
	  REP(k,l)
	    if(k==)nou.push_back(k);
	  x--;
	}

      }
      else rez+=(b[j]-a[j]);
  }

}
*/

int handle(const vi& a,const vi & b,int l){
  int rez=0;
  REP(i,l)
    if(a[i]>b[i]) rez+=(a[i]-b[i]);
    else rez+=(b[i]-a[i]);
  return rez;
}

string canonic_str(const string & s, vi & count){
  int l=s.length();
  int index=0;
  int i=1;
  string rez(s);
  if(l==0) return rez;
  //count.clear();
  //count.push_back(rez[index]);
  count=vi(l);
  count[index]++;
  //  int rez=0;
  while(i<l){
    if(rez[index]==rez[i]){
      while(i<l && rez[index]==rez[i]){
	count[index]++;
	rez.erase(rez.begin()+i);
	//count.erase(count.end());
	l--;
      }
    }
    else{
      index++;
      if(index<l) count[index]++;//count.push_back(rez[index]);
      i++;
    }
  }
  return rez;
}


int main(){
  int T,nr;
  string line;
  ISS buffer;
  string tmp;
  
  getline(cin,line); istringstream(line)>>T;
  for(nr=0;nr<T;nr++){
    getline(cin,line); istringstream(line)>>N;

    words.clear();
    REP(i,N){
      cinL2B(line,buffer);
      buffer>>tmp;
      words.push_back(tmp);
    }

    cout<<"Case #"<<nr+1<<":";
    // ------------------------------------------------------

    //REP(i,N) canonic_str(words[i]);
    //cout<<endl; REP(i,N) cout<<words[i]<<" "; cout<<endl;
    vs check(N);
    vvi count(N);
    
    REP(i,N) check[i]=canonic_str(words[i],count[i]);
    bool ok=true;
    int i=0; while(ok && i<N-1){
      if(check[i]!=check[i+1]) ok=false;
      i++;
    }
    if(!ok) cout<<" Fegla Won"<<endl;

    else{
      int nr_char=0; while(nr_char<count[0].size() && count[0][nr_char]!=0) nr_char++;
      //REP(i,N){ for(int j:count[i]) cout<<j; cout<<endl;}
      vvi mat(N,vi(N,0));
      vi max(nr_char,-1),min(nr_char,-1);
      //cout<<check[0]<<" "<<nr_char<<"--"<<N<<endl;
      REP(i,nr_char){
	REP(j,N){
	  if(max[i]==-1 || max[i]<count[j][i]) max[i]=count[j][i];
	  if(min[i]==-1 || min[i]>count[j][i]) min[i]=count[j][i];
	}
      }
      //REP(i,nr_char) cout<<max[i]<<" "<<min[i]<<endl;
      int rez=0;
      REP(i,nr_char) rez+=max[i]-min[i];
      cout<<" "<<rez<<endl;
      /*
      REP(i,N){ REP(j,N)
	cout<<" "<<count[i][j];
	cout<<endl;}
      /*
      FOR(i,0,N-1) FOR(j,i+1,N-1){
	mat[i][j]=handle(count[i],count[j],nr_char);
	mat[j][i]=mat[i][j];
      }



      vvi elems;
      elems.push_back(count[0]);
      */
      //FOR(i,1,N-1)
      //tmp=handle_all(elems,count[i],nr_char);
    }
    

    //int rez=handle(prize,aparate,0,true);
    //if(rez==-1) cout<<" NOT POSSIBLE"<<endl;
    //else cout<<" "<<rez<<endl;
  }
}
