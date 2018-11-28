#include <iostream>
#include <stdio.h>

using namespace std;

struct range {
    int min,max;
};

int main(int argc, char** argv) {
    int t,count=0;
    range input[101];
    cin>>t;
    for(int i=0;i<t;i++){
        scanf("%d %d",&input[i].min,&input[i].max);
    }
    
    for(int k=0 ; k<t ; k++){
		count = 0;
		if(input[k].min<=1&&1<=input[k].max)
			count++;
		if(input[k].min<=4&&4<=input[k].max)
			count++;
		if(input[k].min<=9&&9<=input[k].max)
			count++;
		if(input[k].min<=121&&121<=input[k].max)
			count++;
		if(input[k].min<=484&&484<=input[k].max)
			count++;
		cout<<"\nCase #"<<k+1<<": "<<count;
    }
	return 0;
}
    
