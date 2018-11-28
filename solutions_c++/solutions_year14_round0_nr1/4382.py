#include <iostream>
#include <list>

using namespace std;

int main() {
	int T;
			cin>>T;
	
			int firstrow;
			int* first = new int[4];
	
			int secondrow;
			int* second = new int[4];
	
			int buff;
	
			for (int i=0; i<T; i++) {
				cin>>firstrow;
				firstrow--;
				for (int j=0; j<firstrow; j++)
					for (int k=0; k<4; k++) 
						cin>>buff;
				
				for (int j=0; j<4; j++) {
					cin>>buff;
					first [j] = (buff);
				}
				
				for (int j=firstrow+1; j<4; j++)
					for (int k=0; k<4; k++) 
						cin>>buff;
						
				cin>>secondrow;
				secondrow--;
				for (int j=0; j<secondrow; j++)
					for (int k=0; k<4; k++) 
						cin>>buff;
				
				for (int j=0; j<4; j++) {
					cin>>buff;
					second [j] = (buff);
				}
				
				for (int j=secondrow+1; j<4; j++)
					for (int k=0; k<4; k++) 
						cin>>buff;
				
				list<int> common;
				
//				cout<<"1 = ";
//				for(int j=0;j<4;j++) { 
//					cout<<" "<<first[j];
//				}
//				cout<<endl;
//				
//				cout<<"2 = ";
//				for(int j=0;j<4;j++) { 
//					cout<<" "<<second[j];
//				}
//				cout<<endl;
				
				for (int j=0; j<4; j++) {
					for (int k=0; k<4; k++) {
						if (first [j] == second [k]) {
							common.push_front (first [j]);
							break;
						}
					}
				}
				
				cout<<"Case #"<<i+1<<": ";
				
				if (common.size() == 1)
					cout << common.front() << endl;
				else if (common.size() > 1)
					cout << "Bad magician!" << endl;
				else if (common.size() == 0)
					cout << "Volunteer cheated!" << endl;
			}
}
