#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

std::vector<string> v;
std::vector<__int128> primos;
set<__int128> s;
int n, j;
unsigned char crib[500000000];

__int128 nums(string &s, int b){
	__int128  x=1;
	__int128 sum=0;
	for (int i = s.size()-1; i >= 0; --i)
	{
		if(s[i]=='1')
			sum+=x;
		x*=b;
	}
	return sum;
}

void divide(string s){
	if(s.size()<n-1){
		divide(s+"1");
		divide(s+"0");
	}else{
		v.push_back(s+"1");
	}
	
}

/*void print(string &s){
	for (int i = 0; i < s.size(); ++i)
	{
		cout << s[i];
	}
	cout << " ";
}*/


int main(){
	int t;
	cin >> t;
	for (int z = 1; z <= t; ++z)
	{
		cin >> n >> j;
		if(n>16)
			divide("100000");
		else
			divide("1");
		primos.push_back(2);
		for (int i = 3; i < 33333334; i+=2)
		{
			if(crib[i]==0){
				primos.push_back(i);
				for (int j = i*3; j < 33333334; j+=(i*2))
					crib[j]=1;
			}
		}
		for (int i = 0; i < primos.size(); ++i)
			s.insert(primos[i]);
		cout << "Case #" << z << ":" << endl;
		int k=0;
		std::vector<int> proof;
		proof.reserve(10);
		while(j){
			string a = v[k];
			for (int i = 2; i <= 10; ++i)
			{
				__int128 x = nums(a, i);
				if(s.count(x)==0){
					for (auto it = s.begin(); it!= s.end(); ++it)
					{
						if(x%*it==0){
							proof.push_back(*it);
							it=s.end();
						}
					}
				}else{
					break;
				}
			}
			if(proof.size()==9){
				cout << a << " ";
				for (int i = 0; i < 9; ++i)
				{
					cout << proof[i] << " ";
				}
				cout << endl;
				j--;
			}
			proof.clear();
			k++;
		}
	}
}