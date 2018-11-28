/*
 * =====================================================================================
 *
 *       Filename:  1.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  04/16/2016 06:00:26 AM
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
string ans(1,s.at(0));
for (int  i = 1;  i < s.length();  i++) {
   if(s.at(i)>=ans.at(0))
		ans = string(1,s.at(i))+ans;
   else
		ans = ans + string(1,s.at(i));

}




fout<<"Case #"<<t<<": "<<ans<<endl;
}

return 0;
}
