#include<iostream>
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;
int pivot_calculation(int c, int d) {
  vector<int> v;
  for (int i = 0; i < 3; i = i + 1) {
   int r = rand()% (d-c) + c; 
   v.push_back(r);
  }
  int p = (v[2] + v[1] + v[0]) / 3;
   return p;
}
void quicksort(double* array,int first_index,int last_index) {
	if (first_index < last_index) {
		int p = pivot_calculation(first_index,last_index);
		double pivot = array[p];
		int a = first_index;
		int b = last_index - 1;
		array[p] = array[last_index];
		array[last_index] = pivot;
		double t;
		while(a <= b) {
			while(a <= b && array[a] <= pivot) {
				a++;
			}
			while(b >= a && array[b] >= pivot) {
				b--;
			}
			if(a < b) {
				t = array[a];
				array[a] = array[b];
				array[b] = t;
			}
		}
		t = array[a];
		array[a] = array[last_index];
		array[last_index] = t;
		quicksort(array,first_index, a - 1); // sort my elements less than pivot
		quicksort(array, a+1, last_index); // vice versa
	}
}
vector<double> QuickSortArray(vector<double> nums)
{  
	int length = nums.size();
	double* array = new double[length];
	// copying elements of the vector into the Array.
	for (int i = 0; i < length; i = i + 1) {
		array[i] = nums[i]; 
	}
	int last_index = length - 1;
	int first_index = 0;
	quicksort(array,first_index,last_index);
	for (int k = 0; k < length; k = k + 1) {
		nums[k] = array[k];
	}
	return nums;
}
int main() {
	ifstream file("input.txt");
	int number;
	file >> number;
	int limit;
	for(int i = 0; i < number ; i++) {
		int won1 = 0;
		bool flag = false;
		double i_chose;
		file >> limit;
		vector<double> ken(limit);
		vector<double> naomi(limit);
		for(int j =0; j < limit; j++) {
			file >> naomi[j];
		}
		naomi = QuickSortArray(naomi);
		for(int j =0; j < limit; j++) {
			file >> ken[j];
		}
		ken = QuickSortArray(ken);
		
		int won2 = 0;
		int b = 0;
		int c = 0;
		for(int b = 0; b < limit; b++) {
			if(naomi[b] > ken[c]) {
				won2++;
				c++;
			}
		}
		for(int j =0; j < limit; j++) {
			i_chose = naomi[j];
			naomi[j] = -1;
			for(int e =0; e<limit; e++) {
				if(ken[e] > i_chose) {
					ken[e] = -1;
					flag = true;
					break;
				}
			}
			if(flag == false) {
				for(int a = 0; a < limit; a++) {
					if(ken[a] != -1) {
						ken[a] = -1;
						break;
					}
				}
				won1++;
			}
			flag = false;
		}
		cout << "Case #"<< i+1 << ": " << won2 << " " << won1 << endl;
	}	
			
	
return 0;
}