// __________ AUTHOR INFO __________
// Name/    Khaled Alam
// Email/   khaledalam.net@gmail.com
// Insta/   @MrKhaledAlam
// Twitter/ @Mr_KhaledAlam
// Website/ KhaledAlam.net
//__________________________________

//#include <bits/stdc++.h>
//#include <conio.h>
//#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <limits>
#include <vector>
#include <set>
#include <cmath>
#include <math.h>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <utility>
#include <map>
#include <ctime>
#include <time.h>
#include <bitset>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <typeinfo>
#include <numeric>
#include <functional>


using namespace std;

#define iFILE(N) freopen(#N, "r", stdin)
#define oFILE(N) freopen(#N, "w", stdout)

int main() {

	iFILE(input.txt);
	oFILE(output.txt);
  int t, N, n;
  int ans = 0;
  string line;


  cin>>t;
  getline(cin, line);
  for(int c=1;c<=t;++c)
  {
    getline(cin, line);

    string ans;

    ans = line[0];

    for(int i=1;i<line.length();++i)
      if (line[i] >= ans[0]) ans = line[i] + ans;
      else ans += line[i];

    cout<<"Case #"<<c<<": "<<ans<<endl;
  }

  return  0;
}
