
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

#define SIZE 16381
using namespace std;

struct node {
	unsigned long long data;
	struct node *next;
};

unsigned long long isPrime( unsigned long long x) {
	for(unsigned long long i = 2; i < x ; i++) {
		if(x%i == 0) {
			return i;
		}
	}
	return 1;
}

int find(struct node **hashTable, unsigned long long x, int mod) {
	int loc;
	struct node *ptr; 
	loc = x % mod;
	ptr = hashTable[loc];
	
	while(ptr != NULL) {
		if(x == ptr->data) 
			return 1;
		ptr = ptr->next;
	}
	return 0;
}

int insert(struct node **hashTable, unsigned long long x, int mod) {
	int loc;
	struct node *ptr; 
	loc = x % mod;
	ptr = hashTable[loc];
	
	// allocate memory for the pointer
	//ptr = (struct node *) malloc (sizeof(struct node));
	ptr = new (struct node);
	ptr->data = x;
	ptr->next = hashTable[loc];
	hashTable[loc] = ptr;

	return 1;
}

int ProcessInput();

int main()
{

	int testcases, i;

	cin >> testcases;

	for(i=0; i < testcases; i++) {
		cout<<"Case #"<<i + 1<<": ";
		ProcessInput();
	}

return 0;
}

 
int ProcessInput()
{
int N, J, i, k, m, count;
int *jamcoin;
unsigned long long *NumArray, *FactorArray;
int nComb;
struct node *hashTable[SIZE];
int size;

cin >> N; 
cin >> J;

jamcoin = new int[N];
nComb = 1 << (N-2);
NumArray = new unsigned long long[9];
FactorArray = new unsigned long long[9];
// Create a hash Lookup Table for storing numbers and their factors
// Since nComb is power of 2, nComb -1 is a good size for hash table to 
// avoid contentions
size = SIZE;

//hashTable = (struct node**) malloc(size*sizeof(struct node*));
//hashTable = new (struct node*)[size];
cout<<" Here"<< endl;
for (i = 0 ; i < size ;i++) {
	hashTable[i] = NULL;
}
cout<<" Here"<< endl;

// First and last digits of jamcoin is 1 and N > 2
jamcoin[N-1] = 1;
jamcoin[0] = 1;
count = 0;
cout <<"Ncomb = "<<nComb<<endl;
for(i = 0; i < nComb ; i ++) {
	cout<<"i = "<<i<<endl;
	for(m=2; m <= 10; m++) 
		NumArray[m-2] = 1;
	for(k= N-2; k > 0 ; k --) {
		jamcoin[k] = (i >>(k-1)) & 0x1;
		for(m=2; m <= 10; m++)
			NumArray[m -2] = NumArray[m-2]*m + jamcoin[k];
	}
	for(m=2; m <=10; m++)
		NumArray[m-2] = NumArray[m-2]*m + 1;
	
	for(m=2; m <=10; m++){
		// Find Number in hashTable
		if(find(hashTable, NumArray[m-2], size) == 1 ) {
		// It exists so just break
			break;
		}
		else {
		// Check if it is prime
		FactorArray[m-2] = isPrime(NumArray[m-2]);
		if(FactorArray[m-2] == 1) {
			FactorArray[m-2] = insert(hashTable, NumArray[m-2], size);
			break;
		}
		}
	}
	// If we come out of the above loop without breaking it is a valid jamcoin
	if(m==11) {
		for(k=N-1; k >=0 ; k--)
			cout<<jamcoin[k];
		cout<<" ";
		for(m=2; m<=10; m++) 
			cout<<FactorArray[m-2]<<" ";
		cout<<endl;
		for(k=N-1; k >=0 ; k--)
			cout<<jamcoin[k];
		cout<<" ";
		for(m=2; m<=10; m++) 
			cout<<NumArray[m-2]<<" ";
		cout<<endl;
		count ++;
		if(count == J)
			return 1;
	}

}

return 0; 
}

