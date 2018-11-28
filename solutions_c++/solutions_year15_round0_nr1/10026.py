#include<iostream>
#include<string>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i=0; i < T; i++) {
	int Smax;
	string S;
	cin >> Smax >> S;
	int res=0,count=0;
	for (int j=0; j < S.size(); j++) {
	    int si = S[j] - '0';
	    if(count < j){
		res += j - count;
		count += j-count;
	    }
	    count += si;
	}
	cout << "Case #" << i+1 << ": " << res << endl;
    }

    return 0;
}
