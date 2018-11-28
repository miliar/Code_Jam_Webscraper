#include<iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main (int argc, char *argv[]) {
	int t, r1, r2;
	cin>>t;
	vector<int> row1(4), row2(4), possible_cards(4);
	vector<int>::iterator it;
	int aux;
	for(int tc=0;tc<t;tc++) { 
		cin>>r1;
		r1--;
		for(int i=0;i<4;i++) {
			if(i!=r1){
				for(int j=0;j<4;j++) { 
					cin>>aux;
				}
			}
			else{
				for(int j=0;j<4;j++) { 
					cin>>row1[j];
				}
			}
		}
		
		cin>>r2;
		r2--;
		for(int i=0;i<4;i++) {
			if(i!=r2){
				for(int j=0;j<4;j++) { 
					cin>>aux;
				}
			}
			else{
				for(int j=0;j<4;j++) { 
					cin>>row2[j];
				}
			}
		}
		
		sort(row1.begin(), row1.end());
		sort(row2.begin(), row2.end());
		
//		cout<<"row1: ";
//		for(int i=0;i<4;i++) { cout<<row1[i]<<" ";}
//		cout<<"\nrow2: ";
//		for(int i=0;i<4;i++) { cout<<row2[i]<<" ";}
//		cout<<endl;
		
		it = set_intersection(row1.begin(), row1.end(), row2.begin(), row2.end(), possible_cards.begin());
		
		cout<<"Case #"<<tc+1<<": ";
		
		if(it==possible_cards.begin())
			cout<<"Volunteer cheated!"<<endl;
		else{
			it--;
			if(it==possible_cards.begin())
				cout<<possible_cards[0]<<endl;
			else
				cout<<"Bad magician!"<<endl;
		}
		
	}
	return 0;
}

