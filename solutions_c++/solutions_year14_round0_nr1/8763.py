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



int t1[4][4];
int t2[4][4];

void gr(int &x, int (*z)[4]){
	cin >> x;
	fori(i,0,4)
		fori(j,0,4)
			cin >> z[i][j];
}

int main()
 {

    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
	
	int t,a,b;
	
	cin >> t;
int cs = 1;
	while(t--){
		gr(a,t1);
		gr(b,t2);
		
		
		a--;b--;
		
		int s = 0;
		int k = 0;
		fori(i,0,4)
			fori(j,0,4)
				if(t1[a][i] == t2[b][j]){
					s++;
					k = t1[a][i];
				}
		cout << "Case #" << cs++ << ": ";
		
		
		if(s == 0){
			cout << "Volunteer cheated!" << endl;
		}else if(s == 1){
			cout << k << endl;
			
		}else
			cout << "Bad magician!" << endl;
		}





 //system("PAUSE");
 return 0;
 }
