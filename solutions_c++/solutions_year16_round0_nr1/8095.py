#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <set>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool check(vector<int> &vec)
{
	for(int i=0 ; i <vec.size();i++)
	{
	
		if (vec[i]==0)
		return false;
		
	}
	cout<<endl;

return true;

}

void findInt(int num, vector<int> &vec)
{
	while ( num > 0)
	{
		vec[num%10]++;
		num=num/10;
	}
	
}
int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n ;
    int m=n;
	vector<int> vec(10,0); // read n 
	set<int> s;
	bool flag=false;
	int count=1;
		while(true)
		{
			if (s.find(n)==s.end())
			{
				s.insert(n);
				findInt(n,vec);
				flag= check(vec);
				 if (flag==true)
				 {
				 	break;
				 }
				count++;
				n=m*count;
			}
			else
			{
				flag=false;
				break;
				
			}
			
		}
	s.clear();
	vec.clear();
    if (flag==true) 
    cout << "Case #" << i << ": " << n << endl;
    else
    cout << "Case #" <<i << ": "<<"INSOMNIA" << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}

