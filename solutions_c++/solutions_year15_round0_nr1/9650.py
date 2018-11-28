#include <iostream>
#include <stdio.h> 
#include <string.h> 
using namespace std;
 
int main() {
	int casos;
	int maxshy;
	char actualshy;
	int persons;
	int personsneeded;
	int personsinvited;
	int numcaso;
	numcaso=1;
	cin >> casos;
	while (casos>0){
		cin >> maxshy;
		personsneeded=-1;
		persons=0;
		personsinvited=0;
		while(maxshy>=0){
			++personsneeded;
			cin >> actualshy;
			if(personsneeded>persons){
				++personsinvited;
				persons++;
			}
			persons+=((int)actualshy-48);
			--maxshy;
		}
		printf("Case #%i: %i\n",numcaso,personsinvited);
		--casos;
		++numcaso;
	}
	return 0;
}