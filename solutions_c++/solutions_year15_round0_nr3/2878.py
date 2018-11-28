#include <vector>
#include <algorithm>
#include <fstream>
#include <stdlib.h> 
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stack>
#include <string.h>
#include <iomanip>
#include <sstream>
#include <map>
#include <set>

using namespace std;
int main()
{
   	freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
     int i, numCase, ans=0;
	cin>>numCase;
	for(i=0; i<numCase; i++){
		int l, x;
		bool yes=false, no=false;
		cin>>l>>x;
		string s, concat;
		cin>>s;	
		for(int j=0; j<x; j++){
			concat=concat+s;
		}
		int size=concat.length();
		int num[10000], quat1[10000], quat2[10000];
		for(int j=0; j<size; j++){
			if(concat[j]=='i'){
				num[j]=2;
			}
			else if(concat[j]=='j'){
				num[j]=3;
			}
			else if(concat[j]=='k'){
				num[j]=4;
			}
		}
    	quat1[0]=num[0];
    	for(int j=1; j<size; j++){
    		if(quat1[j-1]==-4){
    			if(num[j]==2){
    				quat1[j]=-3;
    			}
    			else if(num[j]==3){
    				quat1[j]=2;
    			}
    			else if(num[j]==4){
    				quat1[j]=1;
    			}
    		}
    		else if(quat1[j-1]==-3){
    			if(num[j]==2){
    				quat1[j]=4;
    			}
    			else if(num[j]==3){
    				quat1[j]=1;
    			}
    			else if(num[j]==4){
    				quat1[j]=-2;
    			}
    		}
    		else if(quat1[j-1]==-2){
    			if(num[j]==2){
    				quat1[j]=1;
    			}
    			else if(num[j]==3){
    				quat1[j]=-4;
    			}
    			else if(num[j]==4){
    				quat1[j]=3;
    			}
    		}
    		else if(quat1[j-1]==-1){
    			if(num[j]==2){
    				quat1[j]=-2;
    			}
    			else if(num[j]==3){
    				quat1[j]=-3;
    			}
    			else if(num[j]==4){
    				quat1[j]=-4;
    			}
    		}
    		else if(quat1[j-1]==1){
    			if(num[j]==2){
    				quat1[j]=2;
    			}
    			else if(num[j]==3){
    				quat1[j]=3;
    			}
    			else if(num[j]==4){
    				quat1[j]=4;
    			}
    		}
    		else if(quat1[j-1]==2){
    			if(num[j]==2){
    				quat1[j]=-1;
    			}
    			else if(num[j]==3){
    				quat1[j]=4;
    			}
    			else if(num[j]==4){
    				quat1[j]=-3;
    			}
    		}
    		else if(quat1[j-1]==3){
    			if(num[j]==2){
    				quat1[j]=-4;
    			}
    			else if(num[j]==3){
    				quat1[j]=-1;
    			}
    			else if(num[j]==4){
    				quat1[j]=2;
    			}
    		}
    		else if(quat1[j-1]==4){
    			if(num[j]==2){
    				quat1[j]=3;
    			}
    			else if(num[j]==3){
    				quat1[j]=-2;
    			}
    			else if(num[j]==4){
    				quat1[j]=-1;
    			}
    		}
    	}
    	quat2[size-1]=num[size-1];
    	for(int j=size-1; j>=1; j--){
    		if(quat2[j]==-4){
    			if(num[j-1]==2){
    				quat2[j-1]=3;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=-2;
    			}
    			else if(num[j]==4){
    				quat2[j-1]=1;
    			}
    		}
    		else if(quat2[j]==-3){
    			if(num[j-1]==2){
    				quat2[j-1]=-4;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=1;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=2;
    			}
    		}
    		else if(quat2[j]==-2){
    			if(num[j-1]==2){
    				quat2[j-1]=1;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=4;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=-3;
    			}
    		}
    		else if(quat2[j]==-1){
    			if(num[j-1]==2){
    				quat2[j-1]=-2;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=-3;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=-4;
    			}
    		}
    		else if(quat2[j]==1){
    			if(num[j-1]==2){
    				quat2[j-1]=2;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=3;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=4;
    			}
    		}
    		else if(quat2[j]==2){
    			if(num[j-1]==2){
    				quat2[j-1]=-1;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=-4;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=3;
    			}
    		}
    		else if(quat2[j]==3){
    			if(num[j-1]==2){
    				quat2[j-1]=4;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=-1;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=-2;
    			}
    		}
    		else if(quat2[j]==4){
    			if(num[j-1]==2){
    				quat2[j-1]=-3;
    			}
    			else if(num[j-1]==3){
    				quat2[j-1]=2;
    			}
    			else if(num[j-1]==4){
    				quat2[j-1]=-1;
    			}
    		}
    	}
    	
    	int index=0;
		if(quat1[size-1]!=-1){
			no=true;
		}
		else{
			int i0=0, i1=size-1;
			for(i0=0; i0<size; i0++){
				if(quat1[i0]==2){
					break;
				}
			}
			for(i1=size-1; i1>=0; i1--){
				if(quat2[i1]==4){
					break;
				}
			}
			if(i1 > i0){
				yes=true;
			}
			else{
				no=true;
			}
		}
		if(yes){
			cout << "Case #" << (i+1) << ": "<<"YES"<<endl;
		}
		else{
			cout << "Case #" << (i+1) << ": "<<"NO"<<endl;
		}
	}
    
    return 0;
}
