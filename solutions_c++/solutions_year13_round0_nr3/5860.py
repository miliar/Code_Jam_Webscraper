#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int reverse(int a) {
	 int num = a;
	 int rev = 0;
	 int dig;
	 while (num > 0)
	 {
	      dig = num % 10;
	      rev = rev * 10 + dig;
	      num = num / 10;
	 }
	 return rev;
}
int countRevAndSq(int b,int e) {
	int i=1;
	int count =0;
	for(i;i*i<b;i++);
	for (i;i*i<=e;i++) {
		if( i*i == reverse(i*i) && i == reverse(i)) {	
		count++;
		}
	}
	return count;
}
int main() {
	
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	int T;
	in >> T;
	int beg, en;
	for (int i=1;i<=T;i++) {
		in >> beg >> en;
		out << "Case #" << i  << ": " << countRevAndSq(beg,en) <<endl;
	}
	in.close();
	out.close();
	return 0;
}
