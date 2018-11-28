
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int partition(float* input, int p, int r)
{
    float pivot = input[r];

    while ( p < r )
    {
        while ( input[p] < pivot )
            p++;

        while ( input[r] > pivot )
            r--;

        if ( input[p] == input[r] )
            p++;
        else if ( p < r )
        {
            float tmp = input[p];
            input[p] = input[r];
            input[r] = tmp;
        }
    }

    return r;
}

// The quicksort recursive function
void quicksort(float* input, int p, int r)
{
    if ( p < r )
    {
        int j = partition(input, p, r);        
        quicksort(input, p, j-1);
        quicksort(input, j+1, r);
    }
}

int doSomething(float *array1, float *array2,int size)
{
        int previous_y=0;
        int count=size;
    
        for (int x=0;x<size;x++) {
            for (int y=previous_y;y<size;y++) {
                   if ( array1[x] < array2[y]) {
                        previous_y=y+1;
                        count--;
                        break;
                    }
		      }
		    if (previous_y == size)
		      break;
        }
        
    return count;
}




int main()
{

	int testcase;
	int size;

	float *array1,*array2;
	
	
	ifstream input("input1.in",ios::in);
	ofstream output("output.out",ios::out);
	
	input>>testcase;
	
	for (int i=0;i<testcase;i++)
	{

		input>>size;

		array1 = new float[size];
		array2 = new float[size];
		
		for (int a=0;a<size;a++)
			input>>array1[a];
		
		for (int b=0; b<size;b++)
			input>>array2[b];
			
		quicksort(array1,0,size-1);
		quicksort(array2,0,size-1);
		

        output<<"Case #"<<i+1<<": "<<(size-doSomething(array2,array1,size))<<" "<<doSomething(array1,array2,size)<<endl;
	}
	input.close();
	output.close();
	system("pause");
}


