#include <iostream>
#include <cstdio> //sscanf // ungetc
#include <math.h>
#include <algorithm>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string.h>
#include <queue> // front pop push
#include <stdlib.h>
#include <utility>
#include <list>
#include <stack>
#include <sstream>
#include <map>
#include <ctype.h>
#include <locale>   
 
using namespace std;
// priority_queue< ii, vector<ii>, greater<ii> > pq;  pq.push pq.pop pq.top;
// priority_queue por default ordena decrescente
 

#define INF 0x3f3f3f3f 
#define LINF 0x3f3f3f3f3f3f3f3fLL
#define NVI -1
#define db if(0) 
#define pb push_back 
#define EPS 1e-9 
 
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> vi;
typedef vector<vector<int > > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;



int main(void){

	//freopen("in","r",stdin);
	//freopen("out","w",stdout);
	
		
	int t;scanf("%d",&t);
	string str;
	for(int k=0;k<t;k++){
	
		int s;scanf("%d",&s);
		getchar();
		
		getline(cin,str);
		
		int amigos = 0;
		int pessoas = str[0] - '0';
		
		for(int x=1;x<=s;x++){
			//cout<<" x = " << x<<"\n";
			//cout<<pessoas << " " << amigos<<"\n";
			if(pessoas < x && str[x]> '0'){
				
				amigos += (x - pessoas);
				pessoas+= (amigos + str[x] - '0');
				
			}else{
				pessoas+= (str[x] - '0');
			}
			
			
					
		}
		
		printf("Case #%d: %d\n",k+1,amigos);
		
		
	}	
		

    return 0;
}










