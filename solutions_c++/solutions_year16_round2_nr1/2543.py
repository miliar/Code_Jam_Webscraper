#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <sstream>
using namespace std;

string soln(string m)
{
  vector<int> a(26,0);
  for(int i=0;i<m.length();i++)
  {
	a[m[i]-'A']++;
  }

  vector<int> ans;
  
  if(a['Z'-'A'] != 0)
   {
	int temp = a['Z'-'A'];
	for(int i=0;i<temp;i++)
		ans.push_back(0);
        a['E'-'A']-=temp;
        a['R'-'A']-=temp;
	a['O'-'A']-=temp;
	a['Z'-'A'] = 0;
   }

  if(a['X'-'A'] != 0)
    {
	int temp = a['X'-'A'];
	for(int i=0;i<temp;i++)
	    ans.push_back(6);
	a['S'-'A'] -= temp;
	a['I'-'A'] -= temp;
	a['X'-'A'] = 0;
    }

  if(a['S'-'A'] != 0)
   {
	int temp = a['S'-'A'];
	for(int i=0;i<temp;i++)
	    ans.push_back(7);
	a['E'-'A'] -= temp;
	a['V'-'A'] -= temp;
	a['E'-'A'] -= temp;
	a['N'-'A'] -= temp;
	a['S'-'A'] = 0;
   }
  if(a['V'-'A'] != 0)
   {
	int temp = a['V'-'A'];
	for(int i=0;i<temp;i++)
		ans.push_back(5);
	a['F'-'A'] -= temp;
	a['I'-'A'] -= temp;
	a['E'-'A'] -= temp;
	a['V'-'A'] = 0;
   }

  if(a['F'-'A'] != 0)
  {
	int temp = a['F'-'A'];
	for(int i=0;i<temp;i++)
	     ans.push_back(4);
  	a['O'-'A'] -= temp;
	a['U'-'A'] -= temp;
	a['R'-'A'] -= temp;
	a['F'-'A'] = 0;
  }
    if(a['R'-'A'] != 0)
    {
	int temp = a['R'-'A'];
	for(int i=0;i<a['R'-'A'];i++)
	    ans.push_back(3);
        a['T'-'A'] -= temp;
        a['H'-'A'] -= temp;
	a['E'-'A'] -= temp;
	a['E'-'A'] -= temp;
	a['R'-'A'] = 0;
    }
  if(a['W'-'A'] != 0)
  {
	int temp = a['W'-'A'];
	for(int i=0;i<temp;i++)
	     ans.push_back(2);
	a['T'-'A'] -= temp;
	a['O'-'A'] -= temp;
	a['W'-'A'] = 0;	
  }
  if(a['T'-'A'] != 0)
  {
	int temp = a['T'-'A'];
	for(int i=0;i<temp;i++)
		ans.push_back(8);
	a['E'-'A'] -= temp;
	a['G'-'A'] -= temp;
	a['H'-'A'] -= temp;
	a['I'-'A'] -= temp;
	a['T'-'A'] = 0;
  }
  if(a['I'-'A'] != 0)
  {
	int temp = a['I'-'A'];
	for(int i=0;i<temp;i++)
	       ans.push_back(9);
	a['N'-'A'] -= temp;
	a['N'-'A'] -= temp;
	a['E'-'A'] -= temp;
	a['I'-'A'] = 0;
  }
  if(a['N'-'A'] != 0)
  {
	int temp = a['N'-'A'];
	for(int i=0;i<temp;i++)
		ans.push_back(1);
	a['O'-'A'] -= temp;
	a['E'-'A'] -= temp;
	a['N'-'A'] = 0;
  } 						 	
 sort(ans.begin(),ans.end());
std::ostringstream oss;
 string s = "";
 for(int i=0;i<ans.size();i++)
 {
	oss << ans[i];
 }
 return oss.str();
}


int main() {
	int n;
	string m;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		cin >> m;
		cout << "Case #" << i+1 << ": ";
		string ans = soln(m);
		cout << ans << endl;
		
	}
	return 0;
}
