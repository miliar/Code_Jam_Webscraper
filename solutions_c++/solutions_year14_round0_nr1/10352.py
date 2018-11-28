#include <iostream>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <cctype>
#include <map>
#include <string>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <sstream>
#include<stdio.h>
using namespace std;
int main()
{ freopen("A-small-attempt1.txt","r",stdin);
freopen("output.txt","w",stdout);
	int testcases,casenum=0;
cin>>testcases;
while (testcases--)
{ 
	casenum++;
	int row, mat[4][4];
vector <int> x;
for (int i=0; i<2; i++)
{
cin>> row;

	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			cin>>mat[i][j];
	for (int i=0; i<4; i++)
		x.push_back(mat[row-1][i]);
	
}
sort (x.begin(), x.end());
int ans,counter=0;	
for (int i=0; i<x.size()-1; i++)
	{ if (x[i]==x[i+1]){ans=x[i];
		counter++;}
}
cout<<"Case #"<<casenum<<": ";
if (counter==1)
	cout<<ans<<endl;
else if (counter>1)
	cout<<"Bad magician!"<<endl;
else cout<<"Volunteer cheated!"<<endl;
}




}