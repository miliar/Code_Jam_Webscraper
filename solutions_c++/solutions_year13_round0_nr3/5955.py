#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>
#include <fstream>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x,y) memset(x,y,sizeof(x))
                         
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

#define SIZE 1005

int A[SIZE];

int reverseint(int num_)
{
        int inv; inv = 0;

        while (num_>0)
        {
                inv = inv * 10 + (num_%10);
                num_ = num_ / 10;
        }

        return inv;
}

int main(int argc, char* argv[]){

	ifstream in(argv[1],ios::in);
	ofstream out("palin.txt",ios::out);
	int t,a,b;
	in >> t;
	int num = 1;

	rep(i,SIZE)
		A[i] = 0;

	for(int i=0; i < SIZE; i++) {
		if(i*i > SIZE)
			break;
		else if (i == reverseint(i) && (i*i) == reverseint (i*i))
			A[i*i] = 1;
	}
// debug
/*	rep(i,SIZE)
		if(A[i]==1)
			cout << i << endl;
*/
	while(t > 0){
		in >> a >> b;
		int count=0;
		for (int i=a; i<=b; i++) {
			if(A[i]==1)
				count++;
		}
		out <<"Case #" << num <<": " << count << endl;
		t--;
		num++;
	}

	in.close();
	out.close();
	return 0;
}