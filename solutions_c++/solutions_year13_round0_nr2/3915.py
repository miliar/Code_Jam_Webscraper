/*
 * A2.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Darin
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

int main(){
   int tests,n,m;
   int a[200][200],row[200],col[200];
   //freopen("t.in","r",stdin);
   //freopen("t.out","w",stdout);
   cin >> tests;
   for (int test = 1; test <= tests; test++){
	   cin >> n >> m;
	   for (int i = 0; i < n; i++) row[i] = 0;
	   for (int j = 0; j < m; j++) col[j] = 0;

	   for (int i = 0; i < n; i++)
		  for (int j = 0; j < m; j++){
			 cin >> a[i][j];
			 if (a[i][j] > row[i]) row[i] = a[i][j];
			 if (a[i][j] > col[j]) col[j] = a[i][j];
		  }
	   bool flag = true;
	   for (int i = 0; i < n; i++)
		   for (int j = 0; j < m; j++){
			   int x =std::min(row[i],col[j]);
			   if (x != a[i][j]) flag = false;
		   }
	   cout << "Case #" << test <<": ";
	   if (flag) cout << "YES" << endl;
	   else	     cout << "NO" << endl;
   }
}

