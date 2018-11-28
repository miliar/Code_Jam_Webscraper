/* first try in google code jam*/
#include <iostream>
#include <string>
using namespace std;

int main(void){
	int times, maxlev;
	char data[1001];
	cin >> times;
	for(int i = 0; i < times; i++){
		cin >> maxlev;
		cin >> data;
		int standup = 0, need = 0;
		for(int lev = 0; lev <= maxlev + 1; lev++){
			while(lev > standup){
				need++;
				standup++;
			}
			standup += data[lev] - '0';
		}
		cout << "Case #" << i+1 << ": " << need << endl;
	}
}
