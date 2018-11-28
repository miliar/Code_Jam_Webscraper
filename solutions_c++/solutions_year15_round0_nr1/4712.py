#include<cstdlib>
#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;


int ovation(string in){
	int l = in.length();
	int res = 0;
	int sum = 0;
	sum += (in[0]-'0');
	for (int i = 1; i < l; i++)
	{
		if (sum < i)
		{
			res += i - sum;
			sum = i; 
			sum += (in[i]-'0');
		}
		else{
			sum += (in[i]-'0');
		}

	}
	return res;
}

void main() {
	ifstream q;
	q.open("C:\\Users\\songr_000\\Desktop\\A-large.in");
	int loop;
	q >> loop;
	int temp;
	ofstream ofs("C:\\Users\\songr_000\\Desktop\\output.txt");
	for (int i = 1; i <= loop; i++){
		int temp;
		q >> temp; 
		string y;
		q >> y;
		ofs << "Case #" << i << ": " << ovation(y) << endl;
	}
	ofs.close();
	

}