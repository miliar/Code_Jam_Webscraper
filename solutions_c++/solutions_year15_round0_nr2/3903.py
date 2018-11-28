#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

/* Helper function for finding the max of two numbers */
int max(int x, int y)
{
    if(x > y)
    {
        return x;
    }
    else
    {
        return y;
    }
}

/* left is the index of the leftmost element of the subarray; right is one
 * past the index of the rightmost element */
void merge_helper(int *input, int left, int right, int *scratch)
{
    /* base case: one element */
    if(right == left + 1)
    {
        return;
    }
    else
    {
        int i = 0;
        int length = right - left;
        int midpoint_distance = length/2;
        /* l and r are to the positions in the left and right subarrays */
        int l = left, r = left + midpoint_distance;

        /* sort each subarray */
        merge_helper(input, left, left + midpoint_distance, scratch);
        merge_helper(input, left + midpoint_distance, right, scratch);

        /* merge the arrays together using scratch for temporary storage */ 
        for(i = 0; i < length; i++)
        {
            /* Check to see if any elements remain in the left array; if so,
             * we check if there are any elements left in the right array; if
             * so, we compare them.  Otherwise, we know that the merge must
             * use take the element from the left array */
            if(l < left + midpoint_distance && 
                    (r == right || max(input[l], input[r]) == input[l]))
            {
                scratch[i] = input[l];
                l++;
            }
            else
            {
                scratch[i] = input[r];
                r++;
            }
        }
        /* Copy the sorted subarray back to the input */
        for(i = left; i < right; i++)
        {
            input[i] = scratch[i - left];
        }
    }
}

/* mergesort returns true on success.  Note that in C++, you could also
 * replace malloc with new and if memory allocation fails, an exception will
 * be thrown.  If we don't allocate a scratch array here, what happens? 
 *
 * Elements are sorted in reverse order -- greatest to least */

int mergesort(int *input, int size)
{
    int *scratch = (int *)malloc(size * sizeof(int));
    if(scratch != NULL)
    {
        merge_helper(input, 0, size, scratch);
        free(scratch);
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
	ofstream output;
	ifstream inp;
	output.open("output.out6");
	inp.open("b4.in");
	int T;
	inp >> T;
	int M[10][10] = {0};
	for (int i = 1; i < 10; ++i)
	{
		for (int j = 9; j > i; --j)
		{
			int t=j;
			while(t > i)
			{
				M[i][j]++;
				M[j][i]++;
				t-=i;
			}
		}
	}
	for (int k = 0; k < T; ++k)
	{
		int D;
		inp >> D;
		int numbers[D], num[D];
		for (int i = 0; i < D; ++i)
		{
			inp >> numbers[i];
		}

		mergesort(numbers, D);

		for (int i = 0; i < D; ++i)
		{
			num[i] = numbers[D-1-i];
		}

		int A[10];
		for (int i = 0; i < 10; ++i)
		{
			A[i] = 0;
		}

		for (int i = 0; i < D; ++i)
		{
			A[num[i]]++;
		}

		int totalCost = 0;
		for (int i = 1; i < 10; ++i)
		{
			int cuttingCost = 0;
			for (int j = i+1; j < 10; ++j)
			{
				cuttingCost += M[i][j]*A[j];
			}
			if(totalCost == 0)
				totalCost = i+cuttingCost;
			else if(i+cuttingCost < totalCost)
			{
				totalCost = i+cuttingCost;
			}
		}
		output << "Case #" << k+1 << ": " << totalCost << endl;
	}
	

	return 0;
	
}