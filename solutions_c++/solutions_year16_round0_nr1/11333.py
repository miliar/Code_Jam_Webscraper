#include <bits/stdc++.h>
using namespace std;
//Things To remember
// Arrays
// sort( array_name, array_neme+array_size ) //for array sort
#define sortarray(b,t) sort(b,b+t) //sort the first t elements of arrays
//	sizeof(array_name)	//returns the size of the array





//stacks implementation
//	stack<int> ms				//creating a stack
//	ms.push(2)					//inserts 2 into the stack
//	ms.pop()					//pops the top element of the stack
//	ms.empty()					//returns true if the stack is empty
//	ms.top()					//returns the top of the stack
//	ms.size()					//returns the size of the stack
// 	abc.swap(def)				//swaps stack "abc" with stack "def"
//	ms.emplace ("str"); 		//its used generally when  the stack stores strings

//implementing queues
//	queue<int> my;		//creating a queue
//	my.push(1);			//inserting into a queue
//	my.pop();			//poping out of a queue
//  my.size();			//returns the size of the queue
//	my.empty();			//true if the queue is empty
//	my.emplace ("str"); //its used generally when  the queue stores strings
//	my.swap(mydash);	//swaps my queue with mydash queue

// Input macros
#define s(n) scan(&n)			// int - 9 digits
#define sc(n) scanf("%c",&n)	// char
#define sl(n) scan(&n)			// long long - 18 digits
#define sd(n) scanf("%lf",&n)	//	double
#define ss(n) getline(cin,n)	//	string - NOT STABLE

// Printing
#define p(n) printf("%d",n)			// int 
#define pc(n) printf("%c",n)		// char
#define pl(n) printf("%lld",n)		// long long
#define pd(n) printf("%lf",n)		// double
#define ps(n) cout<<n				// string
#define pa(arr) printarr(arr,0,sizeof(arr)/sizeof(*arr))  // array
#define psp() printf(" ")			// space
#define pt() printf("\t")			// tab
#define pln() printf("\n")			// newline

// Useful constants
#define INF INT_MAX
#define EPS 1e-9


// Useful functions
#define bitcount(x) __builtin_popcount(x) 	// returns the number of 1-bits in x.
#define gcd(a,b) __gcd(a,b)					// gcd of a & b
#define max2(x)  __builtin_ctz(x)  			// returns max power of 2


// Useful container manipulation / traversal macros
#define f(i,a,b) for(i=a; i<=b; i++)		// for loop
#define arrclear(a) memset(a, 0, sizeof(a))	// set all element of array to 0



//Data types
#define llui long long unsigned int
#define lli long long int


//Single linked list implementation-Called list in C++
//	forward_list<int>	ml;												//creates the single linked list
//	ml.begin();															//returns iterator to the first element
//	ml.end();															//returns iterator to the last element 
//	ml.clear();															//destroys all elements of the linked list
//	ml.empty();															//true if the linked list is empty
//	ml.front();															//returns the refrence to the first element of the linked list
// 	ml.sort();															//sorts in ascending order in Nlog(N) time
//	ml.sort(greater <int> () );											//sorts in descending order
//	ml.reverse();														//reverses the whole linked list
//	ml.pop_front();														//pops out the first element of the linked list, Hence Size Reduces...
//	ml.push_front(20);													//pushes these elements at the front of the linked list
// 	ml.remove(20);														//removes all nodes whose values are 20
// 	A.merge(B);															//merges A to B and stores in A in a sorted order NOTE: A and B should be sorted in asc.

//	bool single_digit (const int& value) { return (value<10); }			//to remove a number function outside main class
//	ml.remove_if (single_digit);										//removing statement in main class

//Assign method
//		first.assign (4,15);                           // 15 15 15 15
//  	second.assign (first.begin(),first.end());     // 15 15 15 15 second is another list
//  	first.assign ( {77, 2, 16} );                  // 77 2 16

//	auto it = mylist.begin();							//iterator is made
//	it = mylist.erase_after(it);						//element after it is removed and it is moved to next node
//	it = mylist.erase_after(it,mylist.end());			//elements from it to end is removed


//for( int &x : ml)
//	{
//		cout<<x<<" ";													//code for printing through whole linked list 
//	}
bool single_digit (const int& value) { return (value<10); }



//Vectors implementation
//remember space between the nested arrows...
//	vector<int> v;  										//intialize a vector
//	vector<int> v (3,100);									//3 ints with value 100
// 	vector<int> v(10);										//initializes vector of a given size all will have zero values 
//	v.push_back(10);										//adding something at end of vector
//	v.size();												//returns the size of vector
//	v.empty();												//true if v is empty
//	v.resize(25);											//resizes the vector push_back will now add from index 25,26,27 etc.
// 	v.clear(); 												//completely erases the vector
// 	vector< vector<int> > Matrix;							//create 2-D vector
//  vector< vector<int> > Matrix(N, vector<int>(M, -1));	//2-D vectors of size N*M is created all filled with -1, N and M are defined previously
//	void some_function(const vector<int>& v) 				//to pass a vector by reference OMIT const if you want to change the values of vector of that vector in the function
// 	v.at(i); 												//return element at ith index
//  v.begin() 												// returns iterator to the beginning
//	v.end()													//returns iterator to the end
//	v.front()												//returns the first element of the vector
//	v.back()												//returns the last element of the vector
//	v.pop_back();											//destroys the last element of the vector,So size reduces by one.
// 	vector <int>::iterator it=v.begin();					//it = memory adderess of v.begin; so *it=first value
//	int max_value = *max_element(v.begin(), v.end()); 				// Returns value of max element in vector 
//  int pointer_to_min = min_element(v.begin(), v.end()) – X.begin; // Returns index of min element in vector
//for(vector<int>::iterator it = v.begin(); it != v.end(); it++) { 
//      *it++; // Increment the value iterator is pointing to 
// }

int occ[10];

bool check()
{
	for(int i=0;i<10;i++)
	{
		if(occ[i]!=1)
		{
			return false;
		}
	}
	return true;
}
void update(int a)
{
	int r;
	for(  ;a!=0 ; )
	{
		r=a%10;
		if(occ[r]!=1)
		{
			occ[r]=1;
		}
		a=a/10;
	}
	return;
}

int find(int a)
{
	for(int i=0;i<10;i++)
	{
		occ[i]=0;
	}
	for(int i=1;i<100000;i++)
	{
		update(i*a);
		if(check())
		{
			return (i*a);
		}
	}
	
	
}

int main()
{
	
	
	int t;
	cin>>t;
	int input[t];
	int ans[t];
	
	for(int i=0;i<t;i++)
	{
		int a;
		cin>>a;
		if(a==0)
		{
			ans[i]=0;
		}
		else
		{
			ans[i]=find(a);
		}
	}
	
	for(int i=0;i<t;i++)
	{
		if(ans[i]==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
		}
	}
	
	return 0;
}
