#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <time.h>       /* time */
#include <algorithm>
#include <list>
#include <utility>
#include <stack>
#include <math.h>
#include <iomanip>

using namespace std;



int main()
{
  ofstream outfile;
  outfile.open ("solution.out");
  std::ifstream infile;
  infile.open ("data.in", std::ifstream::in);
  std::string   line;
  getline(infile, line);
  std::stringstream  lineStream(line);
  int T;
  lineStream>>T;
  for(int caseNr=0;caseNr<T;caseNr++){
	int N,R,P,S;
	getline(infile, line);
	std::stringstream  Stream1(line);
	Stream1>>N>>R>>P>>S;
	long int l=1;
	for(int i=0;i<N;i++)l*=2;
	long int buf=l;
	int buffer=N;
    vector<int> Rvec,Pvec,Svec;
    Rvec.push_back(R);
    Pvec.push_back(P);
    Svec.push_back(S);
    bool check=true;
    int counter=0;
    if(l==2 && (P==2 || R==2 || S==2))check=false;
    while(l>2){
        counter++;
        l/=4;
        int r=Rvec.back();
        int p=Pvec.back();
        int s=Svec.back();
        Svec.push_back(s-l);
        Rvec.push_back(r-l);
        Pvec.push_back(p-l);
        if(p<l || s<l || r<l || (l==2 && (p-l==2 || s-l==2 || r-l==2))) check=false;
    }
    vector<int> res;
    vector<int> start;
    if(check){
    if(Pvec.back()==1) start.push_back(1);
    if(Rvec.back()==1) start.push_back(2);
    if(Svec.back()==1) start.push_back(3);
    res=start;
    while(l<buf){
    vector<int> b(4*l,0);
    for(int i=0;i<l;i++){
        if(start[i]==1){
            b[4*i+0]=1;
            b[4*i+1]=2;
            b[4*i+2]=1;
            b[4*i+3]=3;
        }
   if(start[i]==2){
            b[4*i+0]=1;
            b[4*i+1]=2;
            b[4*i+2]=2;
            b[4*i+3]=3;
        }
           if(start[i]==3){
            b[4*i+0]=1;
            b[4*i+1]=3;
            b[4*i+2]=2;
            b[4*i+3]=3;
        }

    }
    l*=4;
    start=b;
    res=b;
    }
    outfile<<"Case #"<<caseNr+1<<": ";
    for(int i=0;i<res.size();i++){
        if(res[i]==1) outfile<<"P";
        if(res[i]==2) outfile<<"R";
        if(res[i]==3) outfile<<"S";
    }
    outfile<<endl;
	}else outfile<<"Case #"<<caseNr+1<<": IMPOSSIBLE"<<endl;

  }

  infile.close();
  outfile.close();
  return 0;
}


