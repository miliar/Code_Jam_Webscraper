#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

void solve_case(int case_num)
{
    // First choice
	int choice;
	cin >> choice;

    set<int> cardSet;
    
    for (int row = 1; row <= 4; row++) {
        for (int col = 1; col <= 4; col++) {
            int card;
            cin >> card;
            
            if (row == choice)
                cardSet.insert(card);
        }
    }
    
    // Second choice
    cin >> choice;
    
    set<int> answers;
    
    for (int row = 1; row <= 4; row++) {
        for (int col = 1; col <= 4; col++) {
            int card;
            cin >> card;
            
            if ((row == choice) && (cardSet.count(card) > 0))
                answers.insert(card);
        }
    }

    // Output
    cout << "Case #" << case_num << ": ";
    
    if (answers.empty())
        cout << "Volunteer cheated!";
    else if (answers.size() > 1)
        cout << "Bad magician!";
    else
        cout << *answers.begin();
    
    cout << endl;
}

int main()
{
    freopen("A-small-attempt0.in.txt", "r", stdin);
    freopen("A-small-attempt0.out.txt", "w", stdout);

	int num_cases;
	cin >> num_cases;
    
	for (int i = 0; i < num_cases; i++)
	{
		const int case_num = i + 1;
		solve_case(case_num);
	}
    
    return 0;
}
