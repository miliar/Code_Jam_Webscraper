#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <climits>
#include <iostream>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>
using namespace std;
typedef vector<string> vs;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef pair<ii,int> iii; 
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef map<string, int> si;
typedef map<int, string> is;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    //system("PAUSE");
    int T;
    int N;
    int r1, r2;
    int rate;
    int maiorRate;
    
    cin >> T;
    for (int i=0; i<T ; i++)
    {
    	r1 = 0;
    	r2 = 0;
    	maiorRate = 0;
    	
    	cin >> N;
    	int vet[N];
    	
        
       
        for (int j = 0; j<N ; j++)
        {
        	cin >> vet[j];
		}
		
		for (int k = 0; k<N-1 ; k++)
		{
			r1 += max(0, vet[k] - vet[k+1]);
			
			maiorRate = max(maiorRate, vet[k] - vet[k+1]);
		}
		
		for (int k = 0; k<N-1 ; k++)
		{
			r2 += min(maiorRate, vet[k]);
		}
		
		cout << "Case #" << i+1<< ": " << r1 << " " << r2 << "\n";
	}
    
    return 0;
}







