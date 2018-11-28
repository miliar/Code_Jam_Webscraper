/**************************************************
                  Believe 
***************************************************/
#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define pb push_back
//memset(array,0,sizeof(array));
//array[m][n]={{0}};

int main(){
	 ios_base::sync_with_stdio(false);
	 ofstream output;
	 output.open("1.txt");
	 string s;
	 long  t;
	 long  array[10]; 
	 long  a[5];
	 cin>>t;
	 for(long f=1;f<=t;f++){
	 	memset(array,0,sizeof(array));
	    memset(a,0,sizeof(a));
	 	cin>>s;
	 	for(long i=0;i<s.length();i++){
	 		if(s[i]=='O'){
	 			a[0]++;
	 		}
	 		if(s[i]=='H'){
	 			a[1]++;
	 		}
	 		if(s[i]=='F'){
	 			a[2]++;
	 		}
	 		if(s[i]=='S'){
	 			a[3]++;
	 		}
	 		if(s[i]=='I'){
	 			a[4]++;
	 		}

	 		if(s[i]=='Z'){
	 			array[0]++;
	 		}
	 		if(s[i]=='W'){
	 			array[2]++;
	 		}
	 		if(s[i]=='U'){
	 			array[4]++;		
	 		}
	 		if(s[i]=='X'){
	 			array[6]++;
	 		}
	 		if(s[i]=='G'){
	 			array[8]++;
	 		}
	 		
	 		
	 	}
	 	array[1]=a[0]-array[2]-array[4]-array[0];
	 	array[3]=a[1]-array[8];
	 	array[5]=a[2]-array[4];
	 	array[7]=a[3]-array[6];
	 	array[9]=a[4]-array[6]-array[8]-array[5];
	 	output<<"Case #"<<f<<": ";
	 	for(long i=0;i<10;i++){
	 		for(long j=1;j<=array[i];j++){
	 			output<<i;
	 		}
	 	}
	 	output<<""<<endl;
	 }


return 0;
}