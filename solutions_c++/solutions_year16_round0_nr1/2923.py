#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int numCases;
	cin >> numCases;
	for(int i=0; i<numCases; i++){
		int baseNumDef;
		cin >> baseNumDef;
		int baseNum = baseNumDef;
		bool num[10];
		for(int a=0; a<10; a++)
			num[a] = false;
		if(baseNum > 0){
			bool allnum = false;
			int count = 2;
			while(!allnum)
			{
				int temp = baseNum;
				while(temp > 0){
					num[temp%10] = true;
					temp = temp / 10;
				}
				allnum = true;
				for(int a=0; a<10;a++){
					if(allnum == true && num[a] == false){
						allnum = false;
					}
				}
				baseNum = count*baseNumDef;
				count ++;
			}
			cout << "Case #" << i+1 << ": " << (baseNum - baseNumDef) << "\n";
		}else{
			cout << "Case #" << i+1 << ": INSOMNIA"  << "\n";
		}
	}
	return 0;
}