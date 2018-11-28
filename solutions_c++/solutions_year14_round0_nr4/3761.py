#include<iostream>
#include<fstream>
#include<vector>
#include<iomanip>
using namespace std;
void QS(double* store, int first , int last) {
	if(first >= last) {
		return;
	}	
	double pvt;
	int pvt_in = (first + last + first+1)/3;
	pvt = store[pvt_in];
	double h = store[pvt_in];
	store[pvt_in] = store[last];
	store[last] = h;
	int lft = first;
	int rht = last-1;
	while(lft <= rht) {
		while(lft <= rht && store[lft] <= pvt) {
			lft = lft + 1;
		}
		while(rht >= lft && store[rht] >= pvt) {
			rht = rht - 1;
		}
		if(lft < rht) {
			h = store[lft];
			store[lft] = store[rht];
			store[rht] = h;
		}
	}
	h = store[lft];
	store[lft] = store[last];
	store[last] = h;
	QS(store, first, lft-1);
	QS(store, lft + 1, last);	
}
vector<double> QuickSortArray(vector<double> nums)
{
	double* store = new double[nums.size()];
	for(int i = 0; i <nums.size(); i++) {
		store[i] = nums[i];
	}
	QS(store, 0, nums.size()-1);
	for(int i = 0; i <nums.size(); i++) {
		nums[i] = store[i];
	}
	return nums;
}

int main() {
ifstream cin("input.txt");
	int num;
	cin >> num;
	int w;
	for(int i = 0; i < num ; i++) {
		int k_won = 0;
		int n_won = 0;
		bool flag = false;
		double n_choose;
		cin >> w;
		vector<double> k(w);
		vector<double> n(w);
		for(int j =0; j < w; j++) {
			cin >> n[j];
		}
		for(int j =0; j < w; j++) {
			cin >> k[j];
		}
		k = QuickSortArray(k);
		n = QuickSortArray(n);
				int n_dwon = 0;
		int l = 0;
		int m = 0;
		while(l < w) {
			if(n[l] > k[m]) {
				n_dwon++;
				l++;
				m++;
			} else {
				l++;
			}
		}
		// _k = k;
		// _n = n;
		// War//////////////////////////////////////////////////////////////////////////////////////////////
		for(int j =0; j < w; j++) {
			n_choose = n[j];
			n[j] = -1;
			for(int e =0; e<w; e++) {
				if(k[e] > n_choose) {
					k[e] = -1;
					k_won++;
					flag = true;
					break;
				}
			}
			if(flag == false) {
				for(int a = 0; a < w; a++) {
					if(k[a] != -1) {
						k[a] = -1;
						break;
					}
				}
				n_won++;
			}
			flag = false;
		}
		cout << "Case #"<< i+1 << ": " << n_dwon << " " << n_won << endl;
	}	
			
	
return 0;
}