#include <fstream> // You should include this library
#include <iostream>
using namespace std;

int arr[7];
int arr2[7];
int main()
{
     freopen("A-small-attempt0.in","r",stdin); // For reading input
     freopen("output.txt","w",stdout); // for writing output
     int t;
     cin >> t;
     for (int i = 0; i < t; i++) {
    	 int num_first;
    	 cin >> num_first;
    	 for (int j = 0; j < 4; j++) {
    		 if (num_first != j+1) {
        		 int temp1;
    			 for (int k = 0; k < 4; k++) {
    				 cin >> temp1;
    			 }
    		 }
    		 else {
    			 for (int k = 0; k < 4; k++) {
    				 cin >> arr[k];
    			 }
    		 }
    	 }
    	 cin >> num_first;
    	 for (int j = 0; j < 4; j++) {
			 if (num_first != j+1) {
				 int temp1;
				 for (int k = 0; k < 4; k++) {
					 cin >> temp1;
				 }
			 }
			 else {
				 for (int k = 0; k < 4; k++) {
					 cin >> arr2[k];
				 }
			 }
		 }
    	 int last = 0;
    	 int cnt = 0;
    	 for (int j = 0; j < 4; j++) {
    		 for (int k = 0; k < 4; k++) {
    			 if (arr[j] == arr2[k]) {
    				 cnt++;
    				 last = arr[j];
    			 }
    		 }
    	 }
    	 cout << "Case #" << i+1 << ": ";
    	 if (cnt < 1) {
    		 cout << "Volunteer cheated!";
    	 }
    	 else if (cnt > 1) {
    		 cout << "Bad magician!";
    	 }
    	 else {
    		 cout << last;
    	 }
    	 cout << endl;
     }
     return 0;
}
