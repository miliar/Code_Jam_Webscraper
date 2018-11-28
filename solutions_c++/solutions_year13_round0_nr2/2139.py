#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<iterator>
using namespace std;

inline int scan()
{
    int po=0;
    char ch;
    ch=getchar_unlocked();
    while(ch<'0' || ch>'9')
        ch=getchar_unlocked();
    while(ch>='0' && ch<='9')
    {
        po=(po<<3)+(po<<1)+ch-'0';
        ch=getchar_unlocked();
    }
    return po;
}
int maxi(int *a, int n)
{
	int maxim =0;
	for(int i =0; i< n; i++)
		if(a[i]>maxim)
			maxim=a[i];
	return maxim;
}
int main() {
	int test;
	test = scan();
	for(int t=0; t<test; t++) {	
		int n=scan(), m=scan();
		int des[n][m], lawn[n][m];
		/*int **des = (int **)malloc(n*sizeof(int*));
		for(int i=0; i<n; i++)
			des[i] = (int*)malloc(m*sizeof(int));*/
		for(int i=0; i<n; i++) 
			for(int j=0; j<m; j++) 
				cin>>des[i][j];		
		
		/*int **lawn = (int **)malloc(n*sizeof(int*));
		for(int i=0; i<n; i++)
			lawn[i] = (int*)malloc(m*sizeof(int));*/
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++) 
				lawn[i][j]=100;	
				
		int *row = (int *)malloc(m*sizeof(int));
		int maxima;				
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++)
				row[j]=des[i][j];
			maxima = maxi(row,m);
			for(int j=0; j<m; j++) {
				if(lawn[i][j]>maxima)
					lawn[i][j]=maxima;
			}
		}
		int *column = (int *)malloc(n*sizeof(int));				
		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++)
				column[j]=des[j][i];
			maxima = maxi(column,n);
			for(int j=0; j<n; j++) {
				if(lawn[j][i]>maxima)
					lawn[j][i]=maxima;
			}
		}
			
		bool check=true;
		
		for(int i=0; i<n; i++){ 
			for(int j=0; j<m; j++) 
				if(lawn[i][j]!=des[i][j]){
					check = false;
					break;
				}	
		}
		
		if(check)
			cout<<"Case #"<<t+1<<": "<<"YES"<<endl;	
		else
			cout<<"Case #"<<t+1<<": "<<"NO"<<endl;
	}
	return 0;
}
