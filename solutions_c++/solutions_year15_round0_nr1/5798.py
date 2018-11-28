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

char arr[1002];

int main(int argc, char* argv[]){
	int t,s;
	FILE * pFile;
	pFile = fopen (argv[1],"r");
	FILE * pFile2;
	pFile2 = fopen (argv[2],"w");
	fscanf(pFile,"%d",&t);
	// cout<<t<<endl;
	FOR(i,t){
		fscanf(pFile,"%d",&s);
		fscanf(pFile,"%s",&arr);
		int sum = arr[0]-48;
		int inv = 0;
		FOR(j,s){
			if(sum>=(j+1)){
				sum+=arr[j+1]-48;
			}
			else{
				int n = j+1-sum;
				inv+=n;
				sum+=(arr[j+1]-48+n);
			}
		}
		fprintf(pFile2, "Case #%d: %d\n",i+1,inv);
		// cout<<"Case #"<<I+1<<": "<<min(arr[l].index+1,arr[m].index+1)<<" "<<max(arr[l].index+1,arr[m].index+1)<<endl;
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