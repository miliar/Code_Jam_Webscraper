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




int a[105][105];

int m,n;

bool bigger(int y, int x){
	bool r = false;
	fori(i,0,m)
		if(a[i][x] > a[y][x]){
			r = true;
			break;	
		}	
	
	
	fori(i,0,n)
		if(a[y][i] > a[y][x] && r){
			return false;
		}	
	return true;
}

int main()
 {
//	freopen("t.in","r",stdin);
 // 	freopen("t.out","w",stdout);

	int ts,st = 1;
	cin >> ts;
	while(ts--){
		cin >> m >> n;
		fori(i,0,m){
			fori(j,0,n){
				cin >> a[i][j];
			}	
		}
		
		bool ok = true;
		fori(i,0,m){
			fori(j,0,n){
				if(!bigger(i,j)){
					ok = false;
					break;
				}
			}	
			if(!ok)break;
		}
		
		
		
		cout << "Case #" << st++ << ": ";
		if(ok)cout << "YES" << endl;
		else cout << "NO" << endl;
	}



 //system("PAUSE");
 return 0;
 }




