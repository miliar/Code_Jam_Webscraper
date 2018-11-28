#include<iostream>
#include<cmath>
#include <set>
#include <vector>
#include <fstream>
using namespace std;
int main (){
	ifstream fin ("A-large.in");
	ofstream fout ("out.txt");
    int t,test;
    fin >> t;
    bool nums[10];
    long long count;
    for (test=1;test<=t;test++) {
        long long i=0,j,n,num,res;
        fin >> n;
        num = n;
        if (n==0){
            fout << "Case #" << test << ": " <<"INSOMNIA"<<endl;
        }else{
        	for (i=0;i<10;i++){
        		nums[i] = false;
			}
			
        	for (i=1;;i++){
			
        	
        	count = 0;
			for (j=0;j<10;j++){
				if (nums[j] == true){
					count++;
				}
			}
			
			if(count ==10){
				fout << "Case #" << test << ": " << n*(i-1)<<endl;
				break;
			}
			num = n*i;
			while(num>0){
				
				nums[num%10] = true;
				num= num/10;
			}
				
						
				
		    }
        
        }
        
        
        
        
        
        
    }
    
    
    
    
    return 0;
}
