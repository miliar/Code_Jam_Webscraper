#include<iostream>
using namespace std;
int getGreatest(double arr[], int N){
	int g=0;
	for(int i=1; i<N; i++){
		if(arr[i]==0)
			continue;
		if(arr[g]<arr[i])
			g=i;
	}
	return g;
}
int getGreaterThan(double arr[], int N, double x){
	int index=-1;
	double diff=1;
	for(int i=0; i<N; i++){
		if(arr[i]>x && (arr[i]-x)<diff){
			diff=arr[i]-x;
			index=i;
		}
	}
	return index;
}
int getSmallerThan(double arr[], int N, double x){
	int index=-1;
	double diff=1;
	for(int i=0; i<N; i++){
		if(arr[i]==0)
			continue;
		if(arr[i]<x && (x-arr[i])<diff){
			diff=x-arr[i];
			index=i;
		}
	}
	return index;
}
int getsmallest(double arr[], int N){
	int i,g;
	for(i=0; i<N; i++){
		if(arr[i]>0){
			g=i;
			break;
		}
	}
	for(i=1; i<N; i++){
		if(arr[i]==0)
			continue;
		if(arr[g]>arr[i])
			g=i;
	}
	return g;
}

int getWar(int N, double naomi[], double ken[]){
	int i,si,ngi, Wn=0;
	for(i=0; i<N; i++){
		ngi=getGreaterThan(ken, N, naomi[i]);
		if(ngi==-1){
			ken[getsmallest(ken,N)]=0;
			Wn++;
		}
		else
			ken[ngi]=0;
		naomi[i]=0;
	}
	return Wn;
}

int getDecentWar(int N, double naomi[], double ken[]){
	int i,nsi,Wn=0;
	for(i=0; i<N; i++)
	{
		nsi=getSmallerThan(ken,N,naomi[i]);
		if(nsi==-1)
			ken[getGreatest(ken,N)]=0;
		else
		{
			ken[nsi]=0;
			naomi[i]=0;
			Wn++;
		}
	}
	return Wn;
}

int main(){
	int T, N, n, i,dw,w;
	double ken[1010], naomi[1010],ken1[1010], naomi1[1010];
	cin>>T;
	for(n=1; n<=T; n++){
		cin>>N;
		for(i=0; i<N; i++){
			cin>>naomi[i];
			naomi1[i]=naomi[i];
		}
		for(i=0; i<N; i++){
			cin>>ken[i];
			ken1[i]=ken[i];
		}
		dw=getDecentWar(N,naomi,ken);
		w=getWar(N,naomi1,ken1);
		cout<<"Case #"<<n<<": "<<dw<<" "<<w<<endl;
	}
	return 0;
}
