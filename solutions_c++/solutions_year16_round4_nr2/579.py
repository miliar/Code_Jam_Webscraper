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

vector<long double> getNew(vector<long double> res,int size,double a);

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
  cout<<"Starting case "<<caseNr<<endl;
	int N,K;
	getline(infile, line);
	std::stringstream  Stream1(line);
	Stream1>>N>>K;
	vector<long double> proba;
	getline(infile, line);
    std::stringstream  Stream2(line);
	for(int j=0;j<N;j++){
		double buffer;
		Stream2>>buffer;
		proba.push_back(buffer);
	}
    sort(proba.begin(),proba.end());
    long double max=0;
          //for(int j=0;j<proba.size();j++) cout<<proba[j]<<" ";
        //cout<<endl;
    for(int i=0;i<=K;i++){
        vector<long double> selprob;
        for(int j=0;j<i;j++) selprob.push_back(proba[j]);
        for(int j=0;j<K-i;j++) selprob.push_back(proba[N-1-j]);
        int size=0;
       //for(int j=0;j<selprob.size();j++) cout<<selprob[j]<<" ";
        //cout<<endl;
        vector<long double> res(1,0);
        res[0]=1;
        while(size<K){
            res=getNew(res,size,selprob[size]);
            size++;
        }
        if(res[size]>max) max=res[size];
    }
	outfile<<"Case #"<<caseNr+1<<": "<<fixed<<setprecision(9)<<max<<endl;
  }

  infile.close();
  outfile.close();
  return 0;
}


vector<long double> getNew(vector<long double> res,int size,double a){
    vector<long double> next(2*size+3);
    for(int i=0;i<2*size+3;i++){
        if(i==0 || i==1){
        next[i]=res[i]*(1-a);
        }else if(i==2*size+2 || i==2*size+1){
        next[i]=res[i-2]*a;
        }else{
        next[i]=res[i-2]*a+res[i]*(1-a);
        }
    }
    return next;

}


