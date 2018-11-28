#include <iostream>
#include <fstream>
//#include <algorithm>	// std::random_shuffle

using namespace std;

/********************************************
** Implement QuickSort **********************
*********************************************/

const int CUTOFF = 5;	// Using insertion sort when number of elements within subarray equals to CUTOFF

template<typename T>
void swap(T x[], int i, int j) {
	T t = x[i];
	x[i] = x[j];
	x[j] = t;
}
	
// return the index of the median element among x[a], x[b] and x[c]
template<typename T>
int medianOfThree(T x[], int a, int b, int c) {
	if(x[a] < x[b]) {
		if(x[b] < x[c])
			return b;
		else if(x[c] < x[a])
			return a;
		else return c;
	} 
	else {
		if(x[a] < x[c])
			return a;
		else if(x[c] < x[b])
			return b;
		else return c;
	}
}

// partition the subarray x[p ... r] into x[p ... q-1] <= x[q] <= x[q+1 ... r]
template<typename T>
int partition(T x[], int p, int r) {
	int i = p;
	int j = r + 1;
	T pivot = x[p];
	while(true) {
		while(x[++i] < pivot)
			if(i == r) break;
			
		while(pivot < x[--j])
			if(j == p) break;
				
		if (i >= j) break;
			
		swap(x, i, j);
	}
	
	swap(x, p, j);	//put pivot into position
	
	return j;	//index of pivot
}

// sort x[p ... r] using insertion sort
template<typename T>
void insertionSort(T x[], int p, int r) {
	for (int j = p; j <= r; j++) {
		T key = x[j];
		int i = j - 1;
		while (i >= p && x[i] > key) {
			x[i+1] = x[i];
			i--;
		}
		x[i+1] = key;
	}
}		

template<typename T>
void quickSort(T x[], int p, int r) {
	int n = r - p + 1;
	if (n <= CUTOFF) {
		insertionSort(x, p ,r);
		return;
	}
	
	int pivot = medianOfThree(x, p, p + n/2, r);
	swap(x, pivot, p);
	
	int q = partition(x, p, r);
	quickSort(x, p, q-1);
	quickSort(x, q+1, r);
}

/********************************************
** End QuickSort ****************************
*********************************************/

template<typename T>
void printArr(T x[], int p, int r) {
	for	(int j = p;	j < r; j++)
		cout <<	x[j] <<	' ';
	cout << endl;
}

int main() {
	std::ifstream f("D-large.in");	// open the file to read in data
	if (!f) {
		std::cerr << "Error: Failed to open." << std::endl;
		return -1;
	}

	std::ofstream myfile;
  	myfile.open ("output.txt");

	int nCase; // number of cases
	f >> nCase;
	int i;

	for (i = 0; i < nCase ; i++) {
		int nWoods;
		f >> nWoods;

		double naomi[nWoods];
		double ken[nWoods];

		int j;

		for (j = 0; j < nWoods; j++) f >> naomi[j];
		for (j = 0; j < nWoods; j++) f >> ken[j];

		// apply QuickSort
		quickSort(naomi, 0,	nWoods-1);
		quickSort(ken, 0, nWoods-1);

		//printArr(naomi, 0, nWoods);
		//printArr(ken, 0, nWoods);

		int m1 = 0,m2 = nWoods - 1;
		int n1 = 0,n2 = nWoods - 1;

		/** Start Deceitful War **/
		int DWScore = 0;
		while(m1 <= m2) {
			// naomi use her lightest wood to against ken's heaviest wood by calling a extreme 
			// close weight to ken's heaviest wood. Beacuse Ken always wants to win, ken has to
			// use his heaviest wood. Ken will keeps scoring for a while until every woods he
			// left are lighter then naomi's.
			if(naomi[m1] <= ken[n1]) {
				m1++;
				n2--;
			}

			// let ken use his lightest wood by telling the her lightest is heavier than his heaviest wood.
			else {
				m1++;
				n1++;
				DWScore++;
			}

		}
		
		m1 = 0,m2 = nWoods - 1;
		n1 = 0,n2 = nWoods - 1;
		/** Start Regular War **/
		int WScore = 0;
		while(n1 <= n2) {
			// there is no optiaml way for naomi. Let's assume she uses her woods in order
			if(naomi[m1] < ken[n1]) {
				m1++;
				n1++;
			}

			else {
				n1++;
				WScore++;
			}
		}

		myfile << "Case #" << i+1 << ": " << DWScore << " " << WScore << std::endl;

	}
	return 0;



}