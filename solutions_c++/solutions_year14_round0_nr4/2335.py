#include <iostream>
using namespace std;

#define MAX 1001
#define LC 0.0000001
 
void q_sort(double numbers[], int left, int right)
{
  	double pivot;
  	int l_hold, r_hold;
 
  	l_hold = left;
  	r_hold = right;
  	pivot = numbers[left];
  	while (left < right)
  	{
  	  	while ((numbers[right] >= pivot) && (left < right))
  	    	right--;
  	  	if (left != right)
  	  	{
  	    	numbers[left] = numbers[right];
  	    	left++;
  	  	}
  	  	while ((numbers[left] <= pivot) && (left < right))
  	    	left++;
  	  	if (left != right)
  	  	{
  	    	numbers[right] = numbers[left];
  	    	right--;
  	  	}
  	}
  	numbers[left] = pivot;
  	pivot = left;
  	left = l_hold;
  	right = r_hold;
  	if (left < pivot)
  		q_sort(numbers, left, pivot-1);
  	if (right > pivot)
  	  	q_sort(numbers, pivot+1, right);
}

void quickSort(double numbers[], int array_size)
{
  	q_sort(numbers, 0, array_size - 1);
}

int playWar(double K[], double N[], int size){
	int i=0, j=0, count = 0;
	while(i < size){
		if(K[i] <= N[j]) count++;
		else j++;
		i++;
	}
	return count;
}

// int playDwar(double K[], int KF, int KL, double N[], int NF, int NL){
int playDwar(double K[], double N[], int size){
	int KF = 0, KL = size-1, NF = 0, NL = size-1;
	int count = 0;
	while(NF<=NL){
		if (N[NL] > K[KL]) {
			NL--;
			KL--;
			count++;
		}
		else if(N[NL] <= K[KL]){
			NF++;
			KL--;
		}
	}
	return count;
}

int main(int argc, char const *argv[])
{
	int T, N, i, j, warAns=0, dwarAns=0;
	double Naomi[MAX], Ken[MAX];
	cin >> T;
	for ( i = 0; i < T; ++i)
	{
		cin >> N;
		for ( j = 0; j < N; ++j) cin >> Naomi[j];
		for ( j = 0; j < N; ++j) cin >> Ken[j];
		quickSort(Naomi, N);
		quickSort(Ken, N);

		warAns = playWar(Ken, Naomi, N);
		dwarAns = playDwar(Ken, Naomi, N);
		cout << "Case #" << i+1 << ": " << dwarAns << " " << warAns << endl;

		// for ( j = 0; j < N; ++j) cout << Naomi[j] << " "; cout << endl;
		// for ( j = 0; j < N; ++j) cout << Ken[j] << " "; cout << endl;
	}
	return 0;
}