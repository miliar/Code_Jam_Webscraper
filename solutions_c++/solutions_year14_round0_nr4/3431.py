#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
double eps=0.00000001;
using namespace std;
int main()
{
	freopen("dl.in","r",stdin);
	freopen("d_large.out","w",stdout);
	int t;
	cin>>t;
	for(int testc=1;testc<=t;testc++)
	{
		int n;
		cin>>n;
		vector <double> naomi(n),ken(n);
		for(int i=0;i<n;i++)
			cin>>naomi[i];
		for(int i=0;i<n;i++)
			cin>>ken[i];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int d_war=0,o_war=0;
		int pos_n=0,pos_k=n-1,fk=0;
		while(naomi[pos_n]<ken[pos_k])
		{
			if(naomi[pos_n]>ken[fk])
			{
				d_war++;
				pos_n++;
				fk++;
			}
			else
			{
				pos_n++;
				pos_k--;
			}
			if(pos_n>=n)
				break;
		}
		d_war+=n-pos_n;
		pos_n=-1,pos_k=-1;
		while(pos_n<n && pos_k<n)
		{
			pos_n++;
			pos_k++;
			while(ken[pos_k]<naomi[pos_n])
			{
				pos_k++;
				if(pos_k>=n)
					break;
			}
		}
		o_war=n-pos_n;
		cout<<"Case #"<<testc<<": "<<d_war<<" "<<o_war<<"\n";
	}
	return 0;
}