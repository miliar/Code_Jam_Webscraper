#include<stdio.h>
int mots[100];
int motN;
int armin;
void swap(int *a, int *b){
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}
void sort_array(int array[],int size){
	
	int i,ii;
	for(i=0;i<size;i++)
	for(ii=i+1;ii<size;ii++)
	if(array[i]>array[ii]){
		swap(&array[i], &array[ii]);
	}
}
void eat(){
	int i,r=0;
	for(i=0;i<motN;i++){
		if(mots[i]!=0 && armin>mots[i]){
			armin+=mots[i];
			mots[i]=0;
			r=1;
		}
	}
	if(r) eat();
}
int recurs(){
	int a,b,tot=0,i;
	int yedek[100],yedarm;
	for(i=0;i<motN;i++){
		yedek[i]=mots[i];
	}
	yedarm=armin;
	eat();
	for(i=0;i<motN;i++){
		tot+=mots[i];
	}
	if(tot==0) return 0;
	motN--;
	a=recurs()+1;
	motN++;
	
	for(i=0;i<motN;i++)
	mots[i]=yedek[i];
	armin=yedarm;
	
	eat();
	for(i=0;i<motN;i++){
		tot+=mots[i];
	}
	if(tot==0) return 0;
	
	armin+=armin-1;
	b=recurs()+1;
	armin=(armin+1)/2;
	
	for(i=0;i<motN;i++)
	mots[i]=yedek[i];
	armin=yedarm;
	
	if(a>b){
		return b;
	}
	return a;
}
int main(){
	int i,T,ii;
	scanf("%d",&T);
	for(i=0;i<T;i++){
		scanf("%d %d",&armin,&motN);
		for(ii=0;ii<motN;ii++){
			scanf("%d",&mots[ii]);
		}
		sort_array(mots,motN);
		if(armin==1)
		printf("Case #%d: %d\n",i+1,motN);
		else
		printf("Case #%d: %d\n",i+1,recurs());
	}
	scanf("%d",&i);
	return 0;
}
