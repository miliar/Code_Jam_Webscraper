#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
// #include <unordered_map>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <climits>
using namespace std;
 
#define ll long long
#define gc getchar 

#define FOR(i,n) for(int i=0;i<n;i++)
#define MOD 1000000009 

typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;


inline void inp( int &n ) 
 {
    n=0;
    int ch=gc();int sign=1;
    while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=gc();}

    while(  ch >= '0' && ch <= '9' )
            n = (n<<3)+(n<<1) + ch-'0', ch=gc();
    n=n*sign;
  }


struct myclass {
    int index;int val;
    myclass(){};
    myclass( int i, int r ) : index(i), val(r) {}
    bool operator<( const myclass & d ) const {
       return val < d.val;//this is for max-heap, reverse this for min heap
    }
};

 
bool myfunction (myclass i,myclass j) {
 
    return (i.val < (j.val));
}


// char input[10002];

// int mul[5][5];
int DP[5][5][5];

int main(int argc, char* argv[]){
	// mul[1][1] = 1;
	// mul[1][2] = 2;
	// mul[1][3] = 3;
	// mul[1][4] = 4;
	DP[2][1][1] = 1;
	DP[2][1][2] = 2;
	DP[2][1][3] = 1;
	DP[2][1][4] = 2;
	DP[2][2][1] = 2;
	DP[2][2][2] = 2;
	DP[2][2][3] = 2;
	DP[2][2][4] = 2;
	DP[2][3][1] = 1;
	DP[2][3][2] = 2;
	DP[2][3][3] = 1;
	DP[2][3][4] = 2;
	DP[2][4][1] = 2;
	DP[2][4][2] = 2;
	DP[2][4][3] = 2;
	DP[2][4][4] = 2;

	DP[3][1][1] = 1;
	DP[3][1][2] = 1;
	DP[3][1][3] = 1;
	DP[3][1][4] = 1;
	DP[3][2][1] = 1;
	DP[3][2][2] = 1;
	DP[3][2][3] = 2;
	DP[3][2][4] = 1;
	DP[3][3][1] = 1;
	DP[3][3][2] = 2;
	DP[3][3][3] = 2;
	DP[3][3][4] = 2;
	DP[3][4][1] = 1;
	DP[3][4][2] = 1;
	DP[3][4][3] = 2;
	DP[3][4][4] = 1;

	DP[4][1][1] = 1;
	DP[4][1][2] = 1;
	DP[4][1][3] = 1;
	DP[4][1][4] = 1;
	DP[4][2][1] = 1;
	DP[4][2][2] = 1;
	DP[4][2][3] = 1;
	DP[4][2][4] = 1;
	DP[4][3][1] = 1;
	DP[4][3][2] = 1;
	DP[4][3][3] = 1;
	DP[4][3][4] = 2;
	DP[4][4][1] = 1;
	DP[4][4][2] = 1;
	DP[4][4][3] = 2;
	DP[4][4][4] = 2;

	int t,x,r,c;
	FILE * pFile;
	pFile = fopen (argv[1],"r");
	FILE * pFile2;
	pFile2 = fopen (argv[2],"w");
	fscanf(pFile,"%d",&t);
	// get_primes();
	// cout<<t<<endl;
	FOR(i,t){
		fscanf(pFile,"%d",&x);
		fscanf(pFile,"%d",&r);
		fscanf(pFile,"%d",&c);
		if(x==1){
			fprintf(pFile2, "Case #%d: GABRIEL\n",i+1);
		}
		else if(DP[x][r][c]==1){
			fprintf(pFile2, "Case #%d: RICHARD\n",i+1);			
		}
		else{
			fprintf(pFile2, "Case #%d: GABRIEL\n",i+1);
		}
	}
	fclose(pFile);
	fclose(pFile2);

	//scanf("%d",&t);
		// unordered_map<int,int> mymap;
		//int temp;
		// inp(n);
		// inp(arr[0]);
		//scanf("%d",&n);
		//scanf("%d",&arr[0]);
	return 0;
 
} 