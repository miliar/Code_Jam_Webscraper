// Jai Mata Di 
#include <iostream>
#include <vector>
using namespace std;
class StandingOvation{
	int maxShyness;
	vector<int> a;
	public:
	void input(){
		cin>>maxShyness;
		for(int i=0;i<=maxShyness;i++){
			char c;
			cin>>c;
			a.push_back(c-'0');
		}
	}
	void print(){
		cout<<"Printing -> "<<maxShyness<<" -> ";
		for(int i=0;i<a.size();i++){
			cout<<a[i]<<" ";
		}
		cout<<endl;
	}
	int calculateMinNoOfFriedsRequired(){
		int minNoOfFriendsRequired = 0;
		int cumulatedSum = 0;
		for(int i=0;i<a.size();i++){
			if(a[i] > 0){
				if(cumulatedSum >= i){
					cumulatedSum += a[i];
				}else{
					minNoOfFriendsRequired += (i-cumulatedSum);
					cumulatedSum +=  ( (i-cumulatedSum) + a[i] );
				}
			}
		}
		return minNoOfFriendsRequired;
	}
};
int main() {
	int noOfTestCases = 0;
	cin>>noOfTestCases;
	for (int testCaseNo = 1; testCaseNo <= noOfTestCases; testCaseNo++)
	{
		StandingOvation standingOvation;
		standingOvation.input();
		//standingOvation.print();
		cout<<"Case #"<<testCaseNo<<": "<<standingOvation.calculateMinNoOfFriedsRequired()<<endl;
	}
	return 0;
}
