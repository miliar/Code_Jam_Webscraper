#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <cstdio>

using namespace std;

int main()
{
    freopen("D://B-large.in", "r", stdin);
    freopen("D://B-large.out", "w", stdout);
    int numCase;
	cin >> numCase;
	for(int i=0; i<numCase; i++) {
		string s;
		cin>>s;
		int counter=1, result=0;
		char pre=s[0];
		for(int j=1; j<s.size(); ++j){
            if(s[j]!=pre){
                ++counter;
                pre=s[j];
            }
		}
		if(s[0]=='+') result=counter/2*2;
		else result=(counter+1)/2*2-1;
        cout << "Case #" << (i+1) << ": " << result << endl;

	}
    return 0;
}
