#include<stdio.h>
#include<process.h>
int arrayfull(long long int arr[])
 {
	long long int i,c=0;
	for(i=0;i<10;i++){
		if(arr[i]==i){
			c++;
		 }
	 }
	if(c==10)
	return 1;
	else
	return 0;
}
int main()
{
	FILE *input, *output;
	input=fopen("input.in","r");
	if(input==NULL)
	{
		printf("ERROR");
	    exit(0);
	}
	output=fopen("output.in","w");
	if(output==NULL)
	{
		printf("ERROR");
	    exit(0);
	}
	long long int n1,k, i,j,t,l=1,n,m,temp,num;
	fscanf(input,"%lld",&t);
	while(l< (t+1)){
		long long int arr[10]={-1};
		fscanf(input,"%lld",&n);
		if(n==0)
		fprintf(output,"Case #%lld: INSOMNIA\n",l);
		else{
			for(i=1;;i++){
				temp=n*i;
				n1=temp;
			    for(j=1;n1!=0;j++)
				{
			        num=n1%10;
			        
			        arr[num]=num;
			        n1=n1/10;
		        }
		      if(arrayfull(arr)==1)
			    {
				fprintf(output,"Case #%lld: %lld\n",l,temp);
				break;
				}
		    k++;     
	        }
		}
l++;
}
	return 0;
}
