#include <iostream>
using namespace std;


void qsort( float* array, int leftbound , int rightbound )
{
    int i,j;
    float tmp;
    for(i=0;i<rightbound;i++)
    {
    	for(j=i;j<rightbound;j++)
    	{
    		if(array[i]>array[j])
    		{
    			tmp = array[i];
    			array[i] = array[j];
				array[j] = tmp;
    		}
    	}
    }
}


int main() {
	// your code goes here
	int i,f,n,j,war,dwar,d,k;
	float naomi[10],ken[10],temp[10];
	scanf("%d",&f);
	for(i=0;i<f;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%f",&naomi[j]);
		}
		for(j=0;j<n;j++)
		{
			scanf("%f",&ken[j]);
		}
		qsort(naomi,0,n);
		qsort(ken,0,n);
		war=0;
		for(j=0;j<n;j++)
		{
			temp[j]=ken[j];
		}
		
		for(j=0;j<n;j++)
		{
			k=0;
			while(ken[k]<naomi[j] && k<n){
				k++;
			}
			if(k==n)
			{
				war++;
				d=0;
				while(ken[d]==0){
					d++;
				}
				ken[d]=0;
			}
			else
			{
				ken[k]=0;
			}
		}
		dwar=0;
		j=0;
		while(naomi[j]<temp[0])
		{
			j++;
		}
	
		k=0;
		for(;j<n;j++){
			if(naomi[j]>temp[k])
			{
			
				dwar++;
				k++;
			}
		}
		
		printf("Case #%d: %d %d\n",i+1,dwar,war);
	}
	
	
	return 0;
}