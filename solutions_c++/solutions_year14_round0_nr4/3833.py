#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
using namespace std; 



// find your lowest and use it to get rid of the others highest

inline long double do_something ()
{
	
}

int smallest(vector<double> ptr,int size)
{
	double small=DBL_MAX;
	int index=0;
	for (int x=0;x<size;x++)
	{
		if (small > ptr[x])
		{
			small = ptr[x];
			index=x;
		}

	}

	return index;
}


int smallest_to_beat_me(vector<double> ptr,int size,double number)
{
	double small=DBL_MAX;
	int index=0;
	for (int x=0;x<size;x++)
	{
		if (small > ptr[x]  && ptr[x] >number)
		{
			small = ptr[x];
			index=x;
		}

	}
	if (small ==DBL_MAX ) return -1;

	return index;
}

int largest(vector<double> ptr,int size)
{
	double large=DBL_MIN;
	int index=0;
	for (int x=0;x<size;x++)
	{
		if (large < ptr[x])
		{
			large = ptr[x];
			index=x;
		}

	}

	return index;
}

void remove_at (double * & ptr,int & size, int index)
{
	double * ptr1 = new double [size-1];
	int offset=0;
	for (int x=0;x<size-1;x++)
	{
		if (x==index) 
			offset++;
		ptr1[x] = ptr[x+offset];
	}

	delete ptr;
	ptr=ptr1;
	size--;
}

int main ()
{
	
	try{
		ifstream fin;
		ofstream fout;
		fout.open("output.txt");
		fin.open("D-large.in");
		
		if (!fin.is_open() || !fout.is_open())
			throw "Input or output file not opening exception";
		else
		{
			int size=0;
			fin >> size;

			for (int x=0;x<size && fin.good();x++)
			{
				int arr_size=0;
				int orignal_size;
				fin >>arr_size;
				orignal_size=arr_size;

				vector<double> ptr;
				vector<double>  ptr1; 
				
				vector<double> ptr3;
				vector<double>  ptr4; 
				
				for (int y=0;y<arr_size;y++)
				{
					double temp=0;
					fin >> temp;
					ptr.push_back(temp);
					ptr3.push_back(temp);
				}
				
				for (int y=0;y<arr_size;y++)
				{
					double temp=0;
					fin >> temp;
					ptr1.push_back(temp);
					ptr4.push_back(temp);
				}
				

				int win=0;
				int loose=0;
				while (arr_size>0)
				{

					while (arr_size>0 && ptr[smallest(ptr,arr_size)] > ptr1[smallest(ptr1,arr_size)]) //get points by bluffing 
					{
						ptr.erase(ptr.begin()+smallest(ptr,arr_size));
						ptr1.erase(ptr1.begin()+smallest(ptr1,arr_size));
						win++;
						arr_size--;

					}

					if (arr_size >0)
					{
						int his_largest = largest(ptr1,arr_size);
						int my_smallest = smallest(ptr,arr_size);
					
						if (ptr[my_smallest] > ptr1[his_largest]) //break out win
						{
							win+=arr_size;
							break;
						}

						else
						{
							loose++;
							ptr1.erase(ptr1.begin()+his_largest);
							ptr.erase(ptr.begin()+my_smallest);
							arr_size--;

							
						}
					}

				}
				int win1=0;
				int loose1=0;
				while (orignal_size >0)
				{
					int my_smallest = smallest(ptr3,orignal_size);
					int his_smallest = smallest_to_beat_me(ptr4,orignal_size,ptr3[my_smallest]);
					
					if (his_smallest ==-1)
					{
						win1+=orignal_size;
						break;
					}
					else
					{
						loose1++;
						orignal_size--;
						ptr3.erase(ptr3.begin()+my_smallest);
						ptr4.erase(ptr4.begin()+his_smallest);
					}
				}
				fout <<"Case #" <<x+1<<": ";
				fout << win <<" " << win1<<endl;
				
			}
		}
	}
	catch (string a)
	{
		cout <<endl << "EXCEPTION : " << a <<endl;
	}
	return 0;
}
