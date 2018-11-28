#include<iostream>
#include<set>
using namespace std;

void printRow(int rows, int ii){

	set<int> cont;
	for(int i=0;i<(2 * rows) - 1; i++){
		for(int j=0;j<rows;j++){
			int temp;
			cin>>temp;
			if(cont.find(temp) == cont.end()){
				cont.insert(temp);
			}else{
				cont.erase(temp);
			}
		}
	}
	cout << "Case #" << ii << ": ";
	for(set<int>::iterator it = cont.begin(); it != cont.end(); it++){
		cout<<*it<<" ";
	}
	cout<<endl;
}

int main(void) {
    /* number of test cases */
    unsigned int t;

    cin >> t;

    for(int i=1; i <= t; i++) { //loops for each case
	int temp;
	cin>>temp;
	printRow(temp, i);
    }

    return 0;
}