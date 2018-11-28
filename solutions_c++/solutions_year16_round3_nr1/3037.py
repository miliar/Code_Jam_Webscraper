#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <map>
#include <cstring>
#include <climits>
using namespace std;

int allzeros(int arr[],int n) {
	for (int i = 0; i < n ; i++) {
		if (arr[i]!=0) {
			return 1;
		}
	}
	return 0;
}

int main() {
  ofstream output;
  output.open("output.txt");
  char st[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
  int t;
  cin >> t;
  int n,count=0;
  for(int i=1;i<=t;i++) {
    cin >> n;
    int a[n];
    for(int j=0;j<n;j++)cin>>a[j];
    count=0;
    int first=INT_MIN, second=INT_MIN, second_ind=0,first_ind=0,n1=n;
    output << "Case #" << i << ": ";
   	while(allzeros(a,n)) {
	   	int sum=0,l;
	   	int chk=0;
		for (l = 0; l < n ; l++) {
			if(a[l]==1)sum=sum+1;
			else if(a[l]!=0) {
				chk=1;
				break;
			}
	  	 }
	  	if(sum==3 && chk==0) {
	  		count =1;
	  		break;
	  	}
	  	
   		first=INT_MIN;
   		second=INT_MIN;
   		second_ind=0;
   		first_ind=0;
		for (int i = 0; i < n ; i++) {
			//output<<a[i]<<endl;
			if (a[i] > first) {
				second = first;
				first = a[i];
				second_ind = first_ind;
				first_ind = i;
			}
			else if (a[i] > second && i!=first_ind) {
				second = a[i];
				second_ind = i;
			}
	  	 }
	  	 a[first_ind] = a[first_ind]-1;
	  	 a[second_ind] = a[second_ind]-1;
	  	 output <<st[first_ind]<<st[second_ind]<<" ";
	  	//cout <<st[first_ind]<<st[second_ind]<<" ";
	  	 if(a[first_ind]==0) n1=n1-1;
	  	 if(a[second_ind]==0) n1=n1-1;
		sum=0;
	   	chk=0;
		for (l = 0; l < n ; l++) {
			if(a[l]==1)sum=sum+1;
			else if(a[l]!=0) {
				chk=1;
				break;
			}
	  	 }
	  	if(sum==3 && chk==0) {
	  		count =1;
	  		break;
	  	}
      }
      if(count==1) {
      	output<<st[first_ind]<<" ";
      	a[first_ind] = a[first_ind]-1;
      	for (int i = 0; i < n ; i++) {
			if (a[i]==1) {
				output<<st[i];
			}
	  	 }
      }
      output<<endl;
   }
  return 0;
}

