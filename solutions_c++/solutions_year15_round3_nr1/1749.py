#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
void main(){
	ifstream input("A-small-attempt0.in");
	ofstream output("output.txt");
	int cases;
	input >> cases;
	for (int i = 0; i != cases; ++i){
		int r, c, w;
		input >> r >> c >> w;
		int ans = 0;
		if (c % w == 0)
			ans += r*c / w;
		else
			ans += r*(c / w + 1);
		ans += (w - 1);
		output << "Case #" + to_string(i + 1) + ": " << ans << endl;
	}
}