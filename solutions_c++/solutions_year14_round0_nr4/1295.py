#include "iostream"
#include "stdio.h"
#include "cmath"
#include "cstring"
using namespace std;

#define pi 	3.14159265359
#define e 	2.71828

#define FOR(max) for(int i=0;i<max;i++)
#define FORi(i,max) for(int i=0;i<max;i++)
#define FOR2(min,max) for(int i=min;i<=max;i++)
#define FOR2i(i,min,max) for(int i=min;i<=max;i++)
#define SQR(n) ((n)*(n))
#define CUBE(n) ((n)*(n)*(n))

#define MAX_SMALL 10
#define MAX_LARGE 1000

void heapSort(float* arr, int size);
void shiftRight(float* arr, int low, int high);
void heapify(float* arr, int low, int high);

int main(){
	#ifdef CODEJAM_INPUT
		freopen("in.txt","r",stdin);
		freopen("D-large.out","w",stdout);
	#endif

	int T,ans1,ans2,count;
	cin>>T;

	float *nm= new float[MAX_LARGE+1],
			*kn= new float[MAX_LARGE+1];

	double t0=0;//t1,t2;
	double last,cur;

	// cout<<T;
	// return 0;

	//T=2;
	FORi(tt,T){
		ans1=0;
		ans2=0;

		cin>>count;
		FOR(count)
			cin>>nm[i];

		FOR(count)
			cin>>kn[i];

		heapSort(nm,count);
		heapSort(kn,count);
		

		// FOR(count)
		// 	cout<<nm[i]<<"\t";
		// cout<<endl;
		// FOR(count)
		// 	cout<<kn[i]<<"\t";
		// cout<<endl;

		int j=0;
		FORi(i,count){
			if(nm[i]>kn[j]){
				ans1++;
				j++;
			}
		}

		j=0;
		FORi(i,count){
			if(nm[j]<kn[i]){
				ans2++;
				j++;
			}
		}


		printf("Case #%d: %d %d\n",tt+1,ans1,count-ans2);
		
	}

	return 0;
}



void shiftRight(float* arr, int low, int high)
{
    int root = low;
    while ((root*2)+1 <= high)
    {
        int leftChild = (root * 2) + 1;
        int rightChild = leftChild + 1;
        int swapIdx = root;
        /*Check if root is less than left child*/
        if (arr[swapIdx] < arr[leftChild])
        {
            swapIdx = leftChild;
        }
        /*If right child exists check if it is less than current root*/
        if ((rightChild <= high) && (arr[swapIdx] < arr[rightChild]))
        {
            swapIdx = rightChild;
        }
        /*Make the biggest element of root, left and right child the root*/
        if (swapIdx != root)
        {
            float tmp = arr[root];
            arr[root] = arr[swapIdx];
            arr[swapIdx] = tmp;
            /*Keep shifting right and ensure that swapIdx satisfies
            heap property aka left and right child of it is smaller than
            itself*/
            root = swapIdx;
        }
        else
        {
            break;
        }
    }
    return;
}
void heapify(float* arr, int low, int high)
{
    /*Start with middle element. Middle element is chosen in
    such a way that the last element of array is either its
    left child or right child*/
    int midIdx = (high - low -1)/2;
    while (midIdx >= 0)
    {
        shiftRight(arr, midIdx, high);
        --midIdx;
    }
    return;
}
void heapSort(float* arr, int size)
{
    /*This will put max element in the index 0*/
    heapify(arr, 0, size-1);
    int high = size - 1;
    while (high > 0)
    {
        /*Swap max element with high index in the array*/
        float tmp = arr[high];
        arr[high] = arr[0];
        arr[0] = tmp;
        --high;
        /*Ensure heap property on remaining elements*/
        shiftRight(arr, 0, high);
    }
    return;
}
