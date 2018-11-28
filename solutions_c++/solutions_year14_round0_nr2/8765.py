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
#include <queue>


using namespace std;


#define mm(type,value) memset(type,value,sizeof(type))
#define mat(matrix,h,w) fori(i,0,h){fori(j,0,w)std::cout<<matrix[i][j]<<" ";std::cout<<std::endl;}
#define sw(matrix,h,w,value) fori(i,0,h)fori(j,0,w)matrix[i][j]=value
#define mt(matrix,s) fori(i,0,s)std::cout<<matrix[i]<<" ";std::cout<<std::endl;
#define qmp(a,b) q.push(make_pair(a,b))
#define pii pair<int,int>


double c,f,x;


int main()
 {

    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
	
	int t,a,b;
	
	cin >> t;
int cs = 1;
	while(t--){
		
		cin >> c >> f >> x;
		double rate = 2.0;
		double sec_need = c/rate;
		
		double sec_cost = sec_need;
		double own = c;
		
		int g = 0;
		while(x/(rate+f) < (x - own) / rate){
			g++;
			rate += f;
			sec_need = c/rate;
			sec_cost += sec_need;	
		}
//		cout << g << endl;		
		sec_cost += (x - own) / rate;
		
		printf("Case #%d: %.7lf\n", cs++, sec_cost);
	}

 //system("PAUSE");
 return 0;
 }
