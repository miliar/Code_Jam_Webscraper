#include <iostream>

using namespace std;

int main()
{
	int T, case_count=1;
	cin >> T;
	while(T--){
		int maxshy;
		string audience;
		cin >> maxshy;
		cin >> audience;
		int people_count=(int)audience[0]-48, count=0;
		//cout << people_count;
		for(int i=1;i<audience.length();i++){
			if(people_count<i){
				count+=i-people_count;
				people_count+=i-people_count;
			}
			people_count+=(int)audience[i]-48;
			//cout << people_count;
		}
		cout << "Case #" << case_count << ": " << count << endl;
		case_count++;
	}
	return 0;
}

