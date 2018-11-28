#include <iostream.h>
#include <fstream>
#include <vector>
using namespace std;
void  user_sort(int *array,int size){
	bool done = false;
    while ( ! done)
    {
        done = true;
        for (int i = 0 ; i < size-1 ; i++)
        {
            if (array[i] > array[i+1])
            {
                done = false;
				std::swap(array[i], array[i+1]);
            }
        }
        size--;
    }

	

}
int main(){
	FILE * fileI = fopen("1.in","r");
	FILE * fileO = fopen("1.out","w");

	int numT ;
	int A;
	int N;
	fscanf(fileI,"%d",&numT);
	for(int i=0;i<numT;i++){
		fprintf(fileO,"Case #%d: ",i+1);
		
		fscanf(fileI,"%d",&A);
		fscanf(fileI,"%d",&N);
		int *other = new int[N];
		int temp;
		int j;
		for( j=0;j<N;j++){
			fscanf(fileI,"%d",&temp);
			other[j]=temp;
			
		}
		
		user_sort(other,N);
		int numO =0;
		int minO = N;
		bool setMinO=false;
		for( j=0;j<N;j++){
			if(other[j]<A){
				A+=other[j];

			}
			else{
				if(N-j+numO<minO){
					minO = N-j+numO;
				}
				while(1){
					numO++;
					if(numO==minO){
						break;
					}
					if(other[j]<A+A-1){
						A+=A-1+other[j];
						break;
					}
					else{
						A+=A-1;
					}
					
				}
			}
			if(numO>=minO){
				numO = minO;
				break;
			}
			
		}

		fprintf(fileO,"%d\n",numO);
		delete other;

	}
	fclose(fileI);
	fclose(fileO);
	return 0;
}