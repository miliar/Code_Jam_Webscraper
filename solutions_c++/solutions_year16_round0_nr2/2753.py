/*
 * =====================================================================================
 *
 *       Filename:  2.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  04/09/2016 01:11:35 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Gaurav (disisbig), giganticgemmic@gmail.com
 *   Organization:  PEC University of Technology,Chandigarh
 *
 * =====================================================================================
 */

#include<bits/stdc++.h>
using namespace std;
int main()
{
ifstream fin;
ofstream fout;
fin.open("input");
fout.open("output");

int T;
fin>>T;
for(int t=1;t<=T;t++)
{
string s;
fin>>s;
int n=s.length();
int count=0;
for(int i=n-1;i>=0;i--)
{
    if(s.at(i)=='-')
	{
  for(int j=i;j>=0;j--)
  {
	s.at(j)=='-' ? s.at(j)='+' : s.at(j)='-';
  }
  count++;
	}
}
fout<<"Case #"<<t<<": "<<count<<endl;
}

return 0;
}
