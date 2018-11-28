#include <iostream>
using namespace std;

#include <stdio.h>
#include <stdlib.h>


int cmpfunc (const void * a, const void * b)
{
   if ((*(double*)a) > (*(double *)b) ) {
   			return 1;
   } else {
   	return -1;
   }
}

int main()
{
   int T,N ,n;
   double * arr1 ,*arr2;
   cin>>T;
   for(int t=1;t<=T;t++){
   	cin>>N;
   	arr1 = (double*)malloc(N*sizeof(double));
   	arr2 = (double *)malloc(N*sizeof(double));
   	for(int i=0;i<N;i++){
   		cin>>arr1[i];
   	}
   	for(int i=0;i<N;i++){
   		cin>>arr2[i];
   	}
   	qsort(arr1, N , sizeof(double), cmpfunc);
   	qsort(arr2, N , sizeof(double), cmpfunc);

   	int ia=0,ib=0,ja=N-1 , jb=N-1;
   	int awin1=0,bwin1=0,awin2=0,bwin2=0;
   	while(awin1+bwin1<N && ia<=ja && ib<=jb){
   		while(ia<=ja && ib<=jb && arr1[ia]>arr2[ib] ){
   			awin1++;
   			ja--;
   			ib++;
   		}
   		while(ia<=ja && ib<=jb && arr1[ia]<arr2[ib] ){
   			bwin1++;
   			ia++;
   			ib++;
   		}
   	}
   	ia=0,ib=0,ja=N-1 , jb=N-1;
   	while(awin2+bwin2<N && ia<=ja && ib<=jb){
   		while(ia<=ja && ib<=jb && arr1[ia]<arr2[ib] ){
   			bwin2++;
   			jb--;
   			ia++;
   		}
   		while(ia<=ja && ib<=jb && arr1[ia]>arr2[ib] ){
   			awin2++;
   			ia++;
   			ib++;
   		}
   	}
  	free (arr1);
   	free(arr2);
  	arr1=NULL;
  	arr2=NULL;

	cout<<"Case #"<<t<<": "<<awin2<<" "<<awin1<<endl;

   }
  return(0);
}