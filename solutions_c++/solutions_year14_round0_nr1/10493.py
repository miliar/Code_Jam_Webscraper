

#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("A-small-attempt3.in", "rt", stdin);
    freopen("out.out", "wt", stdout);

	int a1 , a2 ,t, in;
	vector<int> s1,s2;

	cin >> t;
	for (int k = 1; k <= t; k++) {
		s1.clear() , s2.clear() ;
		cin >> a1;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4 && (cin>>in); j++)
				if (a1 == i)
					s1.push_back(in);

		cin >> a2;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4 && (cin>>in); j++)
				if (a2 == i && count(s1.begin() , s1.end() , in))
						s2.push_back(in);

		if(s2.size() == 1)
			printf("Case #%d: %d\n" , k , s2[0] ) ;
		else if (s2.size() > 1)
			printf("Case #%d: Bad magician!\n" , k ) ;
		else
			printf("Case #%d: Volunteer cheated!\n" , k ) ;
	}

}

