/*	cookie-clicker alpha
 */

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <float> v1;
vector <float> v2;

void dwar_process(vector <float> v1, vector <float> v2, int m)
{
	long int i, dw = 0;
	float n, k;
	vector<float>::const_iterator it;
	
	sort(v1.begin(), v1.end());	
	sort(v2.begin(), v2.end());

	while(1) {
		
		while(1) {
			n = *max_element(v1.begin(), v1.end());
			k = *max_element(v2.begin(), v2.end());
			if (n > k) {
				dw++;
				v1.pop_back();
				v2.pop_back();
				if(v1.empty())
					break;
			}
			else
				break;
		}
		
		if(v1.size() < 2)
			break;
		
		v1.erase(v1.begin());
		v2.pop_back();
	}
	
	cout<<dw;
	
	return;
}

void war_process(vector <float> v1, vector <float> v2, int m)
{
	long int i=0, war = 0, flag = 0;
	float n, k;
	long int temp= 0, size;
	
	sort(v1.begin(), v1.end());	
	sort(v2.begin(), v2.end());
	size = v1.size();
	
	while (1) {
		flag = 0;
		
		if(v1.empty())
			break;
		
		n = *v1.begin();
		for(vector<float>::iterator it = v2.begin() ; it != v2.end(); ++it)
			if(*it > n) {
				v1.erase(v1.begin());
				v2.erase(it);
				flag = 1;
				temp++;
				break;
			}
		
		if(flag == 0) {
			v1.erase(v1.begin());
			v2.pop_back();
		}
	}
	cout<<" "<<size-temp<<endl;
	
	return;
}

int main()
{
	long int n, i, m, j;
	float a;
	cin>>n;
	
	for (i=1 ; i<=n ; i++) {
		cin>>m;
		v1.clear();
		v2.clear();
		for (j=0 ; j<m ; j++) {
			cin>>a;
			v1.push_back(a);
		}
		for (j=0 ; j<m ; j++) {
			cin>>a;
			v2.push_back(a);
		}
		cout<<"Case #"<<i<<": ";
		dwar_process(v1, v2, m);
		war_process(v1, v2, m);
	}
	return 0;
}
