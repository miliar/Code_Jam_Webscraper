#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <queue> // push, front, pop
#include <sstream>
#include <string>
#include <stack> // push, top, pop
#include <set>
#include <vector>
#include <list> // list.insert(it, data); data inserted before it..
#include <iomanip>
#include <stdio.h>
#include <string.h> 

#define PI 3.14159265358979323846264338327950288
#define fill_(x,v) memset(x,v,sizeof(x))
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x))
#define Pi  3.1415926535
#define ll long long

using namespace std;

ifstream fin("c:\\tmp\\A-large.in");
ofstream fout("c:\\tmp\\out.txt");


int run() {
    int n;
    string s;
    fin >> n >> s;
	cout<<n << ' '<<s<<endl;
    vector<int> num;
    for (int i = 0; i <= n; i++) {
        num.push_back(s[i] - '0');
    }
    
    for (int i = 0; i <= 10000; i++) {
        vector<int> t = num;
        t[0] += i;
        bool pass = true;
        int sum = 0;
        for (int k = 0; k < t.size(); k++) {
            if (sum < k) { pass = false; break;}
            sum += t[k];
        }
        if (pass) return i;
    }
    return -1;
}

int main() {
	int N;
	fin >> N;
	
	//char inp[1000];
  //fin.getline(inp, 1000);
  cout<<N<<endl;
	for( int n = 1; n <= N; n++){
		//fout<<"Case #"<<n<<": ";
		
		int ret = run();
		cout<<"Case #"<<n<<": "<<ret<<endl;
		fout<<"Case #"<<n<<": "<<ret<<endl;
		
		//fout<<"Case #"<<n<<": "<<(ret? "YES" : "NO")<<endl;
		//printf("Case #%d: %d\n", n, ret);
		//cout<<"Case #"<<n<<": "<endl;
		//fout << fixed;
		//fout<<"Case #"<<n<<": "<<setprecision(10)<<ret<<endl;
   }
   return 0;
}
