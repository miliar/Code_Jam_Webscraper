#include<iostream>
using namespace std;
#include <string>

int main(){
	
	int x, p = 1, y, g;
	string n;
	cin >> g;
	for (int l = 1; l <= g; l++)
	{
		n.erase();
		int arr[10] = { -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 };
		cin >> x;
		if (x == 0){
			cout << "Case #" << l << ": INSOMNIA"<<endl;
		}
		else{
			p = 1;
			y = x*p;
			for (int i = 0; i < 1000; i++)
			{

				n.append(to_string(y));

				if (n.find("1") != 4294967295){
					arr[0] = 1;

				}
				if (n.find('2') != 4294967295){
					arr[1] = 2;

				}
				if (n.find('3') != 4294967295){
					arr[2] = 3;
				}
				if (n.find('4') != 4294967295){
					arr[3] = 4;
				}
				if (n.find('5') != 4294967295){
					arr[4] = 5;
				}
				if (n.find('6') != 4294967295){
					arr[5] = 6;
				}
				if (n.find('7') != 4294967295){
					arr[6] = 7;
				}
				if (n.find('8') != 4294967295){
					arr[7] = 8;
				}
				if (n.find('9') != 4294967295){
					arr[8] = 9;
				}
				if (n.find('0') != 4294967295){

					arr[9] = 10;

				}

				if ((arr[0] == 1) && (arr[1] == 2) && (arr[2] == 3) && (arr[3] == 4) && (arr[4] == 5) && (arr[5] == 6) && (arr[6] == 7) && (arr[7] == 8) && (arr[8] == 9) && (arr[9] == 10))
				{
					cout << "Case #" << l << ": " << y << endl;
					break;
				}
				else{
					p++;
					y = x*p;

				}

			}
		}

	}
}