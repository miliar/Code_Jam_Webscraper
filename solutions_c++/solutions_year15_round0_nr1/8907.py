#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	int n,length;
	char Smax[1010];
	int totalpeople = 0;
	int people_need = 0;
	cin >> n;
	for(int i = 0;i < n;i++){
		cin >> length >> Smax;
		for(int j = 0;j < length + 1;j++){
			if(totalpeople >= j){
				totalpeople += Smax[j] - '0';
			}
			else{
				people_need += j - totalpeople;
				totalpeople = j;
				totalpeople += Smax[j] - '0';
			}
		}
		cout << "Case #" << i + 1 << ": " << people_need << endl;
		people_need = 0;
		totalpeople = 0;
	}
	return 0;
}