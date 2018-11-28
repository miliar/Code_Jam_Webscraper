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

#define PI 3.14159265358979323846264338327950288
#define fill_(x,v) memset(x,v,sizeof(x))
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x))
#define Pi  3.1415926535
#define ll long long

using namespace std;

ifstream fin("c:\\hackercup\\cake_cutting.txt");
ofstream fout("c:\\hackercup\\output.txt");

long long run() {
  long long n;
  fin >> n;
  long long totL = 0;
  long long extra = 0;
  for(int i = 0; i < n; i++) {
    int a;
    fin >> a;
    totL += a + 1;
    extra += 2 * a;
  }
  return totL * (totL + 1) / 2 - extra + 1;
}

int main() {
	int N;
	fin>> N;
  cout<<N<<endl;
	for( int n = 1; n <= N; n++)
	{
		//fout<<"Case #"<<n<<": ";
    cout<<n<<endl;
    long long ret = run();
		cout<<"Case #"<<n<<": "<<ret<<endl;
		fout<<"Case #"<<n<<": "<<ret<<endl;
		//printf("Case #%d: %d\n", n, ret);
		//cout<<"Case #"<<n<<": "<endl;
		//fout << fixed;
		//fout<<"Case #"<<n<<": "<<setprecision(10)<<ret<<endl;
   }
   return 0;
}