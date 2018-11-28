#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream ci ("input.txt");
	ofstream co ("output.txt");
	int T, Smax;
	ci >> T; 
	for(int i=0; i<T; i++){
		ci >> Smax;
		string s;
		ci >> s; //cout<<T<<" ";
		int h[Smax+1];
		for(int j=0; j<Smax+1; j++){
				h[j] = s[j] - '0';
		}
		int n, sum=0, ans=0;
		for(int j=0; j<Smax+1; j++){
			//cout << h[j] << " " ;
			if(j>sum && h[j]!=0) {ans = ans + (j-sum);sum+=(j-sum);}
			sum += h[j]; //cout << ans << endl;
		}
		co << "Case #" << i+1 << ": " << ans <<endl;
	}
	ci.close();
	co.close();
	return 0;
}
