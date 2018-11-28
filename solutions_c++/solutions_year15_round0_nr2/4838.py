#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <stdio.h>

using namespace std;

int p[1001];
int b[1001];
int main()
{

	freopen("B-small-attempt6.in","r",stdin);
    freopen("output7.txt","w",stdout);

   


	int t;
	cin >> t;
	//cout << t << endl;
	int d = 0;
	while (t--) {

		
		
	//	cout << "eaf" << endl;
		int n;
		cin >> n;
		int ans = 0,ans2 = 0;
		vector< int > v(n);
		vector< int > v1(n);
		int d1 = 0;
		for ( int i = 0; i < n;i++) {
			cin  >> v[i];
			d1 = max(d1,v[i]);
			v1[i] = v[i];
		}	
		 ans = d1;
		int count = 0;
		int index;
		int d4;
	//	cout << "d1 " << d1 << endl;
		 while ( d1 !=2  && d1 != 3 && d1 != 1 ) {
		 	//	cout << "sf" << endl;
		 		//break;
		 		d1 = -1, index = -1; 
		 	
			for ( int j = 0; j < v.size();j++) {
					if ( d1 <= v[j]) {
					
					
						d1 = v[j];
						index  = j;

					}
					


			}
		//	cout <<"d1 " << d1 << endl;
			ans = min(ans,d1+count);
			int x = d1/2;
			int y = d1 - x;
			if ( d1 == 9 )  {
				x = 3;
				y = 6;
			}
			v[index] = y;
			v.push_back(x);
			count += 1;
		}
		ans = min(ans,d1 +count);

		d1 = 0;
		for ( int i = 0; i < n;i++) {
			
			d1 = max(d1,v1[i]);
		}	
		 ans2 = d1;
		 count = 0;
		
		
	//	cout << "d1 " << d1 << endl;
		 while ( d1 !=2  && d1 != 3 && d1 != 1 ) {
		 		//cout << "sf" << endl;
		 		//break;
		 		d1 = -1, index = -1; 
		 		
			for ( int j = 0; j < v1.size();j++) {
					if ( d1 <= v1[j]) {
						
					
						d1 = v1[j];
						index  = j;

					}
					


			}
		//	cout <<"d1 " << d1 << endl;
			ans2 = min(ans2,d1+count);
			int x = d1/2;
			int y = d1 - x;
			v1[index] = y;
			v1.push_back(x);
			count += 1;
		}
		ans2 = min(ans2,d1 +count);
		ans = min(ans,ans2);
		d += 1;

		cout << "Case #"<<d << ": "<<ans  << endl;

	}
	return 0;
}