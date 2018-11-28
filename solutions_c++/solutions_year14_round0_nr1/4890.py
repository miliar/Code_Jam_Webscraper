#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    int num_cases;
    cin >> num_cases;
//    cout << "num cases: " << num_cases << endl;
   
    for(int ncase = 0; ncase < num_cases; ncase++)
    {
	int row;
	cin >> row;
//	cout << "cards row: " << row << endl;
	int cards[4];
	string line;
	getline(cin, line);
	for (int i = 0; i < 4; i++){
	    getline(cin, line);
	    if(i == row-1)
	    {
	        int a,b,c,d;
		sscanf(line.c_str(), "%d %d %d %d", &a, &b, &c, &d);
	        cards[0] = a;
	        cards[1] = b;
	        cards[2] = c;
	        cards[3] = d;
//		cout << "cards: " << a << " " << b << " " << c << " " << d << endl;
	    }
	}
	cin >> row;
//	cout << "cards row2: " << row << endl;
	int cards2[4];
	getline(cin, line);
	for (int i = 0; i < 4; i++){
	    getline(cin, line);
	    if(i == row-1)
	    {
	        int a,b,c,d;
		sscanf(line.c_str(), "%d %d %d %d", &a, &b, &c, &d);
	        cards2[0] = a;
	        cards2[1] = b;
	        cards2[2] = c;
	        cards2[3] = d;
//		cout << "cards2: " << a << " " << b << " " << c << " " << d << endl;
	    }
	}
	vector<int> intersect(8);
	vector<int>::iterator it;
	sort(cards, cards+4);
	sort(cards2, cards2+4);
	it = set_intersection(cards, cards+4, cards2, cards2+4, intersect.begin());
	intersect.resize(it - intersect.begin());

	

	int size = intersect.size();
	cout << "Case #" << ncase+1 << ": ";
	if (size == 0)
	    cout << "Volunteer cheated!\n";
	if (size == 1)
	    cout << intersect[0] << endl;
	if (size > 1)
	    cout << "Bad magician!\n";	
    }    

    return 0;
}
