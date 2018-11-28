#include <iostream>
#include <vector>
using namespace std;


long long min_friends(long long max_s, string histo){
	vector<int> vh(histo.size());
	for(int i =0; i<histo.size(); ++i){
		vh[i] = histo.c_str()[i] - '0';
	}
	if (histo.size() < 1){
		return 0;
	}

	long long invite = 0;
	long long standing = vh[0];
	for(int i=1; i<histo.size(); ++i){
		if(standing < i){
			invite += (i - standing);
			standing += (i - standing);
		}
		standing += vh[i];
	}

	return invite;
}

int main(){
	int n, max_s;
	string histo;
	
	cin >> n;
	
	for(int i=0; i<n; ++i)
	{
		cin >> max_s;
		cin >> histo;
		cout << "Case #" << i+1 << ": " << min_friends(max_s,histo) << endl;
	}
	return 0;
}