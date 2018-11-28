#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

bool palindrome(int n)
{
	int d=0,r;
	int copy=n;
	while (n!=0)
	{
		r=n%10;
		d=d*10+r;
		n=n/10;
	}
	return (d==copy);
}

int main(int argc, char *argv[]) {
	set<int> pals, pals_c;
	
	pals_c.insert(1);
	pals_c.insert(4);
	pals_c.insert(9);
	
	pals.insert(11);
	pals.insert(22);
	pals.insert(33);
	pals.insert(44);
	pals.insert(55);
	pals.insert(66);
	pals.insert(77);
	pals.insert(88);
	pals.insert(99);
	
	set<int>::iterator it=pals.begin();
	
	for(it; it!=pals.end(); ++it)
	{
		int aux = (*it) * (*it);
		if(palindrome(aux))
			pals_c.insert(aux);
	}
	
	set<int>::iterator low, up;
	
	int t;
	
	cin >> t;
	
	for (int ncaso = 1; ncaso <= t; ncaso ++)
	{
		int a,b;
		cin >> a >> b;
		low = pals_c.lower_bound(a);
		up = pals_c.upper_bound(b);
		cout << "Case #" << ncaso << ": " << distance(low, up) << endl;
	}
		
	
	return 0;
}

