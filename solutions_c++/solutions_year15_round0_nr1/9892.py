#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("output");
	int n;
	in >> n;
	string line;
	int sMax;
	int audi;
	int ans=0;
	vector<int> aud;
	for(int k=0;k<n;k++)
	{
		in >> sMax;
		//getline(in, line);
		in >> audi;
		for(int i=sMax;i>=0;i--){
			int t=1;
			for(int j=0;j<i;j++)
				t*=10;
			aud.push_back(audi/t);
			audi=audi%t;
		}
		int to=0;
		for(int i=0;i<aud.size();i++){
			//out << aud.at(i) << endl;
			
			if(i!=0 && to<i && aud.at(i)!=0){
				ans+=(i-to);
				to=i;
			}
			to+=aud.at(i);
		}
		//out << "Case #" << k+1 << ": " << ans(L,a) << "\n";
		out << "Case #" << k+1 << ": " << ans << endl;
		ans=0;
		aud.clear();
	}
	//out << line << endl;
	in.close();
	out.close();
	return 0;
}
