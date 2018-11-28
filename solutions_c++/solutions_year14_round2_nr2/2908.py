#include<iostream>
#include<cstdio>
#include<string>
#include <stdio.h>
using namespace std;

int T, k, l;
unsigned int a, b;
FILE *plik;
	    

int main()
{ 
	scanf("%d", &T);
	plik = fopen("wynikB.txt", "w");
	for (int i =0; i<T; i++){
		cin>>a>>b>>k;
		fprintf(plik, "Case #%d: ", i+1);
		cout<<"Case #"<<i+1<<": ";
        l = a+b-1;
        for( int i =1; i< a; i++){
            for(int j=1; j<b; j++){
                if((i & j )< k){
                     l++;
                    }
            }
        }
        cout<<l<<endl;
        fprintf(plik, "%d\n", l);
    }
    cin.ignore();
    getchar();
    return 0;
}    
