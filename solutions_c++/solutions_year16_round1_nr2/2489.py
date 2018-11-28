#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;


int main()

{
    freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);

    int N, T, h;
    cin >> N;
    for (int caseN = 1; caseN <= N; ++caseN) {
		cin >> T;
		vector<int> heights(2500);
		cout << "Case #" << caseN << ":";
		for ( int m = 0; m < 2* T - 1; m++) {
			for ( int n = 0; n< T; n++ ) {
				cin >> h;
				heights[h]++;
				}
			}
		//for(int i = 0; i< heights.size(); i++)
	 	//	cout<<heights[i];
	 		
	 	int counter = 0;
	 	for(int i = 0; i< heights.size(); i++, counter++){
	 		if(heights[i]>0 && fmod(heights[i],2)!=0 && counter << T)
	 			cout<<" "<<i;
	 	}
	 	cout<<endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;

}
