#define CO(x) std::cout << #x" = " << x << std::endl
#define fori(i,start,sharpEnd) for(int i = start; i < sharpEnd; i++)
#define fora(i,start,End) for(int i = start; i >= End; i--)
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <climits>
#include <map>
#include <vector>
#include <cassert>
#include <limits>
#include <iomanip>


using namespace std;


#define mm(type,value) memset(type,value,sizeof(type))
#define mat(matrix,h,w) fori(i,0,h){fori(j,0,w)std::cout<<matrix[i][j]<<" ";std::cout<<std::endl;}
#define sw(matrix,h,w,value) fori(i,0,h)fori(j,0,w)matrix[i][j]=value
#define mt(matrix,s) fori(i,0,s)std::cout<<matrix[i]<<" ";std::cout<<std::endl;
#define EPS 10e-8


bool pal(long long x){
	stringstream is;
	is << x;
	string a = is.str();
	int len = a.size()>>1;
	int ml = a.size();
	fori(i,0,len){
		if(a[i] != a[ml-1-i])	
			return false;
	}
	return true;
}


bool sq(long long x){
	long long g = sqrt(x);
	long long h = g;
	g *= g;
	if(g == x && pal(h))
		return true;
	return false;	
}


int p[5] = {1,4,9,121,484};

int main()
 {

//	freopen("t.in","r",stdin);
//  	freopen("t.out","w",stdout);
/*	vector<int> v;
	for(long long i = 0; i <= 10000; i++){
		if(sq(i) && pal(i)){
			v.push_back(i);	
		}
	}
	
	fori(i,0,v.size())
		cout << v[i] << endl;
	cout << endl;
*/

	int t,a,b;
	int cs = 1;
	cin >> t;
	while(t--){
		cin >> a >> b;
		int pa = 0,pb = 0;	
		
		while(pa < 5 && a > p[pa])
			pa++;

		while(pb < 5 && b >= p[pb])
			pb++;	

		//CO(pa);CO(pb);
		cout <<  "Case #" << cs++ << ": " << pb-pa << endl;
	}





 //system("PAUSE");
 return 0;
 }




