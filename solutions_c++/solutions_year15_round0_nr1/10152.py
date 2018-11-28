#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main() {
	std::ifstream in("A-small-attempt0.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	int n;
	cin >> n;
	int i=0;
	int sum=0;
	int need=0;
	while(i++<n) {
		int k;
		string s;
		cin >> k >> s;
		sum=0;
		need=0;
		for(int j=0; j<=k; j++) {
            int va = s[j]-'0';
			if(j>sum) { need+=(j-sum); sum=j;}
			sum += va;
		}
		cout << "Case #" << i <<": "<< need << endl;
	}
}
