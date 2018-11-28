
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;
typedef vector<double> vd;
void p(vd& s){
/*	
	for(auto i:s)
		std::cout << std::fixed << std::setw( 7 ) << std::setprecision( 6 ) <<  i << " " ; 	
	cout << endl;
*/
}
int war(vd cn,vd ck){
	int ret = 0;
	int sz = cn.size();
	sort(cn.begin(),cn.end(),[](double a,double b){return a>b;});	
	sort(ck.begin(),ck.end());	
	
	p(cn);
	p(ck);
	for(int i = 0;i< sz;i++){
		int j;
		for(j = 0;j<sz;j++)
			if(ck[j]!=0 && ck[j]>cn[i]){
				ck[j] =0;
				break;		
			}

		if(j==sz)
		    for(j = 0;j<sz;j++)
			if(ck[j]!=0){
				ck[j]=0;
				ret++;
				break;
			}
	}	
	return ret;
}

int dwar(vd cn,vd ck){
	int ret = 0;
	int sz = cn.size();
	sort(cn.begin(),cn.end());	
	sort(ck.begin(),ck.end(),[](double a,double b){return a>b;});	
	vd tn(cn);	

	
	int rr = sz-1; //reverse reader
	int r = 0; // seq reader
	int w = 0;// seq writer
	int rw = sz-1;//reverse writer
	for(int i = 0;i<sz && w<=rw;i++){
		if(cn[i]>ck[rr]){
			tn[rw--] = cn[i];	
			rr--;
		}
		else{
			if(r==rr){
				tn[w] = cn[r];
				break;
			}
			tn[w++] = ck[r+1]+10e-7;
			r++;
		}
	}
	p(cn);
	p(ck);
	p(tn);
	
	for(int i = 0;i< sz;i++){
		int j;
		for(j = 0;j<sz;j++)
			if(ck[j]!=0 && ck[j]>tn[i]){
				ck[j] =0;
				break;		
			}

		if(j==sz)
		    for(j = 0;j<sz;j++)
			if(ck[j]!=0){
				ck[j]=0;
				ret++;
				break;
			}
	}	
	return ret;
}

int main(int argc,char*argv[])
{
int T,i=1;
cin >> T;
while(T-->0){
	int N,y,z;
	cin >> N;	
	vector<double> cn,ck;
	double t;
	for(int i = 0;i< N;i++){
		cin >> t;
		cn.push_back(t);
	}
	for(int i = 0;i< N;i++){
		cin >> t;
		ck.push_back(t);
	}
	y = dwar(cn,ck);
	z = war(cn,ck);
	cout << "Case #" << i++ <<": " << y << " "<< z<<endl;	
}
return 0;
}
