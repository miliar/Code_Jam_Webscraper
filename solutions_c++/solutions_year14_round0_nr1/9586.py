#include <iostream>

using namespace std;

void reset_cards(int *cards, int n)
{
	int i;
	for (i = 1; i <= n; i++)
		cards[i] = 0;
}
int check_cards(int *cards, int n)
{
	int i, card = 0;

	for (i = 1; i <= n; i++) {
		if (cards[i] == 2) {
			if (!card) 
				card = i;
			else
				return -1;
		}
	}
	return card;
}

int main(void)
{
	int T, i, j, k, row;
	int a, b, c, d, ans;
	int cards[17];

	cin >> T;

	for (i = 0; i < T; i++) {
		reset_cards(cards, 16);
		cin >> row;
		for (j = 1; j <= 4; j++) {
			cin >> a >> b >> c >> d;
			if (row == j) {
				cards[a]++;
				cards[b]++;
				cards[c]++;
				cards[d]++;
			}
		}

		cin >> row;
		for (j = 1; j <= 4; j++) {
			cin >> a >> b >> c >> d;
			if (row == j) {
				cards[a]++;
				cards[b]++;
				cards[c]++;
				cards[d]++;
			}
		}
		ans = check_cards(cards, 16);
		
		cout<<"Case #"<<i+1<<": ";
		if (ans == -1) 
			cout<<"Bad magician!"<<endl;
		else if (ans == 0) 
			cout<<"Volunteer cheated!"<<endl;
		else
			cout<<ans<<endl;
	}
		
	return 0;
}	
