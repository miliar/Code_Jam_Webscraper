#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>
#include <iomanip>

#define re
using namespace std;


int t,n;
double *naomi, *ken, *temp_ken;

void swap(double *a,int i , int j)
{
double temp = a[i];
a[i]=a[j];
a[j]=temp;
}

void qsort(double *a,int left,int right)
{
int i, last;

if (left >= right) 
return;
swap(a,left, (left + right)/2); 
last = left;
for (i = left + 1; i <= right; i++) 
if (a[i] < a[left])
swap(a, ++last, i);
swap(a, left, last);

qsort(a, left, last-1);
qsort(a, last+1, right);
}

void solve(int case_no){

	qsort(naomi,0,n-1);
	qsort(ken,0,n-1);

	qsort(temp_ken,0,n-1);


	int naomi_decietful_win = 0;
	int naomi_fair_win = n;

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if( ken[j]!=-1){
			if(naomi[i]>ken[j]){
				naomi_decietful_win++;
				ken[j] = -1;
			}else if(naomi[i]<ken[j]){
				for(int k=n-1;k>=0;k--){
					if(ken[k]!=-1){
						ken[k] =-1;
						break;
					}
				}
			}
			break;
		}
		}

	}

	for(int i=0;i<n;i++){
	for(int j=0;j<n;j++){
		if(temp_ken[j]!=-1){
			if(temp_ken[j] > naomi[i]){
				temp_ken[j] = -1;
				naomi_fair_win--;
				break;
			}
		}

	}

}
cout<<"Case #"<<case_no<<": "<<naomi_decietful_win<<" "<<naomi_fair_win<<endl;


}


int main(int argc, char const *argv[])
{
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif

cin>>t;
for(int j=1;j<=t;j++){
	cin>>n;
	naomi = new double[n];
	ken = new double[n];
	temp_ken = new double[n];
	for(int i=0;i<n;i++){
		cin>>naomi[i];
	}
	for(int i=0;i<n;i++){
		cin>>ken[i];
		temp_ken[i] = ken[i];
	}

	solve(j);
}
    	
/*#ifdef re
printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif*/
return 0;
}
