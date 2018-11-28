
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

int main(){
  int N,nr;
  string line;
  int mat1[5][5],mat2[5][5];
  int n;
  ISS buffer;
  string S;
  vi SS(1001);
  int rez,all;
  
  getline(cin,line); istringstream(line)>>N;
  for(nr=0;nr<N;nr++){
    //getline(cin,line); istringstream(line)>>n;

    cinL2B(line,buffer);
    buffer>>n;
    buffer>>S;
    REP(i,n+1){
      SS[i]=S[i]-'0';
    }


    cout<<"Case #"<<nr+1<<": ";

    //cout<<n<<endl; 
    rez=0;
    all=0;
    REP(i,n+1){
      //cout<<" ("<<rez<<" "<<all<<")";
      if(all<i){
	rez+=(i-all);
	all+=(i-all);
      }
      all+=SS[i];
    }
    cout<<rez<<endl;
    //cout<<n<<" "<<S<<endl;
    // ------------------------------------------------------
    //cout<<endl; REP(i,4) {REP(j,4) cout<<mat2[i][j]<<" "; cout<<endl;}


    //      cout<<" Volunteer cheated!"<<endl;
    //if(count==1)
    //  cout<<" "<<mat2[row[poz]][col[poz]]<<endl;
  }
}
